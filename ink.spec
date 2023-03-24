%global library_name libinklevel
%global library_version 0.9.5
%global library_release 1


Name:           ink
Version:        0.5.3
Release:        3%{?dist}
Summary:        Ink is a program to display the ink level of printers

License:        GPL
URL:            http://ink.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

Requires:       libinklevel
BuildRequires:  autoconf
BuildRequires:  gcc


%package -n %{library_name}
Version:        %{library_version}
Release:        %{library_release}%{?dist}
URL:            http://libinklevel.sourceforge.net/
Summary:        Library for checking the ink level of your printer
Source1:        https://downloads.sourceforge.net/%{library_name}/%{library_name}-%{library_version}.tar.gz
Requires:       libusb1
Requires:       libxml2
BuildRequires:  libusb1-devel
BuildRequires:  libxml2-devel


%package -n %{library_name}-devel
Version:        %{library_version}
Release:        %{library_release}%{?dist}
URL:            http://libinklevel.sourceforge.net/
Summary:        Development headers for libinklevel library
Requires:       %{library_name}%{?_isa} = %{version}-%{release}


%package -n %{library_name}-static
Version:        %{library_version}
Release:        %{library_release}%{?dist}
URL:            http://libinklevel.sourceforge.net/
Summary:        Static version of libinklevel library
Requires:       %{library_name}-devel%{?_isa} = %{version}-%{release}


%description
Ink is a command line tool for checking the ink level of your locally connected
printer. Currently printers of the following brands are supported: HP, Epson and 
Canon. Canon BJNP network printers are supported too. It makes use of libinklevel. 

A detailed list of supported printers is available:
http://libinklevel.sourceforge.net/#supported.


%description -n %{library_name}
Libinklevel is a library for checking the ink level of your printer. It supports
printers attached via USB. Currently printers of the following brands are supported:
HP, Epson and Canon. Canon BJNP network printers are supported too.

A detailed list of supported printers is available:
http://libinklevel.sourceforge.net/#supported.

This is not official software from the printer manufacturers. The goal of this
project is to create a vendor independent API for retrieving the ink level of
a printer connected to a Linux or FreeBSD box.


%description -n %{library_name}-devel
This package contains header files and libraries needed to develop
software that use the libinklevel library.


%description -n %{library_name}-static
This package contains static libraries needed to develop
software that use the libinklevel library.


%prep
%autosetup -a 1


%build
pushd %{library_name}-%{library_version}
%configure
%make_build
popd

export CPPFLAGS="$CPPFLAGS -I%{library_name}-%{library_version}"
export LDFLAGS="$LDFLAGS -L%{library_name}-%{library_version}/.libs"
%configure
%make_build


%install
pushd %{library_name}-%{library_version}
%make_install
find %{buildroot} -name '*.la' -delete
popd

%make_install


%files
%{_bindir}/ink
%{_mandir}/man1/ink*


%files -n %{library_name}
%{_libdir}/libinklevel.so.*


%files -n %{library_name}-devel
%{_libdir}/libinklevel.so
%{_includedir}/inklevel.h
%{_docdir}/libinklevel/*


%files -n %{library_name}-static
%{_libdir}/libinklevel.a


%changelog
* Fri Mar 24 2023 Tomasz Gąsior
- New release of libinklevel library with expanded printer support

* Sun Feb 09 2020 Tomasz Gąsior
- Initial