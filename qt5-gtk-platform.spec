%global debug_package %{nil}

%define commit 1149f4f77523f650e542f83e9a1985e0b9f00a05

Name:           qt5-gtk-platform
Version:        0.2.4
Release:        1.%(echo %commit | cut -c 1-8)%{?dist}
Summary:        Run Qt applications using gtk+ as a windowing system

License:        LGPL v3 or GPL 2+
URL:            https://github.com/CrimsonAS/gtkplatform
Source0:        https://github.com/CrimsonAS/gtkplatform/archive/%{commit}.zip

Suggests:       adwaita-qt5
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtbase-static
BuildRequires:  gtk3-devel
BuildRequires:  libnotify-devel


%description
gtkplatform is a Qt Platform Abstraction plugin providing
Qt applications with the capability to use gtk+ as a host toolkit,
primarily intended for use on Linux desktops.

That is: it lets Qt applications render with native gtk+ menus, and use
gtk+ for input (mouse, keyboard, touch), and getting window content
on screen, the same as it uses e.g. cocoa on macOS for instance.

This platform is considered unstable and not enabled by default.
To enable this plugin set `QT_QPA_PLATFORM=gtk` environment variable
or use `-platform gtk` command line switch.


%prep
%autosetup -n gtkplatform-%{commit}
mkdir .git


%build
%qmake_qt5
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}


%files
%{_qt5_plugindir}/platforms/libqgtk.so
%{_qt5_includedir}/QtGtkExtras/*
%{_qt5_libdir}/libQt5GtkExtras.*
%{_qt5_libdir}/pkgconfig/Qt5GtkExtras.pc
%{_qt5_archdatadir}/mkspecs/modules/*
%{_qt5_examplesdir}/gtkextras/*
%{_libdir}/cmake/Qt5Gui/*


%changelog
* Sun Apr 19 2020 Tomasz Gąsior
- Initial