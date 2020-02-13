# This spec file is based on:
# * https://src.fedoraproject.org/rpms/blobby/blob/f30/f/blobby.spec
# * https://git.archlinux.org/svntogit/community.git/tree/trunk/PKGBUILD?h=packages/blobby2
# * https://en.wikipedia.org/wiki/Blobby_Volley

Name:           blobby
Version:        1.0
Release:        1%{?dist}
Summary:        The head-to-head multiplayer ball game

License:        GPLv2+
URL:            https://github.com/danielknobe/blobbyvolley2
Source0:        https://downloads.sourceforge.net/%{name}/%{name}2-linux-%{version}.tar.gz
Source1:        %{name}.desktop
Patch0:         %{url}/commit/c5329cbc50.patch
Patch1:         %{url}/commit/b069d193b3.patch
Patch2:         compile-flags.patch
Patch3:         global-data-dir.patch
Patch4:         global-data-dir-server.patch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  ImageMagick
BuildRequires:  mesa-libGL-devel
BuildRequires:  physfs-devel
BuildRequires:  SDL2-devel


%description
Blobby Volley is a free and open-source sports computer game series
in which two blobbed shaped entities play volleyball against each other.
There are multiplayer and also single player game modes.


%prep
%autosetup -N
%autopatch -M1 -p1
%autopatch -m2 -p0


%build
%cmake .
make %{?_smp_mflags}


%install
%make_install PREFIX=%{buildroot}/%{_prefix}/%{name}

convert -size 48x48 -transparent black data/Icon.bmp %{name}.png
install -p -m 644 -D %{name}.png %{buildroot}/%{_datadir}/icons/%{name}.png
desktop-file-install %{SOURCE1}


%files
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/%{name}.png


%changelog
* Mon Jan 13 2020 Tomasz Gąsior
- Initial