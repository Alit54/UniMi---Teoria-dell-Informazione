# Teoria dell'Informazione
<html>
    <div align=center>
    Simone Alessandro Casciaro<br>
    08 Ottobre 2024
    </div>
</html>

## Lezione 3: Disuguaglianza di Kraft
### Codici Istantanei
I codici istantanei, oltre alla possibilità di essere immediatamente decodificati, presentano un'altra proprietà.<br>
È possibile capire se esiste un codice istantaneo per un messaggio generato dalla sorgente, anche senza conoscere il codice. <font color=orange> NOTA:</font> Senza il codice, non è possibile determinare se il codice usato dalla sorgente è istantaneo, ma solo capire se può esisterne uno. Questa tecnica è più utile per capire se un codice NON è istantaneo, con operazioni meno onerose computazionalmente rispetto alla ricerca esaustiva.

Per fare ciò, è necessario il vettore $l$, che contiene la lunghezza delle codifiche delle parole del messaggio.
> Esempio<br>
$l=\begin{cases}
1&0\\
5&11110\\
4&1100\\
2&10
\end{cases}$<br>
Questo codice è istantaneo, quindi con $l=(1,5,4,2)$ è possibile costruire un codice istantaneo. Non è detto che quello usato dalla sorgente lo sia, ad esempio:<br>
$l=\begin{cases}
1&A\\
5&AAAAA\\
4&BBAA\\
2&BB
\end{cases}$<br>
che non è istantaneo.

### Albero di Codifica
Un albero di codifica è una rappresentazione grafica delle codifiche appartenenti all'immagine della funzione $c$.
> Esempio<br>
$
c(x_1) = 0\\
c(x_2) = 11110\\
c(x_3) = 1100\\
c(x_4) = 10\\
$
![Albero di Codifica](/img/kraft/generico.png)
### Disuguaglianza di Kraft
#### Ipotesi
Dati: 
- una sorgente $X=\{x_1,\dots,x_m\}$
- $d$ base del codice
- $m$ numero di elementi del messaggio
- $l_c = (l_1,\dots,l_m) > 0$ lunghezze delle codifiche dei simboli

#### Tesi
$$\exists \text{ codice istantaneo } c:X\to D^+ \text{t.c.}\ l_c(x_i)=l_i\ \forall i=1,\dots,m\\
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
$\boxed{\impliedby}$
Sempre per costruzione, partiamo dal vettore $l = (2, 1, 3, 3)$<br>
Controlliamo la sommatoria per vedere se rispettiamo le ipotesi della disuguaglianza. <br>
$\displaystyle\sum_{i=1}^md^{-l_i} = \frac{1}{2^2} + \frac{1}{2^1} + \frac{1}{2^3} + \frac{1}{2^3} = \frac14 + \frac12 + \frac18 + \frac18 = 1\le 1$<br>
Possiamo costruire un albero di codifica in modo tale che il codice che rappresenta sia istantaneo. Dato che si riesce a costruirlo, $\exists c$ codice istantaneo. $\square$

### Codici di Shannon
In seguito a tutto il discorso detto, abbiamo scoperto come i codici istantanei siano migliori di quelli univocamente decodificabili, che sono migliori dei non singolari.

# Inserire immagine Generale codici

Tuttavia, restringere l'insieme dei codici possibili comporta un innalzamento del minimo che noi stiamo cercando. Ricordiamo infatti, che noi vogliamo minimizzare il valore atteso delle lunghezze delle codifiche.<br>
L'idea di Shannon è di minimizzare il valore atteso delle lunghezze avendo però un codice che rispetta la disuguaglianza di Kraft.
$$\begin{cases}\displaystyle
\min_{l_1,\dots,l_m}\sum_{i=1}^ml_ip_i&\text{Minimizzare Valore Atteso}\\
\displaystyle\sum_{i=1}^md^{-l_i}\le1&\text{Disuguaglianza di Kraft}
\end{cases}$$

Per comodità, indichiamo con $p_i$ la probabilità della parola $x_i$ di lunghezza $l_i$.<br>
Per la disugaglianza di Kraft, sappiamo che $\displaystyle\sum_{i=1}^md^{-l_i}\le1$. Per il secondo assioma di Kolmogorov, $1=\displaystyle\sum_{i=1}^mp_i$.<br>
Dato che vogliamo che questa proprietà valga per la sommatoria, possiamo farla valere per ogni elemento (richiesta più stringente).<br>
$d^{-l_i} \le p_i\quad\forall i=1,\dots,m$ e dunque
$$l_i \ge \log_d{\frac1{p_i}}$$
Scegliamo cioè le lunghezze della codifica in base alla probabilità con cui un elemento del messaggio è presente nella sorgente.<br>
Dato che voglio minimizzare il valore atteso, sceglierò il più piccolo $l_i$ possibile, ovvero
$$l_i = \lceil\log_d\frac1{p_i}\rceil$$