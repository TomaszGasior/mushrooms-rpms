# This specfile steals some files from Fedora RPM package:
# https://src.fedoraproject.org/rpms/firefox/
%define fedora_commit 461eee52cd461effb0009d6986d4740cca3a9006
%define mozilla_commit e8fe8b0af1a7a0c64d28b4e08a9c5509d916759f

Name:           firefox-developer-edition-bin
Version:        2
Release:        1%{?dist}
Summary:        Firefox Developer Edition binary launcher

License:        MPLv1.1 or GPLv2+ or LGPLv2+
URL:            https://www.mozilla.org/firefox/
Source0:        firefox-developer-edition
Source1:        https://hg.mozilla.org/mozilla-central/raw-file/%{mozilla_commit}/browser/branding/aurora/default256.png#/firefox-developer-edition.png
Source2:        https://src.fedoraproject.org/rpms/firefox/raw/%{fedora_commit}/f/firefox-symbolic.svg#/firefox-developer-edition-symbolic.svg
Source3:        https://src.fedoraproject.org/rpms/firefox/raw/%{fedora_commit}/f/firefox.desktop#/firefox-developer-edition.desktop

Requires:       /usr/bin/bash
Requires:       /usr/bin/curl
Requires:       /usr/bin/tar
Requires:       /usr/bin/dirname
Requires:       /usr/bin/sed
BuildRequires:  /usr/bin/sed
BuildArch:      x86_64


%description
This package provides easy to use launcher for official binary
distribution of Firefox Developer Edition with icon in applications
list. When started first time, it downloads the browser to your
home directory.

Please keep updates feature enabled in your Firefox instance to
receive new versions of this software.


%prep
sed -i %{SOURCE3} \
    -e 's#firefox#firefox-developer-edition#g' \
    -e 's#Firefox#Firefox Developer Edition#g'


%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_datadir}/{applications,icons}

cp %{SOURCE0} %{buildroot}%{_bindir}/
chmod +x %{buildroot}%{_bindir}/firefox-developer-edition

cp {%{SOURCE1},%{SOURCE2}} %{buildroot}%{_datadir}/icons/
cp %{SOURCE3} %{buildroot}%{_datadir}/applications/


%files
%{_bindir}/firefox-developer-edition
%{_datadir}/applications/firefox-developer-edition.desktop
%{_datadir}/icons/firefox-developer-edition*


%changelog
* Sun Apr 26 2020 Tomasz Gąsior
- Enforce X11, remove Wayland workaround for
  https://bugzilla.mozilla.org/show_bug.cgi?id=1530052
* Wed Apr 22 2020 Tomasz Gąsior
- Initial