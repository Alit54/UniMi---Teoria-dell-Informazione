# Teoremi e Dimostrazioni


Indice dei Teoremi e Dimostrazioni
- [Codice Istantaneo $\implies$ Codice Univocamente Decodificabile](https://github.com/Alit54/UniMi---Teoria-dell-Informazione/blob/develop/Teoremi.md#L12)
- [Disuguaglianza di Kraft](https://github.com/Alit54/UniMi---Teoria-dell-Informazione/blob/develop/Teoremi.md#L32)
- [Information Inequality $[D_d(X||Y)\ge0]$](https://github.com/Alit54/UniMi---Teoria-dell-Informazione/blob/develop/Teoremi.md#L64)
- [$H_d(X)\le\log_dm$](https://github.com/Alit54/UniMi---Teoria-dell-Informazione/blob/develop/Teoremi.md#L80)
- [$\Bbb{E}(l_c)\ge H_d(X)$](https://github.com/Alit54/UniMi---Teoria-dell-Informazione/blob/develop/Teoremi.md#L103)
- [$\Bbb{E}(l_c)< H_d(X)+1$](https://github.com/Alit54/UniMi---Teoria-dell-Informazione/blob/develop/Teoremi.md#L132)
- [Primo Teorema di Shannon](https://github.com/Alit54/UniMi---Teoria-dell-Informazione/blob/develop/Teoremi.md#L142)

### <font color=red>Un codice istantaneo è univocamente decodificabile?</font>
Vogliamo dimostrare che
$$c \text{ istantaneo}\implies c \text{ univocamente decodificabile}$$
Per dimostrarlo, pensiamo alla contronominale.
$$c \text{ non univocamente decodificabile}\implies c \text{ non istantaneo}$$
Sia $c: X\to D^+$ e $C:X^+\to D^+$ la sua estensione.<br>
Se $c$ non è univocamente decodificabile, allora $\exists x, x'\in X^+, x\ne x':C(x)=C(x')$.<br>
Possono esistere due casi:<br>

1. 
![x prefisso di x'](/img/ISTtoUD/caso1.jpeg)<br>
$x'$ è prefisso di $x$. Per far sì che le due codifiche siano uguali, la parte che "eccede" $x'$ in $x$ deve essere codificata nella parola vuota $\empty$. Questo è assurdo, perché $C:X^+\to D^+$ e $\empty$ non fa parte del codominio. In ogni caso, se anche considerassimo un'ulteriore estensione di $\hat C:X^+\to D^*$ che comprende anche la parola vuota nel codominio, tale parola sarebbe prefissa di ogni altra e questo renderebbe il codice non istantaneo.

2. 
![Prefisso comune](/img/ISTtoUD/caso2.jpeg)<br>
$x$ e $x'$ condividono una parte comune, salvo differire nella parte finale. La parte comune avrà chiaramente la stessa codifica, dunque ci concentriamo sulla parte non comune.<br>
Supponiamo per semplicità che la parte non comune sia formata da due caratteri ciascuna. La loro codifica totale sarà la stessa, ma dal disegno si può vedere come la codifica di "$C$" sia prefisso della codifica di "$A$", rendendo il codice non istantaneo.

![C prefisso di A](/img/ISTtoUD/codifica.jpeg)

### Disuguaglianza di Kraft
#### Ipotesi
Dati: 
- una sorgente $X=\{x_1,\dots,x_m\}$
- $d$ base del codice
- $m$ numero di elementi del messaggio
- $l_c = (l_1,\dots,l_m) > 0$ lunghezze delle codifiche dei simboli

#### Tesi
$$\exists \text{ codice istantaneo } c:X\to D^+ \text{ t.c.}\ l_c(x_i)=l_i\ \forall i=1,\dots,m
\iff \displaystyle\sum_{i=1}^md^{-l_i}\le 1$$

#### Dimostrazione
$\boxed{\implies}$<br>
Supponiamo di avere un codice istantaneo $c$. Dato che questa è una dimostrazione per costruzione, lo dimostriamo con un esempio.<br>
$c(x_1)=00\\
c(x_2)=010\\
c(x_3)=011\\
c(x_4)=1\\$
Sia $l_{max}=\displaystyle\max_{i=1,\dots,m}l_c(x_i)$ la massima altezza dell'albero di codifica. Disegnamo l'albero di codifica di $c$. In questo caso, $l_{max} = 3$.<br>
![](/img/kraft/kraft1.png)<br>
DIciamo che ogni $c(x_i)$ "copre" il suo sottoalbero e chiamiamo $A_i$ l'insieme delle foglie all'interno del sottoalbero generato dal nodo $c(x_i)$. Dato che $c$ è un codice istantaneo, tutti gli insiemi $A$ sono disgiunti tra loro.<br>
Il numero di foglie totali è $d^{l_{max}}$.<br>
$$\displaystyle\sum_{i=1}^md^{l_{max}-l_i}=\sum_{i=1}^m|A_i|\le d^{l_{max}}$$
Prendendo gli estremi di questa disuguaglianza e dividendo tutto per $d^{l_{max}}$, otteniamo $$\displaystyle\sum_{i=1}^md^{-l_i}\le1$$
<br>
$\boxed{\impliedby}$<br>
Sempre per costruzione, partiamo dal vettore $l = (2, 1, 3, 3)$<br>
Controlliamo la sommatoria per vedere se rispettiamo le ipotesi della disuguaglianza. <br>
$\displaystyle\sum_{i=1}^md^{-l_i} = \frac{1}{2^2} + \frac{1}{2^1} + \frac{1}{2^3} + \frac{1}{2^3} = \frac14 + \frac12 + \frac18 + \frac18 = 1\le 1$<br>
Possiamo costruire un albero di codifica in modo tale che il codice che rappresenta sia istantaneo (Ad esempio quello usato per la prima parte della dimostrazione). Dato che si riesce a costruirlo, $\exists c$ codice istantaneo. $\square$

### Information Inequality
#### Ipotesi
$X, Y$ due variabili aleatorie definite sul dominio $S$<br>
$d>1$
#### Tesi
$D_d(X||Y)\ge0$
#### Dimostrazione
$D_d(X||Y)$<br>
$=\displaystyle\sum_{s\in S}p_X(s)\log_d\frac{p_X(s)}{p_Y(s)}\qquad$ Per definizione di Entropia Relativa<br>
$=\displaystyle\sum_{s\in S}p_X(s)*\log_de*\ln\frac{p_X(s)}{p_Y(s)}\qquad$ Cambio di base del logaritmo<br>
$=\displaystyle\log_d e\sum_{s\in S}p_X(s)\ln\frac{p_X(s)}{p_Y(s)}$<br>
$\ge\displaystyle\frac1{\ln d}\sum_{s\in S}p_X(s)\Bigg(1-\frac{p_Y(s)}{p_X(s)}\Bigg)\qquad$ perché $\displaystyle 1-\frac1x \le \ln x\quad\forall x$ e $d>1$<br>
$=\displaystyle\frac1{\ln d}\sum_{s\in S}\bigg(p_X(s)-p_Y(s)\bigg)$<br>
$=\displaystyle\frac1{\ln d}\Bigg(\sum_{s\in S}p_X(s)-\sum_{s\in S}p_Y(s)\Bigg)$<br>
$=\displaystyle\frac1{\ln d}(1-1)=0$<br>

### Enunciato: $H_d(X)\le\log_dm\quad\forall d>1$
#### Ipotesi
Sia $X$ una variabile aleatoria<br>
#### Tesi
$H_d(X)\le\log_dm\quad\forall d>1$<br>
$H_d(X)=\log_dm\iff X$ ha una distribuzione uniforme.
#### Dimostrazione
Vogliamo dimostrare che $H_d(X)-\log_dm\le0$<br>
$H_d(X)-\log_dm=$<br>
$\displaystyle=\sum_{i=1}^mp_i\log_d\frac1{p_i}-\log_dm\qquad$ Per definizione di Entropia<br>
$\displaystyle=\sum_{i=1}^mp_i\log_d\frac1{p_i}-\log_dm\sum_{i=1}^mp_i\qquad$ perché $\displaystyle\sum_{i=1}^mp_i=1$<br>
$\displaystyle=\sum_{i=1}^mp_i\log_d\frac1{p_i}-\sum_{i=1}^mp_i\log_dm\qquad$<br>
$\displaystyle=\sum_{i=1}^mp_i\bigg(\log_d\frac1{p_i}-\log_dm\bigg)\qquad$<br>
$\displaystyle=\sum_{i=1}^mp_i\bigg(\log_d\frac1{p_im}\bigg)\qquad$<br>
$\displaystyle=\sum_{i=1}^mp_i\bigg(\log_de*\ln\frac1{p_im}\bigg)\qquad$ Cambio di base del logaritmo<br>
$\displaystyle=\sum_{i=1}^mp_i\bigg(\frac1{\ln d}*\ln\frac1{p_im}\bigg)\qquad$<br>
$\displaystyle=\frac1{\ln d}\sum_{i=1}^mp_i\bigg(\ln\frac1{p_im}\bigg)\qquad$<br>
$\displaystyle\le\frac1{\ln d}\sum_{i=1}^mp_i\bigg(\frac1{p_im}-1\bigg)\qquad$ $\ln x\le x-1\quad\forall x$ e perché $d>1$<br>
$\displaystyle=\frac1{\ln d}\sum_{i=1}^m\bigg(\frac1{m}-p_i\bigg)\qquad$<br>
$\displaystyle=\frac1{\ln d}\sum_{i=1}^m\bigg(\frac1{m}-p_i\bigg)\qquad$<br>
$\displaystyle=\frac1{\ln d}\Bigg(\sum_{i=1}^m\frac1{m}-\sum_{i=1}^mp_i\Bigg)\qquad$<br>
$\displaystyle=\frac1{\ln d}(1-1)=0$

### Teorema $\Bbb{E}(l_c)\ge H_d(X)$
#### Ipotesi
$c:\Bbb{X}\to D^+$ codice istantaneo $d$-ario per una sorgente $<\Bbb{X}, P>$
#### Tesi
$\Bbb{E}(l_c)\ge H_d(X)$
#### Dimostrazione
Sia $Y: \Bbb{X}\to\R$ una variabile aleatoria con funzione di probabilità $\displaystyle q(x)=\frac{d^{-l_c(x)}}{\displaystyle\sum_{x'\in X}d^{-l_c(x')}}$<br>
Vogliamo dimostrare che $\Bbb{E}(l_c)-H_d(X)\ge0$<br>
$\Bbb{E}(l_c)-H_d(X)$<br>
$\displaystyle=\sum_{x\in X}p(x)l_c(x)-\sum_{x\in X}p(x)\log_d\frac1{p(x)}$<br>
$\displaystyle=\sum_{x\in X}p(x)\Bigg(l_c(x)-\log_d\frac1{p(x)}\Bigg)$<br>
$\displaystyle=\sum_{x\in X}p(x)\Bigg(\log_dd^{l_c(x)}-\log_d\frac1{p(x)}\Bigg)$<br>
$\displaystyle=\sum_{x\in X}p(x)\Bigg(\log_d\frac1{d^{-l_c(x)}}+\log_dp(x)\Bigg)$<br>
$\displaystyle=\sum_{x\in X}p(x)\log_d\frac{p(x)}{d^{-l_c(x)}}$<br>
$\displaystyle=\sum_{x\in X}p(x)\log_d\Bigg(\frac{p(x)}{d^{-l_c(x)}}\frac{\displaystyle\sum_{x'\in X}d^{-l_c(x)}}{\displaystyle\sum_{x'\in X}d^{-l_c(x)}}\Bigg)$<br>
$\displaystyle=\sum_{x\in X}p(x)*\Bigg[\log_d\Bigg(p(x)\frac{\displaystyle\sum_{x'\in X}d^{-l_c(x)}}{d^{-l_c(x)}}\Bigg)-\log_d\Bigg(\sum_{x'\in X}d^{-l_c(x)}\Bigg)\Bigg]$<br>
Dividiamo la sommatoria in due punti da studiare separatamente:<br>
1. $\displaystyle\sum_{x\in X'}p(x)\log_d\Bigg(p(x)\frac{\sum_{x'\in X}d^{-l_c(x)}}{d^{-l_c(x)}}\Bigg)$<br>
$\displaystyle\sum_{x\in X}p(x)\log_d\Bigg(\frac{p(x)}{q(x)}\Bigg)$<br>
$D_d(X||Y)\ge0$<br>
<br>

2. $\displaystyle\sum_{x\in X}p(x)\log_d\bigg(\sum_{x'\in X}d^{-l_c(x')}\bigg)$<br>
$\displaystyle=\log_d\bigg(\sum_{x'\in X}d^{-l_c(x')}\bigg)\sum_{x\in X}p(x)$<br>
$\displaystyle=\log_d\bigg(\sum_{x'\in X}d^{-l_c(x')}\bigg)$<br>
$\displaystyle\le\log_d1=0$

Di conseguenza, unendo i due punti, abbiamo qualcosa di positivo a cui viene sottratto qualcosa di negativo. $(1)-(2)\ge0$

### Upper Bound del Valore Atteso
#### Ipotesi
Data una sorgente $<\Bbb{X},\Bbb P>$ e la variabile aleatoria $X:\Bbb X\to\R$ <br>
Dato $c$ codice di Shannon (quindi istantaneo) con lunghezza delle codifiche $l_i=l_c(x_i)\quad\forall i=1,\dots,m$ tali che $\displaystyle l_i=\lceil\log_d{\frac1{p_i}}\rceil$ 
#### Tesi
$$\Bbb E(l_c)<H_d(X)+1$$
#### Dimostrazione
$\Bbb E(l_c)=\displaystyle\sum_{i=1}^mp_il_i = \sum_{i=1}^mpi\lceil\log_d\frac1{p_i}\rceil < \sum_{i=1}^mp_i(\log_d\frac1{p_i}+1)=\sum_{i=1}^mp_i\log_d\frac1{p_i}+\sum_{i=1}^mp_i=H_d(X)+1$

### Primo Teorema di Shannon
#### Ipotesi
Sia $C_n:\Bbb{X}^n\to D^+$ la codifica di un codice a blocchi di Shannon $d-$ ario per la sorgente $<\Bbb{X},\Bbb{P}>$ tale che $l_{C_n}(x_1,\dots,x_n)=\displaystyle\lceil\log_d\frac1{\Bbb{P}_n(x_1,\dots,x_n)}\rceil$
#### Tesi
$$\displaystyle\lim_{n\to\infin}\frac1n\Bbb{E}(l_{C_n})=H_d(X)$$
#### Dimostrazione
Da precedenti dimostrazioni, sappiamo che $H_d(X_1,\dots,X_n)\le\Bbb E(l_{C_n})<H_d(X_1,\dots,X_n)+1$<br>
Inoltre, sappiamo che $H_d(X_1,\dots,X_n)=nH_d(X)$<br>
Unendo le due cose, si ha che $nH_d(X)\le\Bbb{E}(l_{C_n})<nH_d(X)+1$<br>
Per ottenere la tesi, si divide tutta la disequazione per $n$:<br>
$H_d(X)\le\displaystyle\frac1n\Bbb{E}(l_{C_n})<H_d(X)+\frac1n$<br>
Ponendo il $\displaystyle\lim_{n\to\infin}$, si ha che $\displaystyle\frac1n\Bbb{E}(l_{C_n})$ è compreso tra $H_d(X)$ e $H_d(X)+$ un infinitesimo, dunque $$\displaystyle\lim_{n\to\infin}\frac1n\Bbb{E}(l_{C_n})=H_d(X)$$