# This specfile steals some files from Fedora RPM package:
# https://src.fedoraproject.org/rpms/firefox/
%define fedora_commit b0f1086cdfa2d1645864f0094661c425f677d795
%define mozilla_commit e8fe8b0af1a7a0c64d28b4e08a9c5509d916759f

Name:           firefox-developer-edition-bin
Version:        3
Release:        1%{?dist}
Summary:        Firefox Developer Edition binary launcher

License:        MPLv1.1 or GPLv2+ or LGPLv2+
URL:            https://www.mozilla.org/firefox/
Source0:        firefox-developer-edition
Source1:        copr-mushrooms-default-prefs.js
Source2:        https://hg.mozilla.org/mozilla-central/raw-file/%{mozilla_commit}/browser/branding/aurora/default256.png#/firefox-developer-edition.png
Source3:        https://src.fedoraproject.org/rpms/firefox/raw/%{fedora_commit}/f/firefox-symbolic.svg#/firefox-developer-edition-symbolic.svg
Source4:        https://src.fedoraproject.org/rpms/firefox/raw/%{fedora_commit}/f/firefox.desktop#/firefox-developer-edition.desktop

Requires:       /usr/bin/bash
Requires:       /usr/bin/curl
Requires:       /usr/bin/tar
Requires:       /usr/bin/dirname
Requires:       /usr/bin/sed
Requires:       /usr/bin/ln
Requires:       /usr/bin/systemd-path
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
sed -i %{SOURCE4} \
    -e 's#firefox#firefox-developer-edition#g' \
    -e 's#Firefox#Firefox Developer Edition#g'


%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_datadir}/{applications,icons,firefox-developer-edition}

cp %{SOURCE0} %{buildroot}%{_bindir}/
chmod +x %{buildroot}%{_bindir}/firefox-developer-edition

cp %{SOURCE1} %{buildroot}%{_datadir}/firefox-developer-edition/
cp {%{SOURCE2},%{SOURCE3}} %{buildroot}%{_datadir}/icons/
cp %{SOURCE4} %{buildroot}%{_datadir}/applications/


%files
%{_bindir}/firefox-developer-edition
%{_datadir}/applications/firefox-developer-edition.desktop
%{_datadir}/icons/firefox-developer-edition*
%{_datadir}/firefox-developer-edition/copr-mushrooms-default-prefs.js


%changelog
* Sun Jul 26 2020 Tomasz Gąsior
- Update desktop icon from Fedora: add "Open the Profile Manager" item.
- Add downstream default prefs for new installations: make langpacks
  from addons.mozilla.org working, make updates more visible.

* Sun Apr 26 2020 Tomasz Gąsior
- Enforce X11, remove Wayland workaround for
  https://bugzilla.mozilla.org/show_bug.cgi?id=1530052

* Wed Apr 22 2020 Tomasz Gąsior
- Initial