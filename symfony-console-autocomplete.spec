Name:           symfony-console-autocomplete
Version:        1.5.5
Release:        3%{?dist}
Summary:        Bash autocompletion for Symfony Console based scripts

License:        MIT
URL:            https://github.com/bamarni/%{name}
Source0:        https://github.com/bamarni/%{name}/archive/v%{version}.tar.gz
Patch0:         plain-php-script.patch

BuildRequires:  php-cli
Requires:       bash
Requires:       bash-completion
BuildArch:      noarch


%description
Enables shell autocompletion for tools based on the Symfony Console
(Symfony framework, Composer, PHPSpec, Behat, etc.).

Please remember to restart your terminal after installation.


%prep
%autosetup -p 0


%build
php resources/bash/default.php > symfony-console


%install
mkdir -p %{buildroot}/%{_sysconfdir}/bash_completion.d
install -m 644 symfony-console %{buildroot}/%{_sysconfdir}/bash_completion.d


%files
%{_sysconfdir}/bash_completion.d/symfony-console


%changelog
* Sun May 3 2026 Tomasz Gąsior
- Packaging update

* Fri Dec 23 2022 Tomasz Gąsior
- Upstream update

* Mon Apr 11 2022 Tomasz Gąsior
- Upstream update

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
