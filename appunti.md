# Teoria dell'Informazione
<html>
    <div align=center>
    Simone Alessandro Casciaro<br>
    Ottobre 2024 - Dicembre 2024
    </div>
</html>

### Storia
La Teoria dell'Informazione e della Trasmissione fa riferimento al seguente schema.
![Schema di riferimento della Teoria dell'Informazione e della Trasmissione](/img/Schema.png)
Da questo schema, notiamo che:
- La fase della Sorgente viene chiamata <code>Source Coding</code>
- La fase di Codifica e di Decodifica fanno riferimento alla seconda parte del corso, chiamata <code>Teoria della Trasmissione</code>
- Il Rumore sarà un'entità esterna di cui terremo conto nell'utilizzo del Canale, ma che non approfondiremo troppo in questo corso.

### Protagonisti della storia della Teoria dell'Informazione

Ci si pone l'obbiettivo di spedire, attraverso un canale, più informazione possibile da una sorgente a una destinazione.<br>
Gli studiosi che si sono posti il problema sono <b>Claude Shannon</b> e <b>Andrej Kolmogorov</b>.<br>
Shannon si occupa di studiare il problema nel suo caso medio, a livello statistico, ignorando dunque l'applicazione al caso reale, che è invece studio di Kolmogorov.<br>
A loro si aggiunge anche <b>Richard Hamming</b>, che ha studiato un algoritmo per correggere gli errori, dando vinta al primo <font color="red">Codice di Rilevazione e Correzione degli errori</font>. Il corso di <code>Teoria dell'Informazione</code> si baserà sugli studi di Shannon.

Per inviare un messaggio, sono importanti due operazioni:

- <font color="green">Compressione</font> -> Trovare pattern comuni in modo da inviare informazioni ripetute una volta sola
- <font color="green">Aggiungere Ridondanza</font> -> Si ripetono le informazioni rilevanti per poterle, eventualmente, correggere in fase di decodifica.

Studieremo i due teoremi di Shannon, in due punti diversi dello schema soprastante:

- 1° Teorema di Shannon, fase di Source Coding: si cerca di massimizzare la compressione
- 2° Teorema di Shannon, fase di uso del Canale: si cerca di minimizzare il numero di errori

Shannon, per modellare il canale, usa una matrice stocastica che indica la probabilità di ricevere un determinato carattere dopo averne inviato un altro sul canale.

> Esempio di Matrice Stocastica<br>

| IN/OUT | a | b | c | d | e
|---|---|---|---|---|---|
| a | 0.7 | 0 | 0.1 | 0.1 | 0.1
| b | 0 | 1 | 0 | 0 | 0
| c | 0.4 | 0 | 0.5 | 0 | 0.1
| d | 0 | 0.3 | 0.1 | 0.6 | 0
| e | 0.2 | 0 | 0.1 | 0 | 0.7

### Quali sono i messaggi che contengono più informazione?<br>
Supponiamo di disporre di 2 monete, una truccata e l'altra no. Lanciandole entrambe 5 volte, i risultati sono i seguenti: TCCTC, TTTTT. Quale di questi due lanci contiene più informazione? La risposta è: la moneta non truccata, perché quando effettueremo un sesto lancio, per entrambe le monete, sarà più facile prevedere il risultato della moneta truccata, rispetto a quella non truccata.<br>
In generale, laddove c'è meno <font color="red">entropia</font> nel messaggio, c'è anche meno informazione e viceversa.

### L'idea di Shannon
L'idea di Shannon prevede:

- <font color = green>Massimizzare l'informazione</font> $\forall$ utilizzo del canale. (NOTA: è importante specificare l'utilizzo perché stiamo specificando non solo quanta informazione deve essere inserita nel canale, ma anche il lasso di tempo in cui questa deve avvenire). Questa fase riguarda la fase di <font color="red">Source Coding</font>
- <font color = green>Minimizzare il numero di errori</font>. Dipenderà dal rumore e riguarda la fase di <font color = red>Codifica</font> e del <font color=red>Canale</font>.

### Definizioni Importanti
Definiamo:
$$
X \text{ insieme finito dei simboli del messaggio}\\
x = (x_1,\dots,x_m)\in X^m\text{ messaggio}\\
m \text{ lunghezza del messaggio}\\
D \text{ insieme finito dei simboli della codifica}\\
c: X\to D^+\text{ funzione di codifica}\\
l_c(x_i)\text{ lunghezza della codifica del simbolo}\\
p(x_i)\text{ probabilità del simbolo nel messaggio}
$$

