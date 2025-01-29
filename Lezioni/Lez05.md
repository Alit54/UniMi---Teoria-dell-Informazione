# Teoria dell'Informazione
<html>
    <div align=center>
    Simone Alessandro Casciaro<br>
    15 Ottobre 2024
    </div>
</html>

## Lezione 5: 1° Teorema di Shannon
### Upper Bound del Valore Atteso
#### Ipotesi
Data una sorgente $<\Bbb{X},\Bbb P>$ e la variabile aleatoria $X:\Bbb X\to\R$
Dato $c$ codice di Shannon (quindi istantaneo) con lunghezza delle codifiche $l_i=l_c(x_i)\quad\forall i=1,\dots,m$ tali che $\displaystyle l_i=\lceil\log_d{\frac1{p_i}}\rceil$ 
#### Tesi
$$\Bbb E(l_c)<H_d(X)+1$$
#### Dimostrazione
$\Bbb E(l_c)=\displaystyle\sum_{i=1}^mp_il_i = \sum_{i=1}^mpi\lceil\log_d\frac1{p_i}\rceil < \sum_{i=1}^mp_i\left(\log_d\frac1{p_i}+1\right)=\sum_{i=1}^mp_i\log_d\frac1{p_i}+\sum_{i=1}^mp_i=H_d(X)+1$

Problema!
Abbiamo dimostrato che l'errore che commettiamo stimando il valore atteso con l'entropia è compreso tra $0$ e $1$ (Dato che $H_d(X)\le\Bbb E(l_c)<H_d(X)+1$). Tuttavia, questo risultato è relativo alla codifica di ogni singolo simbolo, dunque il problema si moltiplica per il numero di simboli nel messaggio.
$$l_c(x_1,\dots,x_m)=\displaystyle\sum_{i=1}^ml_c(x_i)=\sum_{i=1}^m\left\lceil\log_d\frac1{p_i}\right\rceil$$
> <font color = 00cc99>Esempio</font>
$
\begin{aligned}
x_1&&x_2&&x_3\\
2.5&&2.1&&2.1\\
\lceil2.5\rceil&+&\lceil2.1\rceil&+&\lceil2.1\rceil&=9
\end{aligned}
$
Usiamo un trucco. Invece di sommare le approssimazioni, prima sommiamo e poi approssimiamo.
$\lceil 2.5+2.1+2.1 \rceil = \lceil 6.7 \rceil = 7$ e quindi risparmiamo $2$ bit.<br>

Costruiamo dunque un nuovo codice $$C_n:\Bbb X^n\to D^+$$ che codifica blocchi di simboli della sorgente di lunghezza fissa $n$.<br>
Idealmente questo codice è migliore di quelli visti precedentemente, ma la complessità computazionale del codice aumenta con l'aumentare di $n$.

### Entropia Congiunta
Supponiamo di avere una sorgente $<\Bbb{X},\Bbb P>$, dalla quale estraiamo una tupla $(x_1,\dots,x_n)$ che vogliamo codificare usando la funzione $C_n:\Bbb X^n\to D^+$.
Si ricorda che Shannon, per semplificare i calcoli, assume che i simboli di un messaggio siano indipendenti tra loro e, dunque, che $$p(x_1,\dots,x_n)=\displaystyle\prod_{i=1}^np(x_i)=\Bbb{P}_n(x_1,\dots,x_n)$$ Definiamo una nuova sorgente $<\Bbb{X}^n,\Bbb{P}_n>$ e ne calcoliamo l'entropia. Per farlo, supponiamo di avere $n$ variabili aleatorie $X_1,\dots,X_n$, tutte indipendenti e identicamente distribuite, che estraggono dalla stessa sorgente.
> Premessa utile per il calcolo successivo
$\displaystyle\log_d\frac1{\Bbb{P}(x_1,\dots,x_n)}=\log_d\frac1{\displaystyle\prod_{i=1}^np(x_i)}=\sum_{i=1}^n-(\log_dp_i)=\sum_{i=1}^n\log_d\frac1{p_i}$

$$
\begin{aligned}
H_d(X_1,\dots,X_n)&=\sum_{X_1,\dots,X_n}\Bbb P(x_1,\dots,x_n)\log_d\frac1{\Bbb{P}(x_1,\dots,x_n)}\\
&=\sum_{X_1}\sum_{X_2}\dots\sum_{X_n}\left(\prod_{i=1}^np(x_i)\right)*\sum_{i=1}^n\log_d\frac1{p(x_i)}
\end{aligned}
$$

Questa formula risulta complicata se pensata al caso generale $n$. Per comprenderla, proviamo a vedere cosa succede nel caso $\boxed{n=2}$

