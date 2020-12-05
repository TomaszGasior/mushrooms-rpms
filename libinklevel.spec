Name:           libinklevel
Version:        0.9.3
Release:        2%{?dist}
Summary:        Library for checking the ink level of your printer

License:        GPL
URL:            http://libinklevel.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

Requires:       libusb1
BuildRequires:  libusb1-devel
BuildRequires:  autoconf
BuildRequires:  gcc


%package devel
Summary:       Development headers for libinklevel library
Requires:      %{name}%{?_isa} = %{version}-%{release}


%package static
Summary:       Static version of libinklevel library
Requires:      %{name}-devel%{?_isa} = %{version}-%{release}


%description
Libinklevel is a library for checking the ink level of your printer. It supports
printers attached via USB. Currently printers of the following brands are supported:
HP, Epson and Canon. Canon BJNP network printers are supported too. 

A detailed list of supported printers is available:
http://libinklevel.sourceforge.net/#supported.

This is not official software from the printer manufacturers. The goal of this
project is to create a vendor independent API for retrieving the ink level of
a printer connected to a Linux or FreeBSD box.


%description devel
This package contains header files and libraries needed to develop
software that use the libinklevel library.


%description static
This package contains static libraries needed to develop
software that use the libinklevel library.


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -delete


%files
%{_libdir}/libinklevel.so.*


%files devel
%{_libdir}/libinklevel.so
%{_includedir}/inklevel.h
%{_docdir}/libinklevel/*


%files static
%{_libdir}/libinklevel.a


%changelog
* Sat Dec 5 2020 Tomasz Gąsior
- Split development files into separate packages
* Sun Feb 09 2020 Tomasz Gąsior
- Initial