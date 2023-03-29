%global git_commit_hash c993fb1da1bba5c2cd2860c1aa6c3916b4de77e4

Name:           i8kutils
Version:        1.43
Release:        1.%(echo %git_commit_hash | cut -c 1-7)%{?dist}
Summary:        Fan control for some Dell laptops

License:        GPL-3.0
URL:            https://github.com/vitorafsr/%{name}
Source0:        https://github.com/vitorafsr/%{name}/archive/%{git_commit_hash}.tar.gz
Patch0:         acpi-command.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd-rpm-macros
Requires:       tcl
Requires:       acpi
Requires:       systemd


%description
i8kutils package contains user-space programs for controlling the fans on some
Dell laptops. i8kutils is entirely built upon the dell-smm-hwmon kernel module.

These data contains the states and the system temperature along with others 
infos:
* BIOS version
* Dell service tag (later known as 'serial number')
* CPU temperature
* fan status
* fan rotation speed (only on some models)
* ac power status
* volume buttons status (not the multimedia buttons)

The i8kutils package includes the following utilities:
* i8kctl - command-line interface to the kernel module
* i8kmon - temperature monitor with fan control capability
* i8kfan - utility to set state (speed) of fans

All Dell laptop has the feature of controlling the temperature in the BIOS, but
to some models this feature does not work properly. i8kmon does essentially the same
job as the BIOS is supposed to do.


%prep
%autosetup -n %{name}-%{git_commit_hash} -p 0


%build
%make_build


%install
install -D -t %{buildroot}%{_bindir}/ -m 755 i8kctl i8kmon i8kfan
install -D -t %{buildroot}%{_sysconfdir} i8kmon.conf
install -D -t %{buildroot}%{_unitdir}/ debian/i8kmon.service
install -D -t %{buildroot}%{_mandir}/man1/ i8kctl.1 i8kmon.1
install -D -t %{buildroot}%{_modprobedir}/ dell-smm-hwmon.conf


%files
%config(noreplace) %{_sysconfdir}/i8kmon.conf
%{_bindir}/i8k*
%{_unitdir}/i8kmon.service
%{_mandir}/man1/i8k*
%{_modprobedir}/dell-smm-hwmon.conf


%changelog
* Wed Mar 29 2023 Tomasz Gąsior
- Initial
