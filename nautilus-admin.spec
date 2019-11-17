%global git_commit_hash 89dd83d438da424153a7556ab67c7c610dffc2d9

Name:           nautilus-admin
Version:        1.1.9
Release:        1%{?dist}
Summary:        Extension for Nautilus to do administrative operations

License:        GPL-3.0
URL:            https://github.com/brunonova/%{name}
Source0:        https://github.com/brunonova/%{name}/archive/%{git_commit_hash}.zip

BuildRequires:  cmake
BuildRequires:  gettext
Requires:       python3
Requires:       nautilus-python
Requires:       gedit
BuildArch:      noarch


%description
Nautilus Admin is a simple Python extension for the Nautilus file
manager that adds some administrative actions to the right-click menu:
* Open as Administrator: opens a folder in a new Nautilus window running
with administrator (root) privileges.
* Edit as Administrator: opens a file in a Gedit window running with
administrator (root) privileges.

Please remember to restart Nautilus after installation.
You can use `nautilus -q` command.


%prep
%setup -n %{name}-%{git_commit_hash}


%build
mkdir build
cd build
%cmake ..
make


%install
cd build
%make_install
cd ..
%find_lang %{name}


%files -f %{name}.lang
/%{_datadir}/nautilus-python/extensions/%{name}.py


%changelog
* Mon Nov 18 2019 Tomasz Gąsior
- Initial