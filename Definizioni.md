Indice delle definizioni

- [Albero di Codifica]()
- [Campo di Galois]()
- [Codice]()
    - [Codice Non Singolare]()
    - [Codice Univocamente Decodificabile]()
    - [Codice Istantaneo]()
    - [Codice a Virgola]()
    - [Codici di Shannon]()
- [Entropia]()
    - [Entropia Relativa]()
- [Radice Primitiva]()
- [Sorgente]()

### Simboli usati
$$
X \text{ insieme finito dei simboli del messaggio}\\
x = (x_1,\dots,x_m)\in X^m\text{ messaggio}\\
m \text{ lunghezza del messaggio}\\
D \text{ insieme finito dei simboli della codifica}\\
c: X\to D^+\text{ funzione di codifica}\\
l_c(x_i)\text{ lunghezza della codifica del simbolo}\\
p(x_i)\text{ probabilità del simbolo nel messaggio}\\
C: X^+\to D^+\text{ funzione estesa di decodifica}
$$

### Albero di Codifica
Un albero di codifica è una rappresentazione grafica delle codifiche appartenenti all'immagine della funzione $c$.

### Campo di Galois
Un <font color=red>Campo di Galois</font> viene indicato con la dicitura $GF(p^n)$ dove $p$ è un numero primo e $n$ è un qualunque numero positivo. L'idea dei campi di Galois è di costruire un campo con $p^n$ elementi, partizionando l'insieme del polinomi di grado $n$ a coefficienti in $\Z_p$ usando come modulo un polinomio irriducibile di grado esattamente $n$.

### Codice
Un <font color=red>codice</font> è una funzione $c:X\to D^+$ che associa a un carattere del messaggio la sua codifica.

### Codice Non Singolare
Dato $c:X\to D^+$, diciamo che $c$ è <font color=red>non singolare</font> se $c$ è una funzione iniettiva.
$$c(x_1) = c(x_2)\implies x_1 = x_2$$

### Codice Univocamente Decodificabile
Se $C$ è non singolare, allora $c$ è <font color=red>univocamente decodificabile</font>
$$C \text{ non singolare}\implies c\text{ univocamente decodificabile}$$

### Codici Istantanei
Un codice è <font color=red>istantaneo</font> quando non esiste una parola nell'insieme $D$ dei simboli che è prefisso di un'altra parola.<br>
Definiamo provvisariamente l'insieme $\Bbb{C}$ come l'insieme delle codifiche della funzione $c$.<br>$\Bbb{C}\subseteq D^+$
$$\displaystyle\nexists\ x,y\in\Bbb{C},z\in D^+: y=x*z\implies c \text{ è istantaneo}$$

### Codici a Virgola
Tra i codici istantanei, esistono i <font color=red>codici a virgola</font>, dove ogni codifica termina con un carattere terminatore.

### Codici di Shannon
L'idea di Shannon è di minimizzare il valore atteso delle lunghezze avendo però un codice che rispetta la disuguaglianza di Kraft.
$$\begin{cases}\displaystyle
\min_{l_1,\dots,l_m}\sum_{i=1}^ml_ip_i&\text{Minimizzare Valore Atteso}\\
\displaystyle\sum_{i=1}^md^{-l_i}\le1&\text{Disuguaglianza di Kraft}
\end{cases}$$
Dato che voglio minimizzare il valore atteso, sceglierò il più piccolo $l_i$ possibile, ovvero
$$l_i = \lceil\log_d\frac1{p_i}\rceil$$

### Entropia
Sia una sorgente $<\Bbb{X}, P>$ con $\Bbb{X}=\{x_1,\dots,x_m\}$ e $P=\{p_1,\dots,p_m\}$. Per comodità, indichiamo con $p_i$ la probabilità con cui $x_i$ compare nel messaggio.<br>
Sia $X:\Bbb{X}\to\{a_1,\dots,a_m\}\subseteq\R$ una variabile aleatoria tale per cui $\Bbb{P}(X=a_i)=p_i$<br>
Chiamiamo <font color=red>Entropia</font> la funzione $$H_d(X)=\displaystyle\sum_{i=1}^mp_i\log_d{\frac1{p_i}}$$

### Entropia Relativa
L'entropia relativa è una misura di distanza (non simmetrica!) tra due variabili aleatorie $X$ e $Y$ entrambe definite sul dominio $S$ ma con due funzioni di probabilità diverse, che chiamiamo $p_X$ e $p_Y$.<br>
$$D_d(X||Y) = \displaystyle\sum_{s\in S}p_X(s)\log_d\frac{p_X(s)}{p_Y(s)}$$

### Radice Primitiva
In un campo, un elemento si dice <font color=red>Radice Primitiva</font> se quel numero elevato per tutti gli elementi del campo genera tutti gli elementi del campo, eccetto lo $0$.

### Sorgente
La <font color=red>sorgente</font> viene modellata attraverso la coppia $<X,P>$ dove $X$ è l'insieme dei simboli del messaggio e $P$ è lo spazio delle probabilità.<br>
Nella realtà, la probabilità che un simbolo compaia in un messaggio è influenzata dalla presenza dei simboli vicini (Ad esempio: in italiano, dopo la "$q$" c'è quasi sempre la "$u$".) Shannon non considera questo aspetto al fine di semplificare i calcoli, considerando i simboli tra loro indipendenti.
Considereremo dunque questa relazione
$$p(x)=p(x_1,\dots,x_n)=\displaystyle\prod_{i=1}^mp(x_i)$$