Name:           brlaser
Version:        4.1
Release:        1%{?dist}
Summary:        Printer for shitty fucked up brother printer

License:        GPL-2.0
URL:            https://github.com/drahnr/%{name}
#Source0:        https://github.com/drahnr/%{name}/releases/tag/v%{version}.tar.gz
Source0:        brlaser.tar.xz


BuildRequires:  cups-devel
Requires:       cups

%description
A actually working printer driver for Brother DCP-7065DN

%prep -n brlaser
cd brlaser-%{version}
%autosetup -n brlaser -D

%build -n brlaser
./autogen.sh
%configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%license COPYING
%doc README.md
# TODO no idea which macro to use for that one
/usr/lib/cups/filter/rastertobrlaser
%{_datadir}/cups/drv/brlaser.drv

%changelog
* Thu Aug  3 2017 Bernhard Schuster <bernhard@ahoi.io>
- First release as rpm
