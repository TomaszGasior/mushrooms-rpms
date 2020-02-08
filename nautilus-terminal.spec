%{?python_disable_dependency_generator}

Name:           nautilus-terminal
Version:        3.2.3
Release:        1%{?dist}
Summary:        A terminal embedded in Nautilus, the GNOME's file browser

License:        GPL-3.0
URL:            https://github.com/flozz/%{name}
Source0:        https://github.com/flozz/%{name}/archive/v%{version}.zip

BuildRequires:  python3-devel
Requires:       python3
Requires:       python3-psutil
Requires:       nautilus-python
BuildArch:      noarch


%description
Nautilus Terminal is a terminal embedded into Nautilus, the GNOME's
file browser. It is always opened in the current folder, and follows
the navigation (the cd command is automatically executed when you
navigate to another folder).


%prep
%setup


%build
python3 setup.py build


%install
python3 setup.py install --optimize=1 --root="%{buildroot}"


%files
/%{_datadir}/glib-2.0/schemas/org.flozz.nautilus-terminal.gschema.xml
/%{_datadir}/nautilus-python/extensions/nautilus_terminal_extension.py
/%{python3_sitelib}/nautilus_terminal
/%{python3_sitelib}/nautilus_terminal*.egg-info


%changelog
* Sun Nov 17 2019 Tomasz Gąsior
- Initial