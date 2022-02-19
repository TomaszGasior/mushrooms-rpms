# this spec is based on:
# https://src.fedoraproject.org/rpms/php-Assetic/blob/6f39e013606437e4fdde905d7b9ed32a8607fdf8/f/php-Assetic.spec

%global phpdir %{_datadir}/php

Name:           symfony-console-autocomplete
Version:        1.5.3
Release:        1%{?dist}
Summary:        Bash autocompletion for Symfony Console based scripts

License:        MIT
URL:            https://github.com/bamarni/%{name}
Source0:        https://github.com/bamarni/%{name}/archive/v%{version}.tar.gz

BuildRequires:  php
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  php-composer(symfony/console)
BuildRequires:  php-composer(symfony/process)
Requires:       bash
Requires:       bash-completion
BuildArch:      noarch


%description
Enables shell autocompletion for tools based on the Symfony Console
(Symfony framework, Composer, PHPSpec, Behat, etc.).

Please remember to restart your terminal after installation.


%prep
%autosetup

mkdir vendor
cat <<'AUTOLOAD' | tee vendor/autoload.php
<?php
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4(
    'Bamarni\\Symfony\\Console\\Autocomplete\\',
    __DIR__.'/../src'
);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Symfony4/Component/Console/autoload.php',
    '%{phpdir}/Symfony4/Component/Process/autoload.php',
]);
AUTOLOAD


%build
bin/symfony-autocomplete > symfony-console


%install
mkdir -p %{buildroot}/%{_sysconfdir}/bash_completion.d
install -m 644 symfony-console %{buildroot}/%{_sysconfdir}/bash_completion.d


%files
%{_sysconfdir}/bash_completion.d/symfony-console


%changelog
* Sat Feb 19 2022 Tomasz Gąsior
- Upstream update

* Sun Oct 31 2021 Tomasz Gąsior
- Upstream update

* Sun Jul 26 2020 Tomasz Gąsior
- Upstream update

* Thu Mar 5 2020 Tomasz Gąsior
- Upstream update

* Sun Nov 10 2019 Tomasz Gąsior
- Initial
