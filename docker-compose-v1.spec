# Based on "docker-compose" spec from Fedora repository:
# https://src.fedoraproject.org/rpms/docker-compose/tree/dc43b89a26e224fb84004a6981d9a2a383891496

Name:           docker-compose-v1
Version:        1.29.2
Release:        1%{?dist}
Summary:        Multi-container orchestration for Docker (legacy v1)
License:        Apache-2.0
URL:            https://github.com/docker/compose
Source0:        https://github.com/docker/compose/archive/%{version}.zip
Patch0:         python-3-13-pipes-shlex.patch
Patch1:         docker-sdk-library-v7-compat.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3
Recommends:     bash-completion
Conflicts:      docker-compose-switch
BuildArch:      noarch


%description
Compose is a tool for defining and running multi-container Docker
applications. With Compose, you use a Compose file to configure your
application's services. Then, using a single command, you create and
start all the services from your configuration.

This package provides legacy and unmaintained, Python-based
docker-compose v1 (with dash in the name).


%prep
%autosetup -n compose-%{version} -p 0
sed -e 's/, < [0-9.]\+//' -i setup.py


%build
%py3_build


%install
%py3_install

install -D -p -m 644 contrib/completion/bash/docker-compose \
   %{buildroot}%{_datadir}/bash-completion/completions/docker-compose


%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/docker-compose
%{python3_sitelib}/compose
%{python3_sitelib}/docker_compose*.egg-info
%{_datadir}/bash-completion/completions/docker-compose


%changelog
* Sat Jan 04 2025 Tomasz Gąsior
- Initial
