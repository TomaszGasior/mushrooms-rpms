Name:           phpunit-bash-completion
Version:        0.0.12
Release:        1%{?dist}
Summary:        PHPUnit shell completion for Bash

License:        BSD 3-Clause
URL:            https://github.com/sjorek/%{name}
Source0:        https://github.com/sjorek/%{name}/archive/v%{version}.tar.gz

Requires:       bash
Requires:       bash-completion
BuildArch:      noarch


%description
This package provides shell completion in Bash for PHPUnit. The completion 
routines support completing all options and arguments provided by PHPUnit.

Please remember to restart your terminal after installation.


%prep
%autosetup


%install
mkdir -p %{buildroot}/%{_sysconfdir}/bash_completion.d
install -m 644 phpunit-completion.bash %{buildroot}/%{_sysconfdir}/bash_completion.d


%files
%{_sysconfdir}/bash_completion.d/phpunit-completion.bash


%changelog
* Sun Oct 25 2020 Tomasz Gąsior
- Initial