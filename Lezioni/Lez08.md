# Teoria dell'Informazione
<html>
    <div align=center>
    Simone Alessandro Casciaro<br>
    25 Ottobre 2024
    </div>
</html>

## Lezione 8: Derivati dell'Entropia
<font color=orange> Nota</font>: in questa lezione (e molto probabilmente anche fino alla fine del corso), considereremo $\boxed{d=2}$. Dunque, si eviterà di indicare tale dato nelle definizioni delle entropie e dei logaritmi. In ogni caso, tutte le dimostrazioni presenti in questa lezione sono valide $\forall d>1$.
### Significato pratico dell'Entropia
Nella [Lezione 4](/pdf/Lez04.pdf) abbiamo parlato dell'<font color=red>Entropia</font> come indice di eterogeneità, ma cosa rappresenta l'entropia?
Nella <code>Teoria dell'Informazione</code>, L'<font color=#ff00ff>Entropia</font> $H(X)$ rappresenta la quantità di informazione da mandare per comunicare l'evento $X$ e, dunque, il numero medio di simboli da spedire sul canale.
Parlando dell'<font color=#ff00ff>Entropia Congiunta</font>, $H(X,Y)$ rappresenta la quantità di informazione da mandare sul canale per comunicare sia $X$ sia $Y$.
Infine, l'<font color = #ff00ff>Entropia Condizionata</font> $H(Y|X)$ rappresenta la quantità di informazione da mandare per comunicare $Y$ sapendo che ho già mandato $X$ in precedenza.

Intuitivamente, se posso esprimere $Y$ come funzione di $X$, allora non ha senso mandare $Y$ in quanto possiamo ricavarlo da $X$. Infatti, si ha questa relazione:
$$H(Y|X)=0\iff Y=g(X)$$

><font color=#00CC99>Esempio</font>
$\Bbb X=\left\{-1, 0, 1\right\}$<br>
Indichiamo con $X$ una variabile aleatoria e $Y=X^2$
$H(Y|X)=0$ perché, una volta spedito $X$ sul canale, possiamo conoscere anche il risultato della variabile $Y$.
Diversamente, $H(X|Y)\ne0$ perché aver spedito $Y$ sul canale non sempre è sufficiente a sapere il valore di $X$. Ad esempio, se $Y=1$, non sappiamo se $X=1$ oppure $X=-1$ e dunque abbiamo bisogno di un'informazione aggiuntiva.

### Definizione di Entropia Condizionata
Ricordando che $\displaystyle p(x)=\sum_{y\in Y}p(x,y)$ e che $\displaystyle p(y|x)=\frac{p(x,y)}{p(x)}$, indichiamo l'entropia condizionata come segue:
$$
\begin{aligned}
H(Y|X) &= \sum_{x\in\Bbb X} p(x)H(Y|X=x)\\
&=\sum_{x\in \Bbb X}p(x)\sum_{y\in\Bbb Y}p(y|x)\log\frac1{p(y|x)}\\
&=\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}p(x)p(y|x)\log\frac1{p(y|x)}\\
&=\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}p(x,y)\log\frac1{p(y|x)}
\end{aligned}
$$
Quindi,
$$H(Y|X) = \sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}p(x,y)\log\frac1{p(y|x)}$$

### Teorema: Chain Rule per l'Entropia
#### Tesi
$$H(X,Y) = H(X)+H(Y|X)$$
#### Dimostrazione
$$
\begin{aligned}
H(X,Y)&=-\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}p(x,y)\log p(x,y)\\
&=-\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}p(x,y)\log \left(p(x)*p(y|x)\right)\\
&=-\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}p(x,y)\left[\log p(x) +\log p(y|x)\right]\\
&=-\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}p(x,y)\log p(x) - \sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}p(x,y)\log p(y|x)\\
&=-\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}p(x,y)\log p(x)+ H(Y|X)\\
&=-\sum_{x\in\Bbb X}p(x)\log p(x) + H(Y|X)\\
&=H(X) + H(Y|X)
\end{aligned}
$$
<font color=orange>Nota</font>: Il risultato vale anche se condizioniamo il tutto a una terza variabile $Z$:
$$H(X,Y|Z)=H(X|Z)+H(Y|X,Z)$$

### Informazione Mutua
L'<font color=red>informazione mutua</font> è una misura che indica quanta informazione rilascia $Y$ rispetto a $X$.
$$I(X,Y)=\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}p(x,y)\log\frac{p(x,y)}{p(x)p(y)}$$
L'informazione mutua è sempre $\ge0$.
Inoltre, $$I(X,Y)=H(X)-H(X|Y)$$
#### Dimostrazione
$$\begin{aligned}
I(X,Y)&=\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}p(x,y)\log\frac{p(x,y)}{p(x)p(y)}\\
&=\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}p(x,y)\log\frac{p(y)p(x|y)}{p(x)p(y)}\\
&=\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}p(x,y)\log\frac{p(x|y)}{p(x)}\\
&=\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}p(x,y)\left[\log p(x|y)- \log p(x)\right]\\
&=\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}p(x,y)\log\frac1{p(x)}+\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}p(x,y)\log p(x|y)\\
&=\sum_{x\in\Bbb X}p(x)\log\frac1{p(x)}-\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}p(x,y)\log \frac1{p(x|y)}\\
&=H(X)-H(X|Y)
\end{aligned}$$

