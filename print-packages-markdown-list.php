#!/usr/bin/php
<?php

function git_get_all_branches(): array
{
    exec('git for-each-ref refs/heads --format="%(refname:short)" 2> /dev/null', $branches);

    return $branches;
}

function git_file_exists_on_branch(string $branch_name, string $file_name): bool
{
    exec(sprintf('git show %s:%s 2> /dev/null', $branch_name, $file_name), $output, $exit_code);

    return ! (int) $exit_code;
}

function git_file_get_contents_on_branch(string $branch_name, string $file_name): string
{
    exec(sprintf('git show %s:%s 2> /dev/null', $branch_name, $file_name), $output, $exit_code);

    if ($exit_code !== 0) {
        throw new Exception;
    }

    return implode(PHP_EOL, $output);
}

function rpm_get_field_from_spec_file(string $spec_file_name, string $field): string
{
    exec(sprintf('rpmspec -q --srpm --qf "%%{%s}" %s 2> /dev/null', $field, $spec_file_name), $output, $exit_code);

    if ($exit_code !== 0) {
        throw new Exception;
    }

    return $output[0];
}

function rpm_eval(string $expression): string
{
    exec(sprintf('rpm --eval "%s" 2> /dev/null', $expression), $output, $exit_code);

    if ($exit_code !== 0) {
        throw new Exception;
    }

    return implode(PHP_EOL, $output);
}

function get_package_names(): array
{
    return array_filter(git_get_all_branches(), function($branch_name){
        $is_dead = git_file_exists_on_branch($branch_name, 'dead.package');
        $has_spec_file = git_file_exists_on_branch($branch_name, sprintf('%s.spec', $branch_name));

        if ($is_dead || 'master' === $branch_name) {
            return false;
        }

        if (! $has_spec_file) {
            throw new Exception;
        }

        return $has_spec_file;
    });
}

function get_package_rpm_spec_file(string $package_name): string
{
    $rpm_spec = git_file_get_contents_on_branch($package_name, sprintf('%s.spec', $package_name));
    $temp_file_name = tempnam(sys_get_temp_dir(), 'print-pkg-list');

    file_put_contents($temp_file_name, $rpm_spec);
    register_shutdown_function(function() use ($temp_file_name){ unlink($temp_file_name); });

    return $temp_file_name;
}

function get_package_summary(string $package_name): string
{
    $rpm_spec_file = get_package_rpm_spec_file($package_name);
    $summary = rpm_get_field_from_spec_file($rpm_spec_file, 'summary');

    return rtrim($summary, '.');
}

function get_package_version(string $package_name): string
{
    $rpm_spec_file = get_package_rpm_spec_file($package_name);
    $version = rpm_get_field_from_spec_file($rpm_spec_file, 'version');
    $release = str_replace(rpm_eval('%dist'), '', rpm_get_field_from_spec_file($rpm_spec_file, 'release'));

    return sprintf('%s-%s', $version, $release);
}

function get_package_branch_url(string $package_name): string
{
    $github_repository_url = 'TomaszGasior/mushrooms-rpms';

    return sprintf('https://github.com/%s/tree/%s', $github_repository_url, $package_name);
}

function main(): void
{
    foreach (get_package_names() as $name) {
        $summary = get_package_summary($name);
        $url = get_package_branch_url($name);
        $version = get_package_version($name);

        printf("- [**%s**](%s) *%s*  \n  %s.\n", $name, $url, $version, $summary);
    }
}

main();
