%global __brp_check_rpaths %{nil}
%global install_path /opt/mozjpeg

Name:           mozjpeg
Version:        4.0.3
Release:        1%{?dist}
Summary:        Mozilla JPEG Encoder Project — improved JPEG encoder

License:        BSD
URL:            https://github.com/mozilla/%{name}
Source0:        https://github.com/mozilla/%{name}/archive/v%{version}.zip

BuildRequires:  gcc
BuildRequires:  nasm
BuildRequires:  cmake
BuildRequires:  zlib-static
BuildRequires:  libpng-static


%package devel
Summary:        Development headers for MozJPEG library
Requires:       %{name}%{?_isa} = %{version}-%{release}


%package static
Summary:        Static version of MozJPEG library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}


%description
MozJPEG reduces file sizes of JPEG images while retaining quality and
compatibility with the vast majority of the world's deployed decoders.

MozJPEG is based on libjpeg-turbo. MozJPEG makes tradeoffs that are
intended to benefit Web use cases and focuses solely on improving
encoding, so it's best used as part of a Web encoding workflow.

This package does not replace libjpeg-turbo. MozJPEG is installed
to /opt directory.


%description devel
This package contains header files and libraries needed to develop
software that use the MozJPEG library.


%description static
This package contains static libraries needed to develop
software that use the MozJPEG library.


%prep
%autosetup


%build
%cmake -DCMAKE_INSTALL_PREFIX=%{install_path} .
%cmake_build


%install
%cmake_install
find %{buildroot} -name '*.la' -delete


%files
%dir %{install_path}
%{install_path}/bin/*
%{install_path}/%{_lib}/*.so.*
%{install_path}/man/*


%files devel
%{install_path}/%{_lib}/*.so
%{install_path}/%{_lib}/pkgconfig/*
%{install_path}/include/*
%{install_path}/doc/*


%files static
%{install_path}/%{_lib}/*.a


%changelog
* Tue Mar 2 2021 Tomasz Gąsior
- Upstream update
* Sat Dec 5 2020 Tomasz Gąsior
- Upstream update
- Split development files into separate packages
* Sun Nov 17 2019 Tomasz Gąsior
- Initial
