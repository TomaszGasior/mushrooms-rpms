Name:           ink
Version:        0.5.3
Release:        1%{?dist}
Summary:        Ink is a program to display the ink level of printers

License:        GPL
URL:            http://ink.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

Requires:       libinklevel
BuildRequires:  libinklevel
BuildRequires:  autoconf
BuildRequires:  gcc


%description
Ink is a command line tool for checking the ink level of your locally connected
printer. Currently printers of the following brands are supported: HP, Epson and 
Canon. Canon BJNP network printers are supported too. It makes use of libinklevel. 

A detailed list of supported printers is available:
http://libinklevel.sourceforge.net/#supported.


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%files
%{_bindir}/ink
%{_mandir}/man1/ink*


%changelog
* Sun Feb 09 2020 Tomasz Gąsior
- Initial