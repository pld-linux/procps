.\" {PTM/LK/0.1/08-10-1998/"zakoñczenie procesu"}
.\" T³umaczenie: 08-10-1998 £ukasz Kowalczyk (lukow@tempac.okwf.fuw.edu.pl)
.\" Copyright 1994 Salvatore Valente (svalente@mit.edu)
.\" Copyright 1992 Rickard E. Faith (faith@cs.unc.edu)
.\" May be distributed under the GNU General Public License
.TH KILL 1 "14 pa¼dziernika 1994" "Programy u¿ytkowe" "Instrukcja Programisty Linuksa"
.SH NAZWA
kill \- zakoñcz proces
.SH SK£ADNIA
.BR "kill" " [ \-s sygna³ | \-p ] " " [ -a ] " "pid ..."
.br
.B "kill -l [ sygna³ ]"
.SH OPIS
.B kill
wysy³a podany sygna³ do danego procesu. Je¿eli nie podano numeru sygna³u,
wysy³any jest sygna³ TERM. Sygna³ TERM koñczy te procesy, które go nie
przechwytuj±. Dla innych procesów niezbêdne mo¿e siê okazaæ u¿ycie sygna³u
KILL (9), poniewa¿ nie mo¿e on zostaæ przechwycony.

Wiêkszo¶æ nowoczesnych shelli posiada wbudowane polecenie kill.
.SH OPCJE
.TP
.BR "pid ..."
Lista procesów, które maj± byæ zakoñczone. Ka¿da opcja
.I pid
mo¿e byæ jedn± z nastêpuj±cych:
.IR "nazwa procesu" ,
wówczas sygna³ zostanie wys³any do nazwanego procesu.
.IR n ,
gdzie
.I n
jest liczb± wiêksz± od zera. Sygna³ zostanie wys³any do procesu, którego
pid jest równy
.IR n .
.IR -1 ,
w którym to przypadku sygna³ zostanie wys³any do wszystkich procesów o
numerach pid o warto¶ciach od MAX_INT do 2, je¿eli pozwalaj± na to
uprawnienia u¿ytkownika.
.\" (przyp. t³um.) to by³ oryginalny tekst; moim zdaniem o to chodzi³o ^^^
.\" as allowed by the issuing user.
.IR -n ,
gdzie n jest wiêksze od 1; sygna³ zostanie wys³any do wszystkich procesów
nale¿±cych do grupy o numerze
.IR n .
Je¿eli 
.I n
jest ujemne, musi przed nim wyst±piæ numer sygna³u \- w przeciwnym wypadku
numer grupy zostanie potraktowany jako numer sygna³u do wys³ania.
.TP
.BR \-s
Rodzaj wysy³anego sygna³u. Mo¿e byæ podany jako nazwa lub numer.
.TP
.BR \-p
Polecenie wypisze jedynie numery procesów (pid), do których zosta³by wys³any
sygna³, zamiast go rzeczywi¶cie wysy³aæ.
.TP
.BR \-l
Wypisz listê nazw sygna³ów. Znajduje siê ona w pliku
.I /usr/include/linux/signal.h
.SH "ZOBACZ TAK¯E"
.BR bash (1),
.BR tcsh (1),
.BR kill (2),
.BR sigvec (2)
.SH AUTOR
Program pochodzi z BSD 4.4. Mo¿liwo¶æ t³umaczenia nazw procesów na ich
numery zosta³a dodana przez Salvatore Valente <svalente@mit.edu>.
