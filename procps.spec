Summary:	Utilities for monitoring your system and processes on your system
Summary(de):	Utilities zum Ueberwachen Ihres Systems und der Prozesse
Summary(es):	Utilitarios de monitoración de procesos
Summary(fr):	Utilitaires de surveillance des processus
Summary(pl):	Narzêdzia do monitorowania procesów
Summary(pt_BR):	Utilitários de monitoração de processos
Summary(tr):	Süreç izleme araçlarý
Name:		procps
Version:	2.0.10
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://surriel.com/procps/%{name}-%{version}.tar.bz2
Source1:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-w2.patch
Patch1:		%{name}-sig.patch
Patch2:		%{name}-install.patch
Patch3:		%{name}-man.patch
Patch4:		%{name}-desktop.patch
URL:		http://surriel.com/procps/
BuildRequires:	ncurses-devel >= 5.1
Prereq:		fileutils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	procps-X11

%description
The procps package contains a set of system utilities which provide
system information. Procps includes ps, free, skill, snice, tload,
top, uptime, vmstat, w, and watch. The ps command displays a snapshot
of running processes. The top command provides a repetitive update of
the statuses of running processes. The free command displays the
amounts of free and used memory on your system. The skill command
sends a terminate command (or another specified signal) to a specified
set of processes. The snice command is used to change the scheduling
priority of specified processes. The tload command prints a graph of
the current system load average to a specified tty. The uptime command
displays the current time, how long the system has been running, how
many users are logged on and system load averages for the past one,
five and fifteen minutes. The w command displays a list of the users
who are currently logged on and what they're running. The watch
program watches a running program. The vmstat command displays virtual
memory statistics about processes, memory, paging, block I/O, traps
and CPU activity.

%description -l de
Das procps-Paket enthält System-Utilities, die Systeminformationen
anzeigen. Procps enthält ps, free, skill, snice, tload, top, uptime,
vmstat, w und watch. ps zeigt an, welche Prozesse gerade laufen. Top
zeigt in regelmäßigen Abständen eine Prozessliste an. Free zeigt an,
wieviel Speicher frei ist, und wieviel Speicher benutzt wird. Skill
schickt den Terminierungsbefehl (oder ein anderes angegebenes Signal)
an angegebene Prozesse. Snice ändert die Priorität von angegebenen
Prozessen. tload zeigt einen Graphen der aktuellen Systemauslastung
an. Uptime zeigt an, wie lange das System am laufen ist, wieviele User
eingeloggt sind, und die Auslastungswerte der letzten Minute, der
letzten 5 Minuten, und 15 Minuten. Der w-Befehl zeigt eine Liste der
User an, die gerade eingeloggt sind, und welches Programm sie
benutzen. Vmstat zeigt Statistiken über den virtuellen Speicher,
Prozesse, Paging, Block I/O, Traps, und CPU-Aktivität.

%description -l es
Un paquete de utilitarios que relatan el estado del sistema. Se da
énfasis a los procesos en ejecución, total de memoria disponible y a
los usuarios que están "logados" en el sistema.

%description -l fr
Paquetage d'utilitaires donnant des informations sur l'état du
système, dont les états des processus en cours, le total de mémoire
disponible, et les utilisateurs loggés.

%description -l pl
Pakiet zawiera podstawowe narzêdzia do monitorowania pracy systemu.
Dziêki tym programom bêdziesz móg³ na bie¿±co kontrolowaæ jakie
procesy s± w danej chwili uruchomione, ilo¶æ wolnej pamiêci, kto jest
w danej chwili zalogowany, jakie jest aktualne obci±¿enie systemu itp.

%description -l pt_BR
Um pacote de utilitários que relatam o estado do sistema. É dado
ênfase aos processos em execução, total de memória disponível e aos
usuários que estão logados no sistema.

%description -l tr
Sistemin durumunu rapor eden araçlar paketidir. Koþan süreçlerin
durumunu, kullanýlabilir bellek miktarýný, ve o an için sisteme girmiþ
kullanýcýlarý bildirir.

%package devel
Summary:	libproc header files
Summary(pl):	Pliki nag³ówkowe libproc
License:	LGPL
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
libproc header files.

%description devel -l pl
Pliki nag³ówkowe biblioteki libproc.

%package static
Summary:	Static libproc library
Summary(pl):	Statyczna biblioteka libproc
License:	LGPL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of libproc library.

%description static -l pl
Statyczna wersja biblioteki libproc.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
PATH=%{_prefix}/X11R6/bin:$PATH

%{__make} OPT="%{rpmcflags} -pipe -D__SMP__" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{bin,sbin,usr/X11R6/bin} \
	$RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5,8}} \
	$RPM_BUILD_ROOT%{_applnkdir}/System

%{__make} install libinstall \
	DESTDIR=$RPM_BUILD_ROOT \
	APPLNK=%{_applnkdir}/System

install XConsole   $RPM_BUILD_ROOT%{_prefix}/X11R6/bin

rm -f  $RPM_BUILD_ROOT%{_bindir}/snice
ln -sf skill $RPM_BUILD_ROOT%{_bindir}/snice

rm -f $RPM_BUILD_ROOT/bin/kill
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/{snice,kill,oldps}.1
rm -f $RPM_BUILD_ROOT%{_bindir}/{oldps,kill}

echo ".so skill.1" > $RPM_BUILD_ROOT%{_mandir}/man1/snice.1

bzcat -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
rm -f $RPM_BUILD_ROOT%{_mandir}/*/man1/{kill,oldps}.1

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
if [ -f /proc/uptime ] ; then
	/bin/ps </dev/null >/dev/null 2>&1
fi
rm -f %{_sysconfdir}/psdevtab %{_sysconfdir}/psdatabase

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS BUGS TODO
%attr(755,root,root) /lib/libproc.so.*.*
%attr(755,root,root) /bin/*
%attr(755,root,root) /sbin/sysctl
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_prefix}/X11R6/bin/XConsole
%{_mandir}/man*/*
%lang(cs) %{_mandir}/cs/man*/*
%lang(de) %{_mandir}/de/man*/*
%lang(es) %{_mandir}/es/man*/*
%lang(fi) %{_mandir}/fi/man*/*
%lang(fr) %{_mandir}/fr/man*/*
%lang(hu) %{_mandir}/hu/man*/*
%lang(it) %{_mandir}/it/man*/*
%lang(ja) %{_mandir}/ja/man*/*
%lang(ko) %{_mandir}/ko/man*/*
%lang(nl) %{_mandir}/nl/man*/*
%lang(pl) %{_mandir}/pl/man*/*
%{_applnkdir}/System/top.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libproc.so
%{_includedir}/proc

%files static
%defattr(644,root,root,755)
%{_libdir}/libproc.a
