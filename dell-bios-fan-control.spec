%global debug_package %{nil}

%global git_commit_hash 27006106595bccd6c309da4d1499f93d38903f9a

Name:           dell-bios-fan-control
Version:        1.0
Release:        1.%(echo %git_commit_hash | cut -c 1-7)%{?dist}
Summary:        A user space utility to set control of fans by bios on Dell laptops

License:        GPL-2.0
URL:            https://github.com/TomFreudenberg/%{name}
Source0:        https://github.com/TomFreudenberg/%{name}/archive/%{git_commit_hash}.tar.gz
Source1:        %{name}.conf

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  systemd-rpm-macros
Recommends:     i8kutils


%description
A user space utility to set control of fans by bios on Dell 9560 Laptops.
Allows to control the fans by bios or i8kctl utils.

To enable SMBIOS control: dell-bios-fan-control 1
To disable SMBIOS control: dell-bios-fan-control 0

After disabling SMBIOS control of fans you can set fan speed by i8kctl.

Caveats
* The BIOS of some newer Dell laptops (9560, ...) will override the speed
  you set unless you disable the BIOS control.
* This tool allows to enable or disable bios control of fans to use i8kmon
  instead.

All credits belong to: https://github.com/clopez/dellfan.

This package provides drop-in file for i8kmon service so dell-bios-fan-control
will be executed before and after i8kmon daemon.


%prep
%autosetup -n %{name}-%{git_commit_hash}


%build
%make_build


%install
install -D -t %{buildroot}%{_bindir}/ -m 755 %{name}
install -D -t %{buildroot}%{_unitdir}/i8kmon.service.d/ -m 644 %{SOURCE1}
install -D -t %{buildroot}%{_unitdir}/i8kmon@.service.d/ -m 644 %{SOURCE1}


%files
%{_bindir}/%{name}
%{_unitdir}/i8kmon.service.d/%{name}.conf
%{_unitdir}/i8kmon@.service.d/%{name}.conf


%changelog
* Sun Apr 02 2023 Tomasz Gąsior
- Initial
