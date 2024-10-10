# Teoremi e Dimostrazioni


Indice dei Teoremi e Dimostrazioni
- [Codice Istantaneo $\implies$ Codice Univocamente Decodificabile]()
- [Disuguaglianza di Kraft]()

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