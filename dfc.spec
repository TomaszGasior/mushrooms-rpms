Name:           dfc
Version:        3.1.1
Release:        1%{?dist}
Summary:        Report file system space usage information with style

License:        BSD 3-Clause
URL:            https://github.com/Rolinh/%{name}
Source0:        https://github.com/Rolinh/%{name}/archive/v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  gettext


%description
dfc is a tool to report file system space usage information.
When the output is a terminal, it uses color and graphs by default.
It has a lot of features such as HTML, JSON and CSV export, multiple
filtering options, the ability to show mount options and so on.


%prep
%autosetup


%build
%cmake -DPREFIX=%{_prefix} -DSYSCONFDIR=%{_sysconfdir} -B .
%make_build


%install
%make_install
%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/*
%{_sysconfdir}/xdg/dfc
%{_docdir}/dfc
%{_mandir}/*


%changelog
* Sun Jul 26 2020 Tomasz Gąsior
- Initial