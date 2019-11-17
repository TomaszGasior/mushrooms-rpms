%global debug_package %{nil}
%global install_path /opt/mozjpeg

Name:           mozjpeg
Version:        3.3.1
Release:        1%{?dist}
Summary:        Mozilla JPEG Encoder Project — improved JPEG encoder

License:        BSD
URL:            https://github.com/mozilla/%{name}
Source0:        https://github.com/mozilla/%{name}/archive/v%{version}.zip

BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  nasm
BuildArch:      x86_64


%description
MozJPEG reduces file sizes of JPEG images while retaining quality and
compatibility with the vast majority of the world's deployed decoders.

MozJPEG is based on libjpeg-turbo. MozJPEG makes tradeoffs that are
intended to benefit Web use cases and focuses solely on improving
encoding, so it's best used as part of a Web encoding workflow.

This package does not replace libjpeg-turbo. MozJPEG is installed
to /opt directory.


%prep
%setup


%build
autoreconf -fiv
%set_build_flags
./configure --prefix=%{install_path}
make %{?_smp_mflags}


%install
%make_install


%files
%dir %{install_path}
%{install_path}/*


%changelog
* Sun Nov 17 2019 Tomasz Gąsior
- Initial