Ricapitolando le informazioni viste fino ad ora, si hanno le seguenti relazioni
$$
I(X,Y)=H(X)+H(Y)-H(X,Y)\\
H(X)\ge H(X|Y)\\
H(Y)\ge H(Y|X)\\
H(X)=H(X|Y)+I(X,Y)\\
H(X,Y)=H(X)+H(Y)-I(X,Y)
$$
![Diagramma di Venn Entropia](/img/informazione%20mutua.png)

### Informazione Mutua Condizionata
$$I(X,Y|Z)=\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}\sum_{z\in\Bbb Z} p(x,y,z)\log\frac{p(x,y,z)}{p(x|z)p(y|z)}$$

### Teorema: Data Processing Inequality
Supponiamo di avere una sorgente $<\Bbb X, \Bbb P>$ e di spedire un messaggio sul canale, indicato con $X$. Se il canale è privo di rumore, allora il ricevente riceve esattamente $X$.
$$X \overbrace{\longrightarrow}^\text{Canale senza Rumore} X$$
Tuttavia, se invece il canale presenta del rumore, allora il messaggio ricevuto è $Y$.
Supponiamo di voler migliorare $Y$ tramite un algoritmo per ripulire il rumore, in modo tale da ricevere un nuovo messaggio $Z$. 
$$X \overbrace{\longrightarrow}^\text{Canale con Rumore} Y \overbrace{\longrightarrow}^\text{Algoritmo per ripulire Rumore} Z$$
Ci chiediamo che relazione intercorre tra $I(X,Z)$ e $I(X,Y)$, ovvero se è possibile aumentare l'informazione rispetto a $X$ usando $Z$ al posto di $Y$.

#### Ipotesi
Siano $X,Y,Z$ variabili aleatorie con codominio finito per la sorgente $<\Bbb X, \Bbb P>$ con<br> $p(x,y,z)$ tale che $p(x,z|y)=p(x|y)p(z|y)\quad\forall x,y,z$ (Ovvero $X, Z$ sono indipendenti dato $Y$)
#### Tesi
$$I(X,Y)\ge I(X,Z)$$
#### Dimostrazione
$$\begin{aligned}
I(X,Y,Z)&=\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}\sum_{z\in\Bbb Z} p(x,y,z)\log\frac{p(x,y,z)}{p(x)p(y,z)}\\
&=\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}\sum_{z\in\Bbb Z} p(x,y,z)\log\frac{p(y|x,z)p(x,z)}{p(x)p(y,z)}\\
&=\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}\sum_{z\in\Bbb Z} p(x,y,z)\log\frac{p(y|x,z)p(x,z)}{p(x)p(y|z)p(z)}\\
&=\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}\sum_{z\in\Bbb Z} p(x,y,z)\left[\log\frac{p(x,z)}{p(x)p(z)}+\log\frac{p(y|x,z)}{p(y|z)}\right]\\
&=\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}\sum_{z\in\Bbb Z} p(x,y,z)\log\frac{p(x,z)}{p(x)p(z)}+\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}\sum_{z\in\Bbb Z} p(x,y,z)\log\frac{p(y|x,z)}{p(y|z)}\\
&=\sum_{x\in\Bbb X}\sum_{z\in\Bbb Z} p(x,z)\log\frac{p(x,z)}{p(x)p(z)}+\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}\sum_{z\in\Bbb Z} p(x,y,z)\log\frac{p(y|x,z)}{p(y|z)}\\
&=I(X,Z)+\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}\sum_{z\in\Bbb Z} p(x,y,z)\log\left(\frac{p(y|x,z)}{p(y|z)}\frac{p(x|z)}{p(x|z)}\right)\\
&=I(X,Z)+\sum_{x\in\Bbb X}\sum_{y\in\Bbb Y}\sum_{z\in\Bbb Z} p(x,y,z)\log\frac{p(x,y|z)}{p(y|z)p(x|z)}\\
&=I(X,Z)+I(X,Y|Z)
\end{aligned}$$
Dunque,$$\tag{1}I(X,Y,Z)=I(X,Z)=I(X,Y|Z)$$
Tuttavia, se al posto di condizionare su $Z$ lo avessimo fatto su $Y$, avremmo ottenuto $$\tag{2}I(X,Y,Z)=I(X,Y)+I(X,Z|Y)$$
Possiamo eguagliare le equazioni $1$ e $2$, ottenendo
$$I(X,Z)+I(X,Y|Z)=I(X,Y)+I(X,Z|Y)$$
Dato che $X$ e $Z$ sono indipendenti se condizionate a $Y$, $I(X,Z|Y)=0$ e dato che l'informazione mutua è sempre positiva, abbiamo dimostrato che $$I(X,Y)\ge I(X,Z)$$
e quindi non è possibile aumentare l'informazione rispetto a quello effettivamente ricevuto dal canale.