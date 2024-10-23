# Teoria dell'Informazione
<html>
    <div align=center>
    Simone Alessandro Casciaro<br>
    22 Ottobre 2024
    </div>
</html>

## Lezione 7: Disuguaglianza di Kraft-McMillan
### Ripasso
![IST => UD](/img/sottoinsiemi/Istantanei.jpeg)
I codici Istantanei sono tutti Univocamente Decodificabili. Tuttavia, ci chiediamo se esiste un codice Univocamente Decodificabile e non Istantaneo che, magari, migliora il valore atteso delle lunghezze.

Il nostro obiettivo è trovare un codice tale che $\begin{cases}
\displaystyle\min_{l_1,\dots,l_m}\sum_{i=1}^mp_il_i&\min\Bbb E(l_c)\\
\displaystyle\sum_{i=1}^md^{-l_i}\le1&\text{Disuguaglianza di Kraft}
\end{cases}$
Si ricordano le seguenti nozioni:
$$
\begin{aligned}
c:\Bbb X\to D^+&\quad&c\text{ non singolare}\\
C_n:\Bbb{X}^n\to D^+&\quad&C_n\text{ non singolare}\\
C_n(x_1,\dots,x_n)=c(x_1)\dots c(x_n)\\
l_{C_n}(x_1,\dots,x_n) = \displaystyle\sum_{i=1}^n l_{c}(x_i)&\quad& n\ge1\\
l_{max}=\max_{i=1,\dots,m} l_c(x_i)
\end{aligned}
$$

