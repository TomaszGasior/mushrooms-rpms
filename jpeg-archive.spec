%global debug_package %{nil}
%undefine _hardened_build

%global mozjpeg_version 4.0.3

Name:           jpeg-archive
Version:        2.2.0
Release:        6%{?dist}
Summary:        Utilities for archiving JPEGs for long term storage

License:        MIT BSD
URL:            https://github.com/danielgtaylor/%{name}
Source0:        https://github.com/danielgtaylor/%{name}/archive/v%{version}.zip
Source1:        https://github.com/mozilla/mozjpeg/archive/v%{mozjpeg_version}.zip

BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  nasm
BuildRequires:  cmake
BuildRequires:  zlib-static
BuildRequires:  libpng-static


%description
Utilities for archiving photos for saving to long term storage
or serving over the web. The goals are:
- Use a common, well supported format (JPEG),
- Minimize storage space and cost,
- Identify duplicates / similar photos.


%prep
%autosetup -a 1


%build
pushd mozjpeg-%{mozjpeg_version}
%cmake -DCMAKE_INSTALL_PREFIX=$PWD
%cmake_build
%__cmake --install "%{__cmake_builddir}"
popd

export CFLAGS="$CFLAGS -fcommon"
export MOZJPEG_PREFIX=$PWD/mozjpeg-%{mozjpeg_version}
%make_build


%install
%make_install PREFIX=%{buildroot}/%{_prefix}


%files
%{_bindir}/jpeg-archive
%{_bindir}/jpeg-compare
%{_bindir}/jpeg-hash
%{_bindir}/jpeg-recompress


%changelog
* Sat Jun 18 2022 Tomasz Gąsior
- Fixed incompatibility with Fedora 36, using proper compile flags

* Tue Mar 2 2021 Tomasz Gąsior
- Update the package for newer mozjpeg

* Sat Apr 11 2020 Tomasz Gąsior
- Workaround incompatibility with GCC 10

* Sun Nov 17 2019 Tomasz Gąsior
- Initial
