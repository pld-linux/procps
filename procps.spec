Summary:	Utilities for monitoring your system and processes on your system
Summary(de):	Utilities zum Ueberwachen Ihres Systems und der Prozesse
Summary(fr):	Utilitaires de surveillance des processus.
Summary(pl):	Narzêdzia do monitorowania procesów
Summary(tr):	Süreç izleme araçlarý
Name:		procps
Version:	2.0.6
Release:	3
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	ftp://metalab.unc.edu/pub/Linux/system/status/ps/%{name}-%{version}.tar.gz
Source1:	free.1.pl
Source2:	uptime.1.pl
Source3:	ps.1.pl
Source4:	top.desktop
Patch0:		procps-opt.patch
Patch1:		procps-install.patch
Patch2:		procps-w2.patch
Patch3:		procps-man5.patch
Patch4:		procps-SMP.patch
BuildRequires:	ncurses-devel >= 5.0
URL:		http://www.cs.uml.edu/~acahalan/linux/
Obsoletes:	procps-X11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The procps package contains a set of system utilities which provide system
information. Procps includes ps, free, skill, snice, tload, top, uptime,
vmstat, w, and watch. The ps command displays a snapshot of running
processes. The top command provides a repetitive update of the statuses of
running processes. The free command displays the amounts of free and used
memory on your system. The skill command sends a terminate command (or
another specified signal) to a specified set of processes. The snice command
is used to change the scheduling priority of specified processes. The tload
command prints a graph of the current system load average to a specified
tty. The uptime command displays the current time, how long the system has
been running, how many users are logged on and system load averages for the
past one, five and fifteen minutes. The w command displays a list of the
users who are currently logged on and what they're running.  The watch
program watches a running program. The vmstat command displays virtual
memory statistics about processes, memory, paging, block I/O, traps and CPU
activity.

%description -l de
Das procps-Paket enthält System-Utilities, die Systeminformationen anzeigen.
Procps enthält ps, free, skill, snice, tload, top, uptime, vmstat, w und
watch. ps zeigt an, welche Prozesse gerade laufen. Top zeigt in regelmäßigen
Abständen eine Prozessliste an. Free zeigt an, wieviel Speicher frei ist,
und wieviel Speicher benutzt wird. Skill schickt den Terminierungsbefehl
(oder ein anderes angegebenes Signal) an angegebene Prozesse. Snice ändert
die Priorität von angegebenen Prozessen. tload zeigt einen Graphen der
aktuellen Systemauslastung an. Uptime zeigt an, wie lange das System am
laufen ist, wieviele User eingeloggt sind, und die Auslastungswerte der
letzten Minute, der letzten 5 Minuten, und 15 Minuten. Der w-Befehl zeigt
eine Liste der User an, die gerade eingeloggt sind, und welches Programm sie
benutzen. Vmstat zeigt Statistiken über den virtuellen Speicher, Prozesse,
Paging, Block I/O, Traps, und CPU-Aktivität.

%description -l fr
Paquetage d'utilitaires donnant des informations sur l'état du système,
dont les états des processus en cours, le total de mémoire disponible,
et les utilisateurs loggés.

%description -l pl
Pakiet zawiera podstawowe narzêdzia do monitorowania pracy systemu. Dziêki
tym programom bêdziesz móg³ na bie¿±co kontrolowaæ jakie procesy s± w danej
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
%patch3 -p1 
#%patch4 -p1 

%build
PATH=/usr/X11R6/bin:$PATH

#make OPT="$RPM_OPT_FLAGS -pipe -D__SMP__" 
make OPT="$RPM_OPT_FLAGS -pipe"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{bin,sbin,lib,usr/X11R6/bin} \
	$RPM_BUILD_ROOT{%{_bindir},%{_datadir},%{_mandir}/{man{1,5,8},pl/man1}} \
	$RPM_BUILD_ROOT%{_applnkdir}/Administration

make install \
	DESTDIR=$RPM_BUILD_ROOT BINGRP=`id -g` \
	MAN1DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	MAN5DIR=$RPM_BUILD_ROOT%{_mandir}/man5 \
	MAN8DIR=$RPM_BUILD_ROOT%{_mandir}/man8

install %{SOURCE4} $RPM_BUILD_ROOT%{_applnkdir}/Administration
install XConsole   $RPM_BUILD_ROOT/usr/X11R6/bin

rm -f  $RPM_BUILD_ROOT%{_bindir}/snice
ln -sf skill $RPM_BUILD_ROOT%{_bindir}/snice

rm -f $RPM_BUILD_ROOT/bin/kill
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{snice,kill,oldps}.1
rm -f $RPM_BUILD_ROOT%{_bindir}/{oldps,kill}

echo .so skill.1 > $RPM_BUILD_ROOT%{_mandir}/man1/snice.1

install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/pl/man1/free.1
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man1/uptime.1
install %{SOURCE3} $RPM_BUILD_ROOT%{_mandir}/pl/man1/ps.1

strip --strip-unneeded $RPM_BUILD_ROOT/lib/*.so.*.*

gzip -9fn $RPM_BUILD_ROOT%{_mandir}/{man*/*,pl/man*/*} \
	NEWS BUGS TODO

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
%doc {NEWS,BUGS,TODO}.gz

%attr(755,root,root) /lib/libproc.so.*.*
%attr(755,root,root) /bin/*
%attr(755,root,root) /sbin/sysctl
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) /usr/X11R6/bin/XConsole

%lang(pl) %{_mandir}/pl/man*/*
%{_mandir}/man*/*

%{_applnkdir}/Administration/top.desktop
