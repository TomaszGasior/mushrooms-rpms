%global debug_package %{nil}

Name:           jpeg-archive
Version:        2.2.0
Release:        2%{?dist}
Summary:        Utilities for archiving JPEGs for long term storage

License:        MIT
URL:            https://github.com/danielgtaylor/%{name}
Source0:        https://github.com/danielgtaylor/%{name}/archive/v%{version}.zip

BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  mozjpeg
Requires:       mozjpeg


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
make %{?_smp_mflags}


%install
%make_install PREFIX=%{buildroot}/%{_prefix}


%files
%{_bindir}/jpeg-archive
%{_bindir}/jpeg-compare
%{_bindir}/jpeg-hash
%{_bindir}/jpeg-recompress


%changelog
* Sat Apr 11 2020 Tomasz Gąsior
- Workaround incompatibility with GCC 10
* Sun Nov 17 2019 Tomasz Gąsior
- Initial