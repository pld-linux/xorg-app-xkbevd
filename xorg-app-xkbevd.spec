Summary:	xkbevd - XKB event daemon
Summary(pl.UTF-8):	xkbevd - demon zdarzeń XKB
Name:		xorg-app-xkbevd
Version:	1.1.6
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xkbevd-%{version}.tar.xz
# Source0-md5:	543c0535367ca30e0b0dbcfa90fefdf9
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xkbevd event daemon listens for specified XKB events and executes
requested commands if they occur. The configuration file consists of a
list of event specification/action pairs and/or variable definitions.

%description -l pl.UTF-8
Demon zdarzeń xkbevd nasłuchuje na określone zdarzenia XKB i w
przypadku ich wystąpienia wywołuje żądane polecenia. Plik
konfiguracyjny składa się z par określeń zdarzeń i akcji i/lub
definicji zmiennych.

%prep
%setup -q -n xkbevd-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xkbevd
%{_mandir}/man1/xkbevd.1*
