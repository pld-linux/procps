Summary:     Process monitoring utilities
Summary(de): Dienstprogramm zur Prozeßüberwachung
Summary(fr): Utilitaires de surveillance des processus.
Summary(pl): Narzêdzia do monitorowania procesów
Summary(tr): Süreç izleme araçlarý
Name:        procps
Version:     1.2.8
Release:     4
Copyright:   GPL
Group:       Utilities/System
Source:      ftp://tsx-11.mit.edu/pub/linux/sources/usr.bin/%{name}-%{version}.tar.gz
Patch0:      procps-1.2.8-jbj.patch
Patch1:      procps-rpm_opt_flags.patch
Buildroot:   /tmp/%{name}-%{version}-root

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

%package X11
Summary:     X-based process monitoring utilities
Summary(de): Prozeßüberwachungs-Dienstprogramme für X
Summary(fr): Utilitaires de surveillance des processus sous X
Summary(pl): Narzêdzia do monitorowania procesów pod X Window
Summary(tr): X tabanlý süreç izleme araçlarý
Group:       X11/Utilities

%description X11
A package of X-based utilities which report on the state of the system.
These utilities generally provide graphical presentations of information
available from tools in the procps suite.

%description -l de X11
Ein Utility-Paket auf X-Basis, die über den Systemstatus orientieren. 
Dabei werden die von den Tools aus der procps-Suite gelieferten Daten 
n grafischer Weise dargestellt.

%description -l fr X11
Paquetage d'utilitaires X rapportant l'état du système. Ces utilitaires
offrent généralement des représentations graphiques des informations
disponibles à partir d'outils de la suite procps.

%description -l pl X11
Pakiet zawiera narzêdzia do monitorowania systemu pod X Window. Inmformacje
o stanie systemu s± prezentowane w sposób graficzny.

%description -l tr X11
Sistemin durumunu gösteren, X tabanlý araçlar. Bu araçlar, genellikle
procps paketinde yer alan araçlarla edinebileceðiniz bilgileri grafik olarak
görüntülerler.

%prep
%setup -q
%patch0 -p1 -b .jbj
%patch1 -p1

%build
PATH=/usr/X11R6/bin:$PATH

make LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,bin,lib,usr/{bin,sbin,man/man1,man/man8}}

make install DESTDIR=$RPM_BUILD_ROOT BINGRP=$USER

install top.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/top

strip $RPM_BUILD_ROOT/lib/lib*.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post
# add libproc to the cache
/sbin/ldconfig
# ask ps to set up /etc/psdevtab if /proc is mounted
if [ -f /proc/uptime ] ; then
  /bin/ps </dev/null >/dev/null 2>&1
fi

%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%doc NEWS BUGS TODO
%config(missingok) /etc/X11/wmconfig/top
%attr(755, root, root) /lib/lib*.so.*.*
%attr(755, root, root) /bin/*
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man[18]/

%files X11
%attr(4755, root, root) /usr/X11R6/bin/XConsole

%changelog
* Fri Sep 11 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.2.8-4]
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- added %postun -p /sbin/ldconfig,
- simplification in %files,
- procps is now linked with libncurse instead libtermcap,
- fixed passing $RPM_OPT_FALGS (procps-rpm_opt_flags.patch),
- added striping shared libraries.

* Wed Sep 09 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.2.7-2]
- added pl translation,
- build from non root's account.

* Fri Aug 21 1998 Jeff Johnson <jbj@redhat.com>
- no writable strings patch (problem #856)

* Wed Jun 03 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
