Summary:	Process monitoring utilities
Summary(de):	Dienstprogramm zur Prozeßüberwachung
Summary(fr):	Utilitaires de surveillance des processus.
Summary(pl):	Narzêdzia do monitorowania procesów
Summary(tr):	Süreç izleme araçlarý
Name:		procps
Version:	2.0.2
Release:	3
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	ftp://tsx-11.mit.edu/pub/linux/sources/usr.bin/%{name}-%{version}.tar.gz
Source1:	free.1.pl
Source2:	uptime.1.pl
Patch0:		procps-opt.patch
Patch1:		procps-install.patch
Patch2:		procps-w.patch
BuildRequires:	ncurses-devel
URL:		http://www.cs.uml.edu/~acahalan/linux/
Obsoletes:	procps-X11
Buildroot:	/tmp/%{name}-%{version}-root

%description
A package of utilities which report on the state of the system,
including the states of running processes, amount of memory available,
and currently-logged-in users.

%description -l de
Ein Paket mit Utilities, die den Status des Systems melden, 
einschließlich des Status laufender Prozesse, der Menge des 
verfügbaren Speicherplatzes und der momentan angemeldeten Benutzer.

%description -l fr
Paquetage d'utilitaires donnant des informations sur l'état du système,
dont les états des processus en cours, le total de mémoire disponible,
et les utilisateurs loggés.

%description -l pl
Pakiet zawiera podstawowe narzêdzia do monitorowania pracy systemu. Dziêki
tym programom bêdziesz móg³ na bie¿±co kontralowaæ jakie procesy s± w danej
chwili uruchomione, ilo¶æ wolnej pamiêci, kto jest w danej chwili zalogowany,
jakie jest aktualne obci±¿enie systemu itp.

%description -l tr
Sistemin durumunu rapor eden araçlar paketidir. Koþan süreçlerin durumunu,
kullanýlabilir bellek miktarýný, ve o an için sisteme girmiþ kullanýcýlarý
bildirir.

%prep
%setup -q 
%patch0 -p1 
%patch1 -p1 
%patch2 -p1 

%build
PATH=/usr/X11R6/bin:$PATH

make OPT="$RPM_OPT_FLAGS -pipe" 

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,bin,lib} \
	$RPM_BUILD_ROOT/usr/{bin,X11R6/bin,share}

install -d $RPM_BUILD_ROOT%{_mandir}/{man{1,8},pl/man1}

make install \
	DESTDIR=$RPM_BUILD_ROOT BINGRP=`id -g` \
	MAN1DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	MAN8DIR=$RPM_BUILD_ROOT%{_mandir}/man8

install top.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/top
install XConsole $RPM_BUILD_ROOT/usr/X11R6/bin

rm -f  $RPM_BUILD_ROOT%{_bindir}/snice
ln -sf skill $RPM_BUILD_ROOT%{_bindir}/snice
rm -f  $RPM_BUILD_ROOT/bin/kill

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{snice,kill,oldps}.1
rm -f $RPM_BUILD_ROOT%{_bindir}/oldps

echo .so skill.1 > $RPM_BUILD_ROOT%{_mandir}/man1/snice.1
install ps/ps.1 $RPM_BUILD_ROOT%{_mandir}/man1

strip --strip-unneeded $RPM_BUILD_ROOT/lib/*.so.*.*

install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1/free.1
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man1/uptime.1

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/{man*/*,pl/man*/*} NEWS BUGS 

%post 
/sbin/ldconfig
if [ -f /proc/uptime ] ; then
	/bin/ps </dev/null >/dev/null 2>&1
fi
rm -f /etc/psdevtab /etc/psdatabase

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {NEWS,BUGS}.gz

%lang(pl) %{_mandir}/pl/man*/*
%{_mandir}/man*/*

/etc/X11/wmconfig/top

%attr(755,root,root) /lib/libproc.so.*
%attr(755,root,root) /bin/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) /usr/X11R6/bin/XConsole
