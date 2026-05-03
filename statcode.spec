Name:           statcode
Version:        2.0.0
Release:        2%{?dist}
Summary:        Man pages for HTTP status codes

License:        MIT
URL:            https://github.com/shobrook/%{name}
Source0:        https://github.com/shobrook/%{name}/archive/v%{version}.zip

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
Requires:       python3
BuildArch:      noarch


%description
statcode is like man but for HTTP status codes. If you're a web
developer, you probably spend considerable time looking at response
codes (usually errors) and then Googling what they mean. But with
statcode, you can simply run `statcode [status_code]` and get a quick
explanation of your HTTP response without leaving the terminal.


%prep
%autosetup


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l statcode


%files -f %{pyproject_files}
%{_bindir}/statcode


%changelog
* Thu Feb 13 2020 Tomasz Gąsior
- Initial
