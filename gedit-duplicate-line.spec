%global debug_package %{nil}

%define commit 77fad2a4cd20eaecee165a0f651486c23a4e2b29

Name:           gedit-duplicate-line
Version:        1
Release:        1%{?dist}
Summary:        Gedit plugin to duplicate lines

License:        unlicensed
URL:            https://github.com/hannenz/duplicate
Source0:        https://github.com/hannenz/duplicate/archive/%{commit}.zip

BuildRequires:  python3-devel
Requires:       gedit%{?_isa}
Requires:       libpeas-loader-python3%{?_isa}


%description
This plugin for the gedit text editor allows to duplicate lines,
just like in Geany, where you can press Ctrl+D to duplicate either
the current line or the current selection.

In gedit use Ctrl+Shift+D to duplicate current line or selection.


%prep
%autosetup -n duplicate-%{commit}


%install
mkdir -p %{buildroot}%{_libdir}/gedit/plugins
cp duplicateline.plugin %{buildroot}%{_libdir}/gedit/plugins
cp duplicateline.py %{buildroot}%{_libdir}/gedit/plugins
%py_byte_compile %{__python3} %{buildroot}%{_libdir}/gedit/plugins


%files
%{_libdir}/gedit/plugins/duplicateline.plugin
%{_libdir}/gedit/plugins/duplicateline.py
%{_libdir}/gedit/plugins/__pycache__/duplicateline*


%changelog
* Sat Apr 11 2020 Tomasz Gąsior
- Initial