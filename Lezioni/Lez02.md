# Teoria dell'Informazione
<html>
    <div align=center>
    Simone Alessandro Casciaro<br>
    04 Ottobre 2024
    </div>
</html>

## Lezione 2: Shannon
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
Codici non singolari $\subset$ Codici<br>
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
Codice Univocamente Decodificabile $\subset$ Codice Non Singolare<br>
![I Codici Univocamente Decodificabili sono un sottoinsieme dei Codici non singolari](/img/sottoinsiemi/UD.jpeg)

> Esempio<br>
Consideriamo $c(\heartsuit)=10\quad c(\diamondsuit)=00\quad c(\clubsuit)=11\quad c(\spadesuit)=110$<br>
Questo codice è univocamente decodificabile. Tuttavia, se dobbiamo decodificare la stringa $110...0$, il numero di $0$ influenza la decodifica ($\clubsuit,\diamondsuit,\diamondsuit,\diamondsuit,...$ oppure $\spadesuit,\diamondsuit,\diamondsuit,\diamondsuit,...$). Questo obbliga ad aspettare la fine della stringa per decodificarla, creando problemi ad esempio in caso di streaming. Vogliamo essere in grado di decodificare subito una stringa.
### Codici Istantanei
Un codice è istantaneo quando non esiste una parola nell'insieme $D$ dei simboli che è prefisso di un'altra parola.<br>
Definiamo provvisariamente l'insieme $\Bbb{C}$ come l'insieme delle codifiche della funzione $c$.<br>$\Bbb{C}\subseteq D^+$
$$\displaystyle\nexists\ x,y\in\Bbb{C},z\in D^+: y=x*z\implies c \text{ è istantaneo}$$
dove $x*z$ rappresenta la concatenazione di $x$ e $z$.<br>
Codici Istantanei $\subset$ Codice Univocamente Decodificabile<br>
![I Codici Istantanei sono un sottoinsieme dei Codici Univocamente Decodificabili](/img/sottoinsiemi/Istantanei.jpeg)

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
![x prefisso di x'](/img/ISTtoUD/caso1.jpeg)<br>
$x'$ è prefisso di $x$. Per far sì che le due codifiche siano uguali, la parte che "eccede" $x'$ in $x$ deve essere codificata nella parola vuota $\empty$. Questo è assurdo, perché $C:X^+\to D^+$ e $\empty$ non fa parte del codominio. In ogni caso, se anche considerassimo un'ulteriore estensione di $\hat C:X^+\to D^*$ che comprende anche la parola vuota nel codominio, tale parola sarebbe prefissa di ogni altra e questo renderebbe il codice non istantaneo.

2. 
![Prefisso comune](/img/ISTtoUD/caso2.jpeg)<br>
$x$ e $x'$ condividono una parte comune, salvo differire nella parte finale. La parte comune avrà chiaramente la stessa codifica, dunque ci concentriamo sulla parte non comune.<br>
Supponiamo per semplicità che la parte non comune sia formata da due caratteri ciascuna. La loro codifica totale sarà la stessa, ma dal disegno si può vedere come la codifica di "$C$" sia prefisso della codifica di "$A$", rendendo il codice non istantaneo.

![C prefisso di A](/img/ISTtoUD/codifica.jpeg)

### Esercizio
$GF(4)=GF(2^2)$. Il campo di Galois è $\Z_2[x] \mod x^2+x+1$<br>
Effettuiamo la Pre-Computazione del campo sia per l'operazione $+$ sia per l'operazione $*$<br>
| + | 0 | 1 | x | x+1
|---|---|---|---|---|
| 0 | 0 | 1 | x | x+1
| 1 | 0 | 0 | x+1 | x
| x | x | x+1 | 0 | 1
| x+1 | x+1 | x | 1 | 0
<br>

| * | 0 | 1 | x | x+1
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0
| 1 | 0 | 1 | x | x+1
| x | 0 | x | x+1 | 1
| x+1 | 0 | x+1 | 1 | x