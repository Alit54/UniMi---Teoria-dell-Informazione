# Teoria dell'Informazione
<html>
    <div align=center>
    Simone Alessandro Casciaro<br>
    15 Novembre 2024
    </div>
</html>

## Lezione 11: Esercizi sul Canale
In questa lezione, non sarà presente alcuna nozione teorica. Ci focalizzeremo sull'eseguire alcuni esercizi per calcolare la capacità del canale, come definito nella [Lezione 10](/pdf/Lez10.pdf).
$$C=\begin{cases}\displaystyle\max_{p(x)}I(X,Y)\\\displaystyle\max_{p(x)}H(X)-H(X|Y)\\\displaystyle\max_{p(x)}H(Y)-H(Y|X)\end{cases}$$

### Esercizi
> <font color="00cc99">Esercizio 1</font>
Sia $\Bbb X=\{0,1\}$ e $\Bbb Y=\{0,1,2,3\}$ e sia la matrice di canale $$
\Bbb P = \begin{array}{c|cccc}
     & 0 & 1 & 2 & 3 \\
    \hline
    0 & 0.5 & 0.5 & 0 & 0 \\
    1 & 0 & 0 & 0.5 & 0.5 
\end{array}
$$ Calcolare $C$<br>
Dalla matrice $\Bbb P$, notiamo che una volta ricevuto il valore di $Y$, è possibile ricavare direttamente quello di $X$. Dunque, $H(X|Y)=0$.
$$\displaystyle C=\max_{p(x)}H(X)-H(X|Y)=\max_{p(x)}H(X)$$ Dato che $X$ è una variabile aleatoria bernoulliana $\left(\Bbb X=\{0,1\}\right)$, l'entropia viene massimizzata quando $p=\frac12$ e, in quel caso, $H(X)=1$.
Dunque, $$\boxed{C=1}$$

> <font color="00cc99">Esercizio 2</font>
Sia $\Bbb X=\{0,1,2\}$ e $\Bbb Y=\{0,1,2\}$ e sia la matrice di canale $$
\Bbb P = \begin{array}{c|ccc}
     & 0 & 1 & 2 \\
    \hline
    0 & 0.5 & 0.5 & 0 \\
    1 & 0  & 0.5 & 0.5 \\
    2 & 0.5 & 0 & 0.5
\end{array}
$$ Calcolare $C$<br>
Tramite la matrice di canale $\Bbb P$, ci accorgiamo che indipendentemente dal valore che assume $X$, abbiamo due possibili valori per $Y$, entrambi con probabilità $\frac12$. Dunque, $H(Y|X=i)=H(Y|X=j)\quad\forall i,j$
Calcoliamo, ad esempio, $H(Y|X=0)$
$$H(Y|X=0)=\displaystyle\sum_{y\in\Bbb Y}p(y|X=0)\log\frac1{p(y|X=0)} = \frac12\log2+\frac12\log2+0=1$$ Possiamo ora calcolare $H(Y|X)$
$$H(Y|X)=\displaystyle\sum_{x\in\Bbb X}p(x)*H(Y|X=x) = \sum_{x\in\Bbb X}p(x)*1 = 1$$ $C=\displaystyle\max_{p(x)}H(Y)-H(Y|X) = \max_{p(x)}H(Y)-1$
Massimizzare $H(Y)-1$ è la stessa cosa di massimizzare $H(Y)$
Come nell'esercizio $1$, l'entropia viene massimizzata quando $Y$ assume una distribuzione uniforme. Tuttavia, non possiamo scegliere la distribuzione di probabilità di $Y$, ma solo quella di $X$. Proviamo, per intuito, a scegliere $X$ con una distribuzione di probabilità uniforme e calcoliamo $p(y_j)$ $$\begin{aligned}p(y_j)&=\displaystyle\sum_{y\in\Bbb Y}p(x_i, y_j) \\&= \sum_{y\in\Bbb Y}p(y_j|x_i)p(x_i)\\&=\sum_{y\in\Bbb Y}p(y_j|x_i)*\frac13=\frac12*\frac13+\frac12*\frac13+0*\frac13\\&=\frac13\end{aligned}$$ Notiamo che $p(y_j)$ è un valore costante indipendente da $j$, dunque $Y$ ha una distribuzione uniforme.
$$H(Y)=\sum_{y\in\Bbb Y}p(y)\log\frac1{p(y)}=\sum_{y\in\Bbb Y}\frac13\log3=3\left(\frac13\log3\right) = \log3$$ Dunque, $$\boxed{C=\log3-1}$$

> <font color="00cc99">Esercizio 3</font>
Sia $\Bbb X=\{0,1\}$ e $\Bbb Y=\{0,1\}$ e sia la matrice di canale $$
\Bbb P = \begin{array}{c|cc}
     & 0 & 1 \\
    \hline
    0 & 1-\alpha & \alpha \\
    1 & \alpha  & 1-\alpha
