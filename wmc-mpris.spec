Name:           wmc-mpris
Version:        0.1.0
Release:        1%{?dist}
Summary:        MPRIS proxy for Web Media Controller

License:        Unlicense
URL:            https://github.com/f1u77y/%{name}
Source0:        https://github.com/f1u77y/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires:       glib2
Requires:       json-glib
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel


%description
MPRIS proxy for usage with Web Media Controller on GNU/Linux. This is
required for web-media-controller Firefox extension which can be
downloaded from https://github.com/f1u77y/web-media-controller/releases.


%prep
%autosetup


%build
%cmake
%cmake_build


%install
%cmake_install
mv %{buildroot}/usr/lib %{buildroot}/%{_libdir}


%files
%{_bindir}/*
%{_sysconfdir}/chromium/native-messaging-hosts/*
%{_sysconfdir}/opt/chrome/native-messaging-hosts/*
%{_libdir}/mozilla/native-messaging-hosts/*


%changelog
* Sun Feb 09 2020 Tomasz Gąsior
- Initial