$$
\begin{aligned}
H_d(X_1,X_2)&=\sum_{X_1}\sum_{X_2}\prod_{i=1}^2p(x_i)\sum_{i=1}^2\log_d\frac1{p(x_i)}\\
&=\sum_{X_1}\sum_{X_2}\prod_{i=1}^2p(x_i)\left(\log_d\frac1{p(x_1)}+\log_d\frac1{p(x_2)}\right)\\
&=\sum_{X_1}\sum_{X_2}p(x_1)*p(x_2)*\left(\log_d\frac1{p(x_1)}+\log_d\frac1{p(x_2)}\right)\\
&=\sum_{X_1}\sum_{X_2}\left(p(x_1)*p(x_2)*\log_d\frac1{p(x_1)}+p(x_1)*p(x_2)\log_d\frac1{p(x_2)}\right)\\
&=\sum_{X_1}\sum_{X_2}p(x_1)*p(x_2)*\log_d\frac1{p(x_1)}+\sum_{X_1}\sum_{X_2}p(x_1)*p(x_2)*\log_d\frac1{p(x_2)}\\
&=\sum_{X_2}p(x_2)\sum_{X_1}p(x_1)\log_d\frac1{p(x_1)}+\sum_{X_1}p(x_1)\sum_{X_2}p(x_2)\log_d\frac1{p(x_2)}\\
&=\sum_{X_1}p(x_1)\log_d\frac1{p(x_1)}+\sum_{X_2}p(x_2)\log_d\frac1{p(x_2)}\\
&=H_d(X_1)+H_d(X_2)
\end{aligned}
$$
Dunque, in generale: $$H_d(X_1,\dots,X_n)=\displaystyle\sum_{i=1}^nH_d(X_i)$$ ma dato che le varie $X_i$ seguono la stessa distribuzione di probabilità di $X$, vale che
$$H_d(X_1,\dots,X_n)=\displaystyle\sum_{i=1}^nH_d(X)=nH_d(X)$$

### Primo Teorema di Shannon
#### Ipotesi
Sia $C_n:\Bbb{X}^n\to D^+$ la codifica di un codice a blocchi di Shannon $d-$ ario per la sorgente $<\Bbb{X},\Bbb{P}>$ tale che $l_{C_n}(x_1,\dots,x_n)=\displaystyle\left\lceil\log_d\frac1{\Bbb{P}_n(x_1,\dots,x_n)}\right\rceil$
#### Tesi
$$\displaystyle\lim_{n\to\infin}\frac1n\Bbb{E}(l_{C_n})=H_d(X)$$
#### Dimostrazione
Da precedenti dimostrazioni, sappiamo che $H_d(X_1,\dots,X_n)\le\Bbb E(l_{C_n})<H_d(X_1,\dots,X_n)+1$

Inoltre, sappiamo che $H_d(X_1,\dots,X_n)=nH_d(X)$

Unendo le due cose, si ha che $nH_d(X)\le\Bbb{E}(l_{C_n})<nH_d(X)+1$

Per ottenere la tesi, si divide tutta la disequazione per $n$:
$$H_d(X)\le\displaystyle\frac1n\Bbb{E}(l_{C_n})<H_d(X)+\frac1n$$

Ponendo il $\displaystyle\lim_{n\to\infin}$, si ha che $\displaystyle\frac1n\Bbb{E}(l_{C_n})$ è compreso tra $H_d(X)$ e $H_d(X)+$ un infinitesimo, dunque $$\displaystyle\lim_{n\to\infin}\frac1n\Bbb{E}(l_{C_n})=H_d(X)$$

### Teorema: Upper Bound Valore Atteso di sorgente campionata
#### Ipotesi
Data una sorgente $<\Bbb{X},\Bbb{P}>$ e $c:\Bbb{X}\to D^+$ un codice di Shannon tale che $l_c(x)=\displaystyle\left\lceil\log_d\frac1{q(x)}\right\rceil$, dove $q$ è una distribuzione di probabilità stimata sulla sorgente $\Bbb{X}$ e associata alla variabile aleatoria $Y:\Bbb{X}\to\R$
#### Tesi
$$\Bbb{E}(l_c)<H_d(X)+1+D_d(X||Y)$$
#### Dimostrazione

$$
\begin{aligned}
\Bbb{E}(l_c)&=\sum_{x\in X}p(x)\left\lceil\log_d\frac1{q(x)}\right\rceil\\
&<\sum_{x\in X}p(x)\left(\log_d\frac1{q(x)}+1\right)\\
&=\sum_{x\in X}p(x)\log_d\frac1{q(x)}+\sum_{x\in X}p(x)\\
&=\sum_{x\in X}p(x)\log_d\frac1{q(x)}+1\\
&=\sum_{x\in X}p(x)\log_d\left(\frac1{q(x)}\frac{p(x)}{p(x)}\right)+1\\
&=\sum_{x\in X}p(x)\log_d\frac{p(x)}{q(x)}+\sum_{x\in }p(x)\log_d\frac1{p(x)}+1\\
&=D_d(X||Y)+H_d(X)+1
\end{aligned}
$$

### <font color=00cc99>Esercizi</font>
1. Ignorando la condizione di terminazione dell'algoritmo di [Sardinas-Patterson](/src/SardinasPatterson.py) dell'esercizio della scorsa lezione, provare ad andare avanti finché non si raggiunge un'ulteriore condizione di terminazione.
$S_5=\{ED\}$
$S_6=\{D\}$
$S_7=\{\}$
<br>

2. Costruire un codice istantaneo per una sorgente con le seguenti probabilità $\Bbb{P}\displaystyle=\left\{\frac13,\frac14,\frac16,\frac18,\frac19, x\right\}$
$x = \displaystyle 1-\frac{24-18-12-9-8}{72} = \frac1{72}$<br>
Dunque le lunghezze sono:
$
l_1=2\\l_2=2\\l_3=3\\l_4=3\\l_5=4\\l_6=7
$ <br>
E i relativi codici:
$
c(x_1)=00\\c(x_2)=01\\c(x_3)=100\\c(x_4)=101\\c(x_5)=1100\\c(x_6)=1101000
$