\end{array}
$$
Calcolare $C$<br>
Cominciamo dal calcolare $H(Y|X)$
$$\begin{aligned}H(Y|X=0)&=\Bbb P(y=0|x=0)\log\frac1{\Bbb P(y=0|x=0)}+\Bbb P(y=1|x=0)\log\frac1{\Bbb P(y=1|x=0)}\\&=(1-\alpha)\log\frac1{1-\alpha}+\alpha\log\frac1\alpha\\&=H(B)\end{aligned}$$ $$\begin{aligned}H(Y|X=1)&=\Bbb P(y=0|x=1)\log\frac1{\Bbb P(y=0|x=1)}+\Bbb P(y=1|x=1)\log\frac1{\Bbb P(y=1|x=1)}\\&=\alpha\log\frac1\alpha+(1-\alpha)\log\frac1{1-\alpha}\\&=H(B)\end{aligned}$$ In entrambi i casi, otteniamo l'entropia di una variabile aleatoria bernoulliana $B$ di parametro $\alpha$.
$$\begin{aligned}H(Y|X)&=\Bbb P(x=0)H(Y|X=0)+\Bbb P(x=1)H(Y|X=1)\\&=p*H(B)+(1-p)H(B)\\&=H(B)+(p+1-p)\\&=H(B)\end{aligned}$$ Come nell'esercizio precedente, supponiamo di avere $X$ uniforme e vediamo se otteniamo una distribuzione uniforme per $Y$
$$\Bbb P(Y=0)=(1-\alpha)\Bbb P(X=0)+\alpha*\Bbb P(X=1)=(1-\alpha)\frac12+\alpha*\frac12=\frac12$$
$$\Bbb P(Y=1)=\alpha*\Bbb P(X=0)+(1-\alpha)*\Bbb P(X=1)=\alpha*\frac12+(1-\alpha)\frac12=\frac12$$ Dato che le due probabilità sono uguali indipendentemente da $\alpha$, $Y$ è uniforme e dunque, essendo una bernoulliana, ha entropia uguale a $1$.
Ricapitolando, $C=\displaystyle\max_{p(x)}H(Y)-H(Y|X)$ e dunque
$$\boxed{C=1-H(B)}$$

> <font color="00cc99">Esercizio 4</font>
Sia $\Bbb X=\{0,1\}$ e $\Bbb Y=\{0,1, e\}$ e sia la matrice di canale $$
\Bbb P = \begin{array}{c|ccc}
     & 0 & 1 & e\\
    \hline
    0 & 1-\alpha & 0 & \alpha \\
    1 & 0  & 1-\alpha & \alpha
\end{array}
$$ Calcolare $C$<br>
Calcolando $H(Y|X)$, ci accorgiamo che siamo nella stessa situazione dell'esercizio precedente.
Dunque $H(Y|X)=H(B)$ dove $B$ è una variabile aleatoria bernoulliana di parametro $\alpha$. 
Consideriamo una nuova variabile aleatoria bernoulliana $Z$ definita in questo modo: $$Z=\begin{cases}1&Y=e\\0&Y\ne e\end{cases}$$ Sfruttando la definizione di Entropia Congiunta, sappiamo che $$\begin{cases}H(Y,Z)=H(Y)+H(Z|Y)\\H(Y,Z)=H(Z)+H(Y|Z)\end{cases}\implies H(Y) = H(Z) + H(Y|Z) - H(Z|Y)$$ $Z$ è dipendente da $Y$, dunque $H(Z|Y)=0$
Vogliamo calcolare $H(Z)$, ma prima ci serve calcolare $\Bbb P(Z=1)$ e $\Bbb P(Z=1)$
$$\begin{aligned}\Bbb P(Z=1)&=\Bbb P(Z=1|X=0)\Bbb P(X=0)+ \Bbb P(Z=1|X=1)\Bbb P(X=1)\\&=\alpha p + \alpha (1-p) \\&= \alpha(p+1-p)\\&=\alpha \end{aligned}$$ Di conseguenza, $\Bbb P(Z=0)=1-\alpha$ 
Ora calcoliamo $H(Z)$ $$\begin{aligned}H(Z)&=\Bbb P(Z=0)\log\frac1{\Bbb P(Z=0)}+\Bbb P(Z=1)\log\frac1{\Bbb P(Z=1)}\\&=\alpha\log\frac1\alpha+(1-\alpha)\log\frac1{1-\alpha}\\&=H(B)\end{aligned}$$ Infine, calcoliamo $H(Y|Z)$ $$\begin{aligned}H(Y|Z)&=H(Y|Z=0)\Bbb P(Z=0)+ H(Y|Z=1)\Bbb P(Z=1)\\&=H(X)*(1-\alpha)+0*\alpha \\&= H(X)*(1-\alpha)\end{aligned}$$ Quando $Z=0$, $Y$ si comporta esattamente come $X$, per questo $H(Y|Z=0)=H(X)$
Mettendo insieme tutti i pezzi, $$C=\displaystyle\max_{p(x)} H(B)+H(X)*(1-\alpha)-H(B) = \max_{p(x)} H(X)*(1-\alpha)$$
L'entropia massima per $X$, dato che è bernoulliana, è $1$ quando $p=\frac12$, dunque $$\boxed{C=1-\alpha}$$