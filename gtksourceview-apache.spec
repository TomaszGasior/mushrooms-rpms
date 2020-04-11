Name:           gtksourceview-apache
Version:        1
Release:        1%{?dist}
Summary:        GtkSourceView language definition for Apache configuration files.

License:        LGPL
URL:            https://bugzilla.gnome.org/show_bug.cgi?id=612368
Source0:        https://bug612368.bugzilla-attachments.gnome.org/attachment.cgi?id=195525#/apache.lang

Requires:       gtksourceview3
Requires:       gtksourceview4
BuildArch:      noarch


%description
Language definition for Apache configuration files.
Works with text editors based on GtkSourceView widget like gedit.


%install
mkdir -p %{buildroot}/%{_datadir}/gtksourceview-{3.0,4}/language-specs
cp %{SOURCE0} %{buildroot}/%{_datadir}/gtksourceview-3.0/language-specs
cp %{SOURCE0} %{buildroot}/%{_datadir}/gtksourceview-4/language-specs


%files
%{_datadir}/gtksourceview-3.0/language-specs/apache.lang
%{_datadir}/gtksourceview-4/language-specs/apache.lang


%changelog
* Sat Apr 11 2020 Tomasz Gąsior
- Initial