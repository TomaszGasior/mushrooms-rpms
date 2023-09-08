%{!?tcl_version: %global tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitelib: %global tcl_sitelib %{_datadir}/tcl%(echo %tcl_version | cut -d '.' -f 1)/%{tcl_version}}

%define debug_package %{nil}

Name:           i8kutils
Version:        1.52
Release:        1%{?dist}
Summary:        Fan control for some Dell laptops

License:        GPL-3.0
URL:            https://github.com/Wer-Wolf/%{name}
Source0:        https://github.com/Wer-Wolf/%{name}/archive/v%{version}.zip

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  systemd
BuildRequires:  tcl
Requires:       tcl
Requires:       tcllib
Requires:       acpi
Requires:       systemd


%description
i8kutils is a collection of utilities for controlling the fans on some Dell
laptops. The utilities are entirely built upon the dell-smm-hwmon kernel module.

The i8kutils package includes the following utilities:
* i8kctl, a command-line utility for interfacing with the kernel module.
* i8kmon, a temperature monitor with fan control capability.


%prep
%autosetup


%build
%meson -Dsysvinit_support=disabled -Dmoduledir=%{tcl_sitelib}
%meson_build


%install
%meson_install


%files
%config(noreplace) %{_sysconfdir}/i8kmon.conf
%{_bindir}/i8k*
%{_unitdir}/i8kmon.service
%{_mandir}/man1/i8k*
%{_udevrulesdir}/50-i8kmon.rules
%{tcl_sitelib}/i8k/hwmon-1.0.tm
%{tcl_sitelib}/i8k/thermal-1.0.tm


%changelog
* Sat Jun 17 2023 Tomasz Gąsior
- Upstream update: easier to disable systemd service

* Sat Jun 03 2023 Tomasz Gąsior
- Upstream update: better security, ondemand option from command line

* Thu Mar 30 2023 Tomasz Gąsior
- Dead upstream from vitorafsr replaced with active fork from Wer-Wolf

* Wed Mar 29 2023 Tomasz Gąsior
- Initial
