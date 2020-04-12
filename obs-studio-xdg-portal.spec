%define commit fc5876a6f509fa9e492b0f61a915993058d8abd0

Name:           obs-studio-xdg-portal
Version:        0.0.1
Release:        1%{?dist}
Summary:        OBS Studio plugin for XDG screencasting portal

License:        GPLv3
URL:            https://gitlab.gnome.org/feaneron/obs-xdg-portal
Source0:        https://gitlab.gnome.org/feaneron/obs-xdg-portal/-/archive/%{commit}/obs-xdg-portal-%{commit}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  obs-studio-devel
BuildRequires:  glib2-devel
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel


%description
OBS Studio plugin using the Desktop portal for Wayland & X11
screencasting.


%prep
%autosetup -n obs-xdg-portal-%{commit}


%build
%meson
%meson_build


%install
mkdir -p %{buildroot}/%{_libdir}/obs-plugins
cp %{_vpath_builddir}/obs-xdg-portal.so %{buildroot}/%{_libdir}/obs-plugins


%files
%{_libdir}/obs-plugins/obs-xdg-portal.so


%changelog
* Sun Apr 12 2020 Tomasz Gąsior
- Initial