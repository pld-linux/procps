#
# Conditional build:
%bcond_without	systemd		# systemd support
%bcond_with	selinux		# selinux support

Summary:	Utilities for monitoring your system and processes on your system
Summary(de.UTF-8):	Utilities zum Ueberwachen Ihres Systems und der Prozesse
Summary(es.UTF-8):	Utilitarios de monitoración de procesos
Summary(fr.UTF-8):	Utilitaires de surveillance des processus
Summary(pl.UTF-8):	Narzędzia do monitorowania procesów
Summary(pt_BR.UTF-8):	Utilitários de monitoração de processos
Summary(tr.UTF-8):	Süreç izleme araçları
Name:		procps
Version:	3.3.10
Release:	0.1
Epoch:		1
License:	GPL v2+
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/procps-ng/%{name}-ng-%{version}.tar.xz
# Source0-md5:	1fb7f3f6bf92ce6c5c9ed9949ae858fe
Source1:	%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	60d24720b76c10553ed4abf68b76e079
Source2:	top.desktop
Source3:	top.png
Source4:	XConsole.sh
Patch0:		%{name}-missing-symbol.patch
Patch1:		%{name}-FILLBUG_backport.patch
URL:		https://gitlab.com/procps-ng/procps
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools >= 0.14.1
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	libtool >= 2:2
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.402
BuildRequires:	sed >= 4.0
%{?with_systemd:BuildRequires:	systemd-devel >= 1:206}
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post):	/sbin/ldconfig
Requires:	fileutils
Obsoletes:	procps-X11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The procps package contains a set of system utilities which provide
system information. Procps includes ps, free, skill, snice, tload,
top, uptime, vmstat, w and watch. The ps command displays a snapshot
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

%description -l de.UTF-8
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

%description -l es.UTF-8
Un paquete de utilitarios que relatan el estado del sistema. Se da
énfasis a los procesos en ejecución, total de memoria disponible y a
los usuarios que están "logados" en el sistema.

%description -l fr.UTF-8
Paquetage d'utilitaires donnant des informations sur l'état du
système, dont les états des processus en cours, le total de mémoire
disponible, et les utilisateurs loggés.

%description -l pl.UTF-8
Pakiet zawiera podstawowe narzędzia do monitorowania pracy systemu.
Dzięki tym programom będziesz mógł na bieżąco kontrolować jakie
procesy są w danej chwili uruchomione, ilość wolnej pamięci, kto jest
w danej chwili zalogowany, jakie jest aktualne obciążenie systemu itp.

%description -l pt_BR.UTF-8
Um pacote de utilitários que relatam o estado do sistema. É dado
ênfase aos processos em execução, total de memória disponível e aos
usuários que estão logados no sistema.

%description -l tr.UTF-8
Sistemin durumunu rapor eden araçlar paketidir. Koşan süreçlerin
durumunu, kullanılabilir bellek miktarını, ve o an için sisteme girmiş
kullanıcıları bildirir.

%package devel
Summary:	libproc header files
Summary(pl.UTF-8):	Pliki nagłówkowe libproc
License:	LGPL
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
libproc header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libproc.

%package static
Summary:	Static libproc library
Summary(pl.UTF-8):	Statyczna biblioteka libproc
License:	LGPL
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static version of libproc library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libproc.

%prep
%setup -qn %{name}-ng-%{version}
%patch0 -p1
%patch1 -p1

%{__sed} -i -e "s#usrbin_execdir=.*#usrbin_execdir='\${bindir}'#g" configure.ac

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_systemd:--enable-systemd} \
	%{?with_selinux:--enable-libselinux} \
	--disable-pidof \
	--enable-oomem \
	--enable-sigwinch \
	--enable-skill \
	--enable-w-from \
	--enable-watch8bit \
	--enable-wide-percent \
	--sbindir=/sbin
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir},/%{_lib},/bin}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