### Teorema di Kraft-McMillan
Siano $l_1,\dots,l_m$ le lunghezze di un codice $d-$ario Univocamente Decodificabile per una sorgente $<\Bbb X, \Bbb P>$ di $m$ simboli $\iff\displaystyle\sum_{i=1}^md^{-l_i}\le1$
#### Dimostrazione
$\boxed{\impliedby}$
Per la [disuguaglianza di Kraft](https://github.com/Alit54/UniMi---Teoria-dell-Informazione/blob/main/pdf/Lez03.pdf), $\displaystyle\sum_{i=1}^md^{-l_i}\le1\implies\exist c$ istantaneo con lunghezze $l_1,\dots,l_m$. Ma un codice istantaneo è sempre univocamente decodificabile.
$\boxed{\implies}$
Considero un codice $c$ univocamente decodificabile e calcolo $\displaystyle\Bigg(\sum_{x\in\Bbb X}d^{-l_c(x)}\Bigg)^n$
> Se $\boxed{n=2}$<br>
$\displaystyle\Bigg(\sum_{i=1}^ma_i\Bigg)^2 = \sum_{i=1}^ma_i*\sum_{j=1}^ma_j = \sum_{i=1}^m\sum_{j=1}^ma_ia_j$

Nel caso generale,
$$
\begin{aligned}
\tag{1}
\Bigg(\sum_{x\in\Bbb X}d^{-l_c(x)}\Bigg)^n&=\sum_{x_1\in\Bbb X}\dots\sum_{x_n\in\Bbb X} d^{-l_c(x_1)}\dots d^{-l_c(x_n)}\\
&=\sum_{x_1\in\Bbb X}\dots\sum_{x_n\in\Bbb X} d^{-\displaystyle\sum_{i=1}^nl_c(x_i)}\\
&=\sum_{(x_1,\dots,x_n)\in\Bbb X^n}d^{-l_{C_n}(x_1,\dots,x_n)}&\text{Passiamo alla sorgente }<\Bbb X^n, \Bbb P_n>
\end{aligned}
$$
Analizzando $l_{C_n}$, scopriamo che:
$n\le l_{C_n}(x_1,\dots,x_n)$ perché se ad ogni $x_i$ associo un solo simbolo nella codifica, abbiamo $\displaystyle\sum_{i=1}^n1 =n$\\
$l_{C_n}(x_1,\dots,x_n)\le n*l_{max}$ perché se ad ogni $x_i$ associo la lunghezza massima della codifica, abbiamo $\displaystyle\sum_{i=1}^nl_{max} =n*l_{max}$
Quindi $$n\le l_{C_n}(x_1,\dots,x_n)\le n*l_{max}$$

Consideriamo $\Bbb X^n$ e lo partizioniamo in $k$ elementi a $2$ a $2$ disgiunti secondo la lunghezza delle codifiche dato da $C_n$
Chiamiamo ogni partizione $\Bbb X^n_k$
$\Bbb X^n_k = \{(x_1,\dots,x_n)\in \Bbb X^n:l_{C_n}(x_1,\dots,x_n)=k\}$
Data la premessa precedente, si ha che se $k<n$ oppure se $k>n*l_{max}$ allora $\Bbb X^n_k=\empty$
Gli insiemi $\Bbb X^n_k$ sono tali che:

- $\Bbb X^n_i\cap \Bbb X^n_j=\empty\quad\forall i\ne j$
- $\displaystyle\bigcap_{k=n}^{n*l_{max}}\Bbb X^n_k=\Bbb X^n$
- $\Bbb X^n_k\subseteq \Bbb X^n$
![Partizione](/img/kraft-mcmillan/partizione.PNG)

Riprendendo il punto $1$, si ha che
$$
\begin{aligned}
\tag{1.1}
\Bigg(\sum_{x\in\Bbb X}d^{-l_c(x)}\Bigg)^n&=\sum_{(x_1,\dots,x_n)\in\Bbb X^n}d^{-l_{C_n}(x_1,\dots,x_n)}\\
&=\sum_{k=1}^{nl_{max}}\sum_{(x_1,\dots,x_n)\in\Bbb X^n_k}d^{-l_{C_n}(x_1,\dots,x_n)}\\
&=\sum_{k=1}^{nl_{max}}\sum_{(x_1,\dots,x_n)\in\Bbb X^n_k}d^{-k}\\
&=\sum_{k=1}^{nl_{max}}|\Bbb X^n_k|d^{-k}
\end{aligned}
$$
Dato che $C_n$ è una funzione non singolare (e quindi iniettiva), la cardinalità del dominio è minore di quella del codominio. Quindi $|\Bbb X^n_k|\le|D^k|$ Possiamo dunque maggiorare la sommatoria precedente.
$$
\begin{aligned}
\tag{1.2}
\Bigg(\sum_{x\in\Bbb X}d^{-l_c(x)}\Bigg)^n&=\sum_{k=n}^{nl_{max}}|\Bbb X^n_k|d^{-k}\\
&\le\sum_{k=1}^{nl_{max}}|D^k|d^{-k}\\
&=\sum_{k=1}^{nl_{max}}d^kd^{-k}\\
&=\sum_{k=1}^{nl_{max}}1\\
&=n*l_{max}
\end{aligned}
$$
Abbiamo dunque dimostrato che $$\tag{1.2.1}\Bigg(\sum_{x\in\Bbb X}d^{-l_c(x)}\Bigg)^n\le n*l_{max}$$
Facendo uno studio di funzione e rinominando $\displaystyle\sum_{x\in\Bbb X}d^{-l_c(x)} = M$ 
![Studio di Funzione](/img/kraft-mcmillan/studio.PNG)
notiamo che la disuguaglianza al punto $1.2.1$ è rispettata se e solo se $M\le1$, quindi abbiamo dimostrato che $$\sum_{x\in\Bbb X}d^{-l_c(x)}\le1\quad\square$$

### <font color=00cc99>Esercizi</font>
1. Data una codifica e 3 possibili spazi di probabilità, trovare il migliore supponendo che vogliamo minimizzare il valore atteso delle lunghezze.

| | $C_B$ | $p_1$ | $p_2$ | $p_3$
|---|---|---|---|---|
| $x_1$ | $000$ | $0.2$ | $0.4$ | $0.1$
| $x_2$ | $001$ | $0.2$ | $0.2$ | $0.1$
| $x_3$ | $01$ | $0.2$ | $0.2$ | $0.2$
| $x_4$ | $110$ | $0.2$ | $0.1$ | $0.4$ 
| $x_5$ | $111$ | $0.2$ | $0.1$ | $0.2$

Calcolando i 3 valori attesi, si ha che:
$\Bbb{E}(l_1) = 0.2*3+0.2*3+0.2*2+0.2*3+0.2*3=2.8$
$\Bbb{E}(l_2) = 0.4*3+0.2*3+0.2*2+0.1*3+0.1*3=2.8$
$\Bbb{E}(l_3) = 0.1*3+0.1*3+0.2*2+0.4*3+0.2*3=2.8$
Le 3 probabilità sono dunque equivalenti. Tuttavia, per nessuna delle 3 probabilità il codice è ottimale.

2. Data una sorgente $\Bbb X=\{a_1,\dots,a_8,a_9,\dots,a_{12}\}$ e $\Bbb P(a_i)=\begin{cases}0.1&i=1,\dots,8\\0.05&i=9,\dots,12\end{cases}$
Dato $d=5$, trovare un codice istantaneo e, se possibile, ottimale.
Usando l'algoritmo di Huffman, notiamo che il codice restituito non è ottimale, contrariamente a quanto abbiamo studiato nella lezione precedente. Infatti, il codice restituito è il seguente:
> $
c(a_1)=1\\
c(a_2)=2\\
c(a_3)=31\\
c(a_4)=32\\
c(a_5)=33\\
c(a_6)=34\\
c(a_7)=35\\
c(a_8)=41\\
c(a_9)=42\\
c(a_{10})=43\\
c(a_{11})=44\\
c(a_{12})=45\\
$ Non va bene, perché il sottoalbero del simbolo $5$ non viene coperto.

Si può risolvere introducendo nell'algoritmo di Huffman un numero di simboli "Dummy" con probabilità $0$, per far sì che l'algoritmo possa restituire un codice istantaneo ottimale. Il numero di simboli dummy è dato dalla seguente espressione
$$n+q\equiv 1\mod{d-1}$$ dove $n=|\Bbb X|$ e $q$ è il numero di simboli dummy. Con questi accorgimenti, il codice restituito è:
> $
c(a_1)=1\\
c(a_2)=2\\
c(a_3)=3\\
c(a_4)=41\\
c(a_5)=42\\
c(a_6)=43\\
c(a_7)=44\\
c(a_8)=45\\
c(a_9)=51\\
c(a_{10})=52\\
c(a_{11})=53\\
c(a_{12})=54\\
$