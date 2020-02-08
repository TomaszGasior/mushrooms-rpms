# this spec file is based on:
# * https://src.fedoraproject.org/rpms/woff2
# * https://github.com/journeyman88/copr-repositories/blob/master/font-tools/woff2.spec

%global orig_name woff2

Name:           woff2-tools
Version:        1.0.2
Release:        1%{?dist}
Summary:        Tools for Web Open Font Format 2.0

License:        MIT
URL:            https://github.com/google/woff2
Source0:        https://github.com/google/woff2/archive/v%{version}/%{orig_name}-%{version}.tar.gz

Requires:       %{orig_name}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  brotli-devel >= 1.0


%description
Tools for compressing TTF files to WOFF2 format, decompressing WOFF2
files back to TTF files and dumping WOFF2 file information.


%prep
%autosetup -n %{orig_name}-%{version}


%build
%cmake . \
    -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
    -DCMAKE_INSTALL_LIBDIR="%{_libdir}"
%make_build


%install
mkdir -p  %{buildroot}%{_bindir}
install -m 755 woff2_decompress %{buildroot}%{_bindir}
install -m 755 woff2_compress %{buildroot}%{_bindir}
install -m 755 woff2_info %{buildroot}%{_bindir}


%files
%attr(755, root, root) %{_bindir}/woff2_compress
%attr(755, root, root) %{_bindir}/woff2_decompress
%attr(755, root, root) %{_bindir}/woff2_info


%changelog
* Sat Feb 8 2020 Tomasz Gąsior
- Initial