# identical binaries are copied, not linked:
ln -f $RPM_BUILD_ROOT%{_bindir}/{pkill,pgrep}
ln -f $RPM_BUILD_ROOT%{_bindir}/{snice,skill}

mv $RPM_BUILD_ROOT{%{_bindir},/bin}/ps

install -d $RPM_BUILD_ROOT/%{_lib}
mv -f $RPM_BUILD_ROOT{%{_libdir}/libprocps.so.*,/%{_lib}}
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libprocps.so.*.*.*) \
        $RPM_BUILD_ROOT%{_libdir}/libprocps.so

cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}
install -p %{SOURCE4} $RPM_BUILD_ROOT%{_bindir}/XConsole

# PLD: kill is packaged in util-linux
%{__rm} $RPM_BUILD_ROOT%{_bindir}/kill
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/kill.1
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libprocps.la
# packaged as doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/procps-ng

bzcat -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/*/man1/{kill,oldps}.1
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README-procps-non-english-man-pages

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS Documentation/{BUGS,FAQ,TODO} NEWS README top/README.top
%attr(755,root,root) /%{_lib}/libprocps.so.*.*
%ghost %attr(755,root,root) /%{_lib}/libprocps.so.4
%attr(755,root,root) /bin/ps
%attr(755,root,root) /sbin/sysctl
%attr(755,root,root) %{_bindir}/XConsole
%attr(755,root,root) %{_bindir}/free
%attr(755,root,root) %{_bindir}/pgrep
%attr(755,root,root) %{_bindir}/pkill
%attr(755,root,root) %{_bindir}/pmap
%attr(755,root,root) %{_bindir}/pwdx
%attr(755,root,root) %{_bindir}/skill
%attr(755,root,root) %{_bindir}/slabtop
%attr(755,root,root) %{_bindir}/snice
%attr(755,root,root) %{_bindir}/tload
%attr(755,root,root) %{_bindir}/top
%attr(755,root,root) %{_bindir}/uptime
%attr(755,root,root) %{_bindir}/vmstat
%attr(755,root,root) %{_bindir}/w
%attr(755,root,root) %{_bindir}/watch
%{_desktopdir}/top.desktop
%{_pixmapsdir}/top.png
%{_mandir}/man1/free.1*
%{_mandir}/man1/pgrep.1*
%{_mandir}/man1/pkill.1*
%{_mandir}/man1/pmap.1*
%{_mandir}/man1/ps.1*
%{_mandir}/man1/pwdx.1*
%{_mandir}/man1/skill.1*
%{_mandir}/man1/slabtop.1*
%{_mandir}/man1/snice.1*
%{_mandir}/man1/tload.1*
%{_mandir}/man1/top.1*
%{_mandir}/man1/uptime.1*
%{_mandir}/man1/w.1*
%{_mandir}/man1/watch.1*
%{_mandir}/man5/sysctl.conf.5*
%{_mandir}/man8/sysctl.8*
%{_mandir}/man8/vmstat.8*
%lang(cs) %{_mandir}/cs/man[158]/*
%lang(de) %{_mandir}/de/man[158]/*
%lang(es) %{_mandir}/es/man[158]/*
%lang(fi) %{_mandir}/fi/man[158]/*
%lang(fr) %{_mandir}/fr/man[158]/*
%lang(hu) %{_mandir}/hu/man[158]/*
%lang(it) %{_mandir}/it/man[158]/*
%lang(ja) %{_mandir}/ja/man[158]/*
%lang(ko) %{_mandir}/ko/man[158]/*
%lang(nl) %{_mandir}/nl/man[158]/*
%lang(pl) %{_mandir}/pl/man[158]/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libprocps.so
%{_includedir}/proc
%{_pkgconfigdir}/libprocps.pc
%{_mandir}/man3/openproc.3*
%{_mandir}/man3/readproc.3*
%{_mandir}/man3/readproctab.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libprocps.a