> Esempio<br>
$X=\{\heartsuit,\diamondsuit,\clubsuit,\spadesuit\}\\d=2\\c:X\to\{0,1\}^+$<br>
Delle possibili scelte di $c$ sono:<br>
$c(\heartsuit)=0\quad\quad c(\diamondsuit)=010\quad c(\clubsuit)=01\quad c(\spadesuit)=10\\
c(\heartsuit)=0\quad\quad c(\diamondsuit)=1\quad\quad c(\clubsuit)=01\quad c(\spadesuit)=10\\
c(\heartsuit)=00\quad\ \  c(\diamondsuit)=01\ \ \quad c(\clubsuit)=10\quad c(\spadesuit)=11\\
c(\heartsuit)=0\qquad c(\diamondsuit)=00\ \ \quad c(\clubsuit)=000\ \  c(\spadesuit)=0000$

### Modellizzazione della Sorgente
La sorgente viene modellata attraverso la coppia $<X,P>$ dove $X$ è l'insieme dei simboli del messaggio e $P$ è lo spazio delle probabilità.<br>
Nella realtà, la probabilità che un simbolo compaia in un messaggio è influenzata dalla presenza dei simboli vicini (Ad esempio: in italiano, dopo la "$q$" c'è quasi sempre la "$u$".) Shannon non considera questo aspetto al fine di semplificare i calcoli, considerando i simboli tra loro indipendenti.
Considereremo dunque questa relazione
$$p(x)=p(x_1,\dots,x_n)=\displaystyle\prod_{i=1}^mp(x_i)$$

Data una sorgente $<X,P>$, dato $d>1$ e data $c:X\to D^+$ vogliamo che:
$$\displaystyle\Bbb{E}(l_c)=\sum_{x\in X}l_c(x)p(x)\text{ sia minimo}$$

### Codice Non Singolare
Dato $c:X\to D^+$, diciamo che $c$ è non singolare se $c$ è una funzione iniettiva.
$$c(x_1) = c(x_2)\implies x_1 = x_2$$
Codici non singolari $\subset$ Codici
![I Codici non singolari sono un sottoinsieme dei Codici](/img/sottoinsiemi/NS.jpeg)

### Definizione
Dato $c: X\to D^+$, consideriamo un'estensione di $c$ a una concatenazione di elementi di $X$ e la chiamiamo $$C:X^+\to D^+$$
> Esempio<br>
Considerando la prima funzione $c$ definita nel precedente esempio, abbiamo:
$01001\begin{cases}C(\heartsuit,\spadesuit,\clubsuit)\\ C(\diamondsuit, \clubsuit)\\ C(\clubsuit, \heartsuit, \clubsuit)\end{cases}$<br>
La funzione $C$ non è "non singolare"

Notiamo quindi che se $c$ è non singolare, non è detto $C$ lo sia. Questo rende la decodifica impossibile (o meglio, ambigua).

Vogliamo che anche $C$ sia non singolare.
### Codice Univocamente Decodificabile
Se $C$ è non singolare, allora $c$ è univocamente decodificabile
$$C \text{ non singolare}\implies c\text{ univocamente decodificabile}$$


Come si capisce se un codice è univocamente decodificabile? Esiste un algoritmo (Sardinas-Patterson) che ermette di stabilirlo.<br>
La Complessità Computazionale di questo algoritmo è $O(m*L)$ dove $m=|X|$ e $L=\displaystyle\sum_{x\in X}l_c(x)$<br>
Codice Univocamente Decodificabile $\subset$ Codice Non Singolare
![I Codici non singolari sono un sottoinsieme dei Codici](/img/sottoinsiemi/UD.jpeg)

> Esempio<br>
Consideriamo $c(\heartsuit)=10\quad c(\diamondsuit)=00\quad c(\clubsuit)=11\quad c(\spadesuit)=110$<br>
Questo codice è univocamente decodificabile. Tuttavia, se dobbiamo decodificare la stringa $110...0$, il numero di $0$ influenza la decodifica ($\clubsuit,\diamondsuit,\diamondsuit,\diamondsuit,...$ oppure $\spadesuit,\diamondsuit,\diamondsuit,\diamondsuit,...$). Questo obbliga ad aspettare la fine della stringa per decodificarla, creando problemi ad esempio in caso di streaming. Vogliamo essere in grado di decodificare subito una stringa.
### Codici Istantanei
Un codice è istantaneo quando non esiste una parola nell'insieme $D$ dei simboli che è prefisso di un'altra parola.<br>
Definiamo provvisariamente l'insieme $\Bbb{C}$ come l'insieme delle codifiche della funzione $c$.<br>$\Bbb{C}\subseteq D^+$
$$\displaystyle\nexists\ x,y\in\Bbb{C},z\in D^+: y=x*z\implies c \text{ è istantaneo}$$
dove $x*z$ rappresenta la concatenazione di $x$ e $z$.
![I Codici non singolari sono un sottoinsieme dei Codici](/img/sottoinsiemi/Istantanei.jpeg)

### Codici a Virgola
Tra i codici istantanei, esistono i codici a virgola, dove ogni codifica termina con un carattere terminatore.
> Esempio<br>
con $d=3$, possiamo avere:<br>
$
c(\heartsuit)=102\\
c(\diamondsuit)=002\\
c(\clubsuit)=112\\
c(\spadesuit)=1102
$<br><br>
con $d=2$ invece possiamo avere:<br>
$c(\heartsuit)=0\\
c(\diamondsuit)=10\\
c(\clubsuit)=110\\
c(\spadesuit)=111$<br>
Quando il carattere terminatore è sulla codifica di lunghezza maggiore, si può omettere.

### Un codice istantaneo è univocamente decodificabile?
Vogliamo dimostrare che
$$c \text{ istantaneo}\implies c \text{ univocamente decodificabile}$$
Per dimostrarlo, pensiamo alla contronominale.
$$c \text{ non univocamente decodificabile}\implies c \text{ non istantaneo}$$
Sia $c: X\to D^+$ e $C:X^+\to D^+$ la sua estensione.<br>
Se $c$ non è univocamente decodificabile, allora $\exists x, x'\in X^+, x\ne x':C(x)=C(x')$.<br>
Possono esistere due casi:<br>

1. 
![I Codici non singolari sono un sottoinsieme dei Codici](/img/ist=>UD/caso1.jpeg)<br>
$x'$ è prefisso di $x$. Per far sì che le due codifiche siano uguali, la parte che "eccede" $x'$ in $x$ deve essere codificata nella parola vuota $\empty$. Questo è assurdo, perché $C:X^+\to D^+$ e $\empty$ non fa parte del codominio. In ogni caso, se anche considerassimo un'ulteriore estensione di $\hat C:X^+\to D^*$ che comprende anche la parola vuota nel codominio, tale parola sarebbe prefissa di ogni altra e questo renderebbe il codice non istantaneo.

2. 
![I Codici non singolari sono un sottoinsieme dei Codici](/img/ist=>UD/caso2.jpeg)<br>
$x$ e $x'$ condividono una parte comune, salvo differire nella parte finale. La parte comune avrà chiaramente la stessa codifica, dunque ci concentriamo sulla parte non comune.<br>
Supponiamo per semplicità che la parte non comune sia formata da due caratteri ciascuna. La loro codifica totale sarà la stessa, ma dal disegno si può vedere come la codifica di "$C$" sia prefisso della codifica di "$A$", rendendo il codice non istantaneo.

![I Codici non singolari sono un sottoinsieme dei Codici](/img/ist=>UD/codifica.jpeg)

### Campo di Galois
Un campo di Galois viene indicato con la dicitura $GF(p^n)$ dove $p$ è un numero primo e $n$ è un qualunque numero positivo. L'idea dei campi di Galois è di costruire un campo con $p^n$ elementi, partizionando l'insieme del polinomi di grado $n$ a coefficienti in $\Z_p$ usando come modulo un polinomio irriducibile di grado esattamente $n$.

### Radice Primitiva
In un campo, un elemento si dice <font color=red>Radice Primitiva</font> se quel numero elevato per tutti gli elementi del campo genera tutti gli elementi del campo, eccetto lo $0$.
> Esempio<br>
In $\Z_5$, $2$ è una radice primitiva.<br>
$
2^1 = 2\\
2^2 = 4\\
2^3 = 8 \equiv 3\\
2^4 = 16 \equiv 1
$<br>
In $\Z_7$, $2$ non è una radice primitiva.<br>
$
2^1 = 2\\
2^2 = 4\\
2^3 = 8 \equiv 1\\
2^4 = 16 \equiv 2\\
2^5 = 32 \equiv 4\\
2^6 = 64 \equiv 1
$