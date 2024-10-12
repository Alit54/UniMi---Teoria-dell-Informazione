# Teoria dell'Informazione
<html>
    <div align=center>
    Simone Alessandro Casciaro<br>
    11 Ottobre 2024
    </div>
</html>

## Lezione 4: Entropia
### Definizione
Sia una sorgente $<\Bbb{X}, P>$ con $\Bbb{X}=\{x_1,\dots,x_m\}$ e $P=\{p_1,\dots,p_m\}$. Per comodità, indichiamo con $p_i$ la probabilità con cui $x_i$ compare nel messaggio.<br>
Sia $X:\Bbb{X}\to\{a_1,\dots,a_m\}\subseteq\R$ una variabile aleatoria tale per cui $\Bbb{P}(X=a_i)=p_i$<br>
Chiamiamo <font color=red>Entropia</font> la funzione $$H_d(X)=\displaystyle\sum_{i=1}^mp_i\log_d{\frac1{p_i}}$$
L'entropia dipende solo dalla distribuzione di probabilità di $X$ e non da $X$ stessa.

### Cambio di base dell'entropia
Avendo $a, b$ e $p$, ricordiamo che $\log_b p=\log_b a*\log_a p$<br>
Quindi, per cambiare base all'entropia, possiamo:<br>
$H_b(X)=\displaystyle\sum_{i=1}^m p_i\log_b\frac1{p_i}=\sum_{i=1}^mp_i*\log_b a*\log_a\frac1{p_i}=\log_ba*\sum_{i=1}^mp_i\log_a\frac1{p_i}=\log_ba*H_a(X)$<br>
Dunque, $$H_b(X)=\log_ba*H_a(X)$$

### Rappresentazione sul Piano Cartesiano
Sia $X$ una variabile aleatoria Bernoulliana<br>
$X:\Bbb{X}\to\{0,1\}$ tale che $\Bbb{P}(X=1)=p$ e $\Bbb{P}(X=0)=1-p$<br>

![Grafico dell'Entropia](/img/Entropia.png)<br>
L'entropia risulta minima quando $p=0$ oppure $p=1$, mentre è massima quando $p=\displaystyle\frac12$. Questo indica che l'entropia è un indice che misura la quantità di informazione. Maggiore è l'entropia, maggiore è l'informazione spedita sul canale.

### Maggiorante e minorante del $\ln x$
![Maggiorante e Minorante](/img/Logaritmo.png)<br>
Come si vede dal disegno, abbiamo che $\forall x\in\R:\displaystyle1-\frac1x\le\ln x\le x-1$<br>
Questa informazione ci sarà utile per le dimostrazioni successive.

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

### Entropia Relativa
L'entropia relativa è una misura di distanza (non simmetrica!) tra due variabili aleatorie $X$ e $Y$ entrambe definite sul dominio $S$ ma con due funzioni di probabilità diverse, che chiamiamo $p_X$ e $p_Y$.<br>
$$D_d(X||Y) = \displaystyle\sum_{s\in S}p_X(s)\log_d\frac{p_X(s)}{p_Y(s)}$$
<font color=orange>NOTA BENE:</font> $D_d(X||Y) \ne D_d(Y||X)$

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

### Algoritmo di Sardinas-Patterson
L'algoritmo di Sardinas-Patterson è il punto di riferimento per capire se un codice è univocamente decodificabile oppure no.<br>
Si parte indicando con $S_1$ le parole del codice. Poi, si procede con due fasi:<br>
1. Si prendono tutti gli $x\in S_1:xy\in S_i$ e si mettono gli $y$ in $S_{i+1}$
2. Si prendono tutti gli $x\in S_i:xy\in S_1$ e si mettono gli $y$ in $S_{i+1}$

Al primo passaggio, $i=1$ dunque i due insiemi coincideranno.<br>
L'algoritmo termina in due casi:<br>
1. Uno degli $S_i$ contiene una parola del codice. In questo caso il codice non è UD.
2. Si arriva ad avere un $S_i$ vuoto. In questo caso il codice è UD.

> Esempio<br>
$S_1=\{A, E, C, ABB, CED, BBEC\}$<br><br>
Costruiamo $S_2$<br>
Fase A:<br>
$A$ è prefisso di $ABB$, dunque inseriamo $BB$ in $S_2$<br>
$C$ è prefisso di $CED$, dunque inseriamo $ED$ in $S_2$<br>
Fase B:<br>
$A$ è prefisso di $ABB$, ma abbiamo già inserito $BB$ in $S_2$<br>
$C$ è prefisso di $CED$, ma abbiamo già inserito $ED$ in $S_2$<br>
Dunque $S_2=\{BB, ED\}$<br><br>
Ora confrontiamo $S_1$ e $S_2$ e costruiamo $S_3$<br>
Fase A:<br>
$E$ è prefisso di $ED$, dunque inseriamo $D$ in $S_3$<br>
Fase B:<br>
$BB$ è prefisso di $BBEC$, dunque inseriamo $EC$ in $S_3$<br>
Dunque $S_3=\{D, EC\}$<br><br>
Ora confrontiamo $S_1$ e $S_3$ e costruiamo $S_4$<br>
Fase A:<br>
$E$ è prefisso di $EC$, dunque inseriamo $C$ in $S_4$<br>
Fase B:<br>
$\nexists$<br>
Dunque $S_4=\{C\}$<br>
L'algoritmo termina perché $S_4$ contiene $C$, che è una parola del codice. Dunque il codice non è UD.

### Esercizio
Determinare se il codice $\{A, BCA, DE, CBC, AABC, C\}$ è univocamente decodificabile.<br>
Se non lo è, trovare una stringa non decodificabile.<br>

$S_1 = \{A, BCA, DE, CBC, AABC, C\}$<br>
$S_2 = \{ABC, BC\}$<br>
$S_3 = \{BC, A\}$<br>
$A$ è una parola del codice, dunque il codice non è univocamente decodificabile.<br>
Ad esempio, la stringa $CBCA$ potrebbe essere interpretata sia come $C, BCA$ che come $CBC, A$