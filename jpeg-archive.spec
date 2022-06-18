%global debug_package %{nil}
%undefine _hardened_build

Name:           jpeg-archive
Version:        2.2.0
Release:        5%{?dist}
Summary:        Utilities for archiving JPEGs for long term storage

License:        MIT
URL:            https://github.com/danielgtaylor/%{name}
Source0:        https://github.com/danielgtaylor/%{name}/archive/v%{version}.zip

BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  mozjpeg-static


%description
Utilities for archiving photos for saving to long term storage
or serving over the web. The goals are:
- Use a common, well supported format (JPEG),
- Minimize storage space and cost,
- Identify duplicates / similar photos.


%prep
%autosetup


%build
export CFLAGS="$CFLAGS -fcommon"
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
