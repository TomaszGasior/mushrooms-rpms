Name:           symfony-console-autocomplete
Version:        1.3.5
Release:        1%{?dist}
Summary:        Bash autocompletion for Symfony Console based scripts

License:        MIT
URL:            https://github.com/bamarni/%{name}
Source0:        https://github.com/bamarni/%{name}/archive/v%{version}.tar.gz

BuildRequires:  composer
Requires:       bash
Requires:       bash-completion
BuildArch:      noarch


%description
Enables shell autocompletion for tools based on the Symfony Console
(Symfony framework, Composer, PHPSpec, Behat, etc.).

Please remember to restart your terminal after installation.


%prep
%setup
composer install --no-dev


%build
bin/symfony-autocomplete > symfony-console


%install
mkdir -p %{buildroot}/%{_sysconfdir}/bash_completion.d
install -m 644 symfony-console %{buildroot}/%{_sysconfdir}/bash_completion.d


%files
/%{_sysconfdir}/bash_completion.d/symfony-console


%changelog
* Sun Nov 10 2019 Tomasz Gąsior
- Initial