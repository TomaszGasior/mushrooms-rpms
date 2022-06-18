%undefine _hardened_build
%global git_commit_hash 7390849d125ad7979d7c6e23e4ef7c64060ca6bf

Name:           hardinfo
Version:        0.6.alpha
Release:        3.%(echo %git_commit_hash | cut -c 1-7)%{?dist}
Summary:        System profiler and benchmark tool for Linux systems

License:        GPL-2.0
URL:            https://github.com/lpereira/%{name}
Source0:        https://github.com/lpereira/%{name}/archive/%{git_commit_hash}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  json-glib-devel
BuildRequires:  libsoup-devel
BuildRequires:  lm_sensors-devel
Recommends:     /usr/bin/glxinfo
Recommends:     /usr/bin/hddtemp
Recommends:     /usr/bin/sysbench
Recommends:     /usr/bin/xrandr
Recommends:     /usr/sbin/dmidecode


%description
HardInfo is a system profiler and benchmark for Linux systems. It is able
to obtain information from both hardware and basic software, and organize it
in a simple to use GUI.

Features include: report generation (in either HTML or plain text),
benchmark result synchronization, ability to explore the information
on remote computers.

For some features the application must be ran as root user!


%prep
%autosetup -n %{name}-%{git_commit_hash}


%build
%cmake -DHARDINFO_GTK3=1
%cmake_build


%install
%cmake_install
%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.png
%{_mandir}/man1/%{name}*


%changelog
* Sat Jun 18 2022 Tomasz Gąsior
- Upstream update from master branch

* Sun Feb 20 2022 Tomasz Gąsior
- Upstream update from master branch
- sysbench added to recommended dependencies

* Mon Nov 01 2021 Tomasz Gąsior
- Initial
