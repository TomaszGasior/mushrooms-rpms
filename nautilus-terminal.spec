%{?python_disable_dependency_generator}

Name:           nautilus-terminal
Version:        4.0.6
Release:        2%{?dist}
Summary:        A terminal embedded in Nautilus, the GNOME's file browser

License:        GPL-3.0
URL:            https://github.com/flozz/%{name}
Source0:        https://github.com/flozz/nautilus-terminal/archive/refs/tags/v%{version}.zip

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3
Requires:       python3-psutil
Requires:       nautilus-python
BuildArch:      noarch
Recommends:     dconf-editor


%description
Nautilus Terminal is a terminal embedded into Nautilus, the GNOME's
file browser. It is always opened in the current folder, and follows
the navigation (the cd command is automatically executed when you
navigate to another folder).

Press F4 to open the terminal. Use dconf-editor to edit its settings.


%prep
%autosetup -p 0


%build
# https://github.com/flozz/nautilus-terminal/issues/63
rm nautilus_terminal/not_packaged.py

%py3_build


%install
%py3_install


%files
%{_datadir}/glib-2.0/schemas/org.flozz.nautilus-terminal.gschema.xml
%{_datadir}/nautilus-python/extensions/nautilus_terminal_extension.py
%{python3_sitelib}/nautilus_terminal
%{python3_sitelib}/nautilus_terminal*.egg-info
%{_bindir}/nautilus-terminal


%changelog
* Sun May 23 2021 Tomasz Gąsior
- New `nautilus-terminal` command for debugging

* Tue May 18 2021 Tomasz Gąsior
- Upstream update
- Downstream patch for terminal disabled by default removed
  https://github.com/flozz/nautilus-terminal/issues/37

* Sun Nov 22 2020 Tomasz Gąsior
- Upstream update
- New options: terminal toggle shortcut, terminal background and text color

* Sat Feb 8 2020 Tomasz Gąsior
- Disable terminal by default (downstream patch)

* Sat Feb 8 2020 Tomasz Gąsior
- Upstream update
- Added terminal bottom view option

* Sun Nov 17 2019 Tomasz Gąsior
- Initial
