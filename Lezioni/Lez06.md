# Teoria dell'Informazione
<html>
    <div align=center>
    Simone Alessandro Casciaro<br>
    18 Ottobre 2024
    </div>
</html>

## Lezione 6: Codici di Huffman
> <font color=#00CC99>Esercizio</font><br>
In questa lezione, partiamo da un esercizio
$\Bbb X=\{s_1, s_2, s_3, s_4, s_5, s_6\}$
$\Bbb P=\{0.05, 0.45, 0.12, 0.09, 0.16, 0.13\}$
Costruiamo un codice istantaneo.
È sufficiente costruire un codice a virgola, ad esempio:
$
c_1(s_1) = 1\\
c_1(s_2) = 01\\
c_1(s_3) = 001\\
c_1(s_4) = 0001\\
c_1(s_5) = 00001\\
c_1(s_6) = 00000
$
Questo codice non è ideale, in quanto lo abbiamo costruito ignorando le probabilità con cui ogni simbolo appare nella sorgente.
Infatti, $\Bbb E(l_{c_1}) = 1*0.5 + 2*0.45 + 3*0.12 + 4*0.09 + 5*0.16 + 5*0.13 = \boxed{3.12}$<br>
Se costruiamo un codice a virgola ordinando i simboli per probabilità, abbiamo:
$
c_2(s_1) = 00000\\
c_2(s_2) = 1\\
c_2(s_3) = 0001\\
c_2(s_4) = 00001\\
c_2(s_5) = 01\\
c_2(s_6) = 001
$
E abbiamo $\Bbb E(l_{c_2}) = 5*0.5 + 1*0.45 + 4*0.12 + 5*0.09 + 2*0.16 + 3*0.13 = \boxed{2.34}$

### Algoritmo di Huffman
L'algoritmo di Huffman ci permette di trovare il codice istantaneo che minimizza il valore atteso delle lunghezze $\Bbb E(l_c)$
Cioè vogliamo trovare il codice tale che $\begin{cases}\displaystyle\min_{l_1,\dots,l_n}\sum_{i=1}^mp_il_i\\\displaystyle\sum_{i=1}^md^{-l_1}\le1\end{cases}$
#### Come funziona l'algoritmo?
1. Si prendono i simboli della sorgente $\Bbb X$ e si ordinano in base alle probabilità in maniera decrescente.
2. Si crea un nuovo modello fittizio della sorgente $\Bbb X'$ in cui i $d$ simboli meno probabili sono sostituiti da un unico simbolo $\hat x$ con probabilità pari alla somma delle probabilità dei simboli sostituiti: $$p(\hat x) = \displaystyle\sum_{i=m-d+1}^m p(x_i)$$
3. Si itera fino a che la sorgente ha al massimo $d$ simboli.
> <font color=#00CC99>Esempio con il codice di inizio lezione</font>
Abbiamo $\Bbb X_1$ e supponiamo di avere $d=2$:
$
p(s_2) = 0.45\\
p(s_5) = 0.16\\
p(s_6) = 0.13\\
p(s_3) = 0.12\\
p(s_4) = 0.09\\
p(s_1) = 0.05
$
I due simboli meno probabili sono $s_4$ e $s_1$
<br>Costruiamo $\Bbb X_2$ sostituendo questi due simboli, poi ordiniamo nuovamente
$
p(s_2) = 0.45\\
p(s_5) = 0.16\\
p(s_{4+1}) = 0.14\\
p(s_6) = 0.13\\
p(s_3) = 0.12\\
$ e iterativamente finché abbiamo al massimo $2$ simboli
<br>Costruiamo $\Bbb X_3$
$
p(s_2) = 0.45\\
p(s_{6+3}) = 0.25\\
p(s_5) = 0.16\\
p(s_{4+1}) = 0.14\\
$ <br>Costruiamo $\Bbb X_4$
$
p(s_2) = 0.45\\
p(s_{5+4+1}) = 0.30\\
p(s_{6+3}) = 0.25\\
$ <br>Costruiamo $\Bbb X_5$
$
p(s_{5+4+1+6+3}) = 0.55\\
p(s_2) = 0.45
$

4. Si assegnano le $d$ codifiche ai $d$ simboli rimasti nell'ultima sorgente creata e si prosegue a ritroso iterativamente usando le concatenazioni
> Su $\Bbb X_5\\
c(s_{5+4+1+6+3}) = $ <font color=red> $0$ </font> $\\
c(s_2) = $ <font color=red> $1$ </font> $
$
ma $s_{5+4+1+6+3}$ era composto da $s_{5+4+1}$ e $s_{6+3}$, quindi associo loro le due codifiche con una concatenazione
<br>Su $\Bbb X_4\\
c(s_{5+4+1}) = 0$<font color=red>$0$</font>$\\
c(s_{6+3}) = 0$<font color=red>$1$</font>$\\
c(s_2) = 1
$
e si prosegue fino a $\Bbb X_1$
<br>Su $\Bbb X_3\\
c(s_5) = 00$<font color=red>$0$</font>$\\
c(s_{4+1}) = 00$<font color=red>$1$</font>$\\
c(s_{6+3}) = 01\\
c(s_2) = 1
$
<br>Su $\Bbb X_2\\
c(s_5) = 000\\
c(s_{4+1}) = 001\\
c(s_6) = 01$<font color=red>$0$</font>$\\
c(s_3) = 01$<font color=red>$1$</font>$\\
c(s_2) = 1
$
<br>Su $\Bbb X_1\\
c(s_5) = 000\\
c(s_4) = 001$<font color=red>$0$</font>$\\
c(s_1) = 001$<font color=red>$1$</font>$\\
c(s_6) = 010\\
c(s_3) = 011\\
c(s_2) = 1
$
Calcolando $\Bbb E(l_c) = 4*0.05+1*0.45+3*0.12+4*0.09+3*0.16+3*0.13 = \boxed{2.24}$

Un'implementazione Python del [Codice di Huffman](/src/Huffman.py) è la seguente

```python
def Huffman(X: list[str], P: list[float], d: int = 2) -> list:
    # Algoritmo che trova il codice istantaneo che minimizza il valore atteso delle lunghezze di codifica
    if len(X) != len(P):
        raise Exception('X and P must have the same lenght')
    
    # Inseriamo i Dummies
    nDummies = (1-len(X))%(d-1)

    sorgente = [(x, p) for x, p in zip(X, P)]
    for _ in range(nDummies):
        sorgente.append(('Dummy', 0))

    # Iteriamo finché la sorgente ha al massimo d simboli
    while len(sorgente) > d:
        # Si ordinano le probabilità
        sorgente = sorted(sorgente, key = lambda x:x[1], reverse=True)
        new_sorgente = []
        
        for i in range(len(sorgente)-d):
            new_sorgente.append(sorgente[i])
        # Si tolgono i d simboli meno probabili e si aggiunge un unico simbolo che li sostituisce
        sum_p = 0
        sum_x = []
        for i in range(d):
            sum_p += sorgente[len(sorgente)-1-i][1]
            sum_x.append(sorgente[len(sorgente)-1-i][0])
        new_sorgente.append((sum_x, sum_p))
        sorgente = new_sorgente.copy()

    # Creiamo la codifica
    codifica = []
    for i, simbolo in enumerate(sorgente):
        codifica.append((simbolo[0], str(i)))

    # Risrotoloiamo le codifiche
    while len(codifica) < len(X) + nDummies:
        for i, simbolo in enumerate(codifica):
            if type(simbolo[0]) == list:
                for j, minisimbolo in enumerate(simbolo[0]):
                    codifica.append((minisimbolo, simbolo[1]+str(j)))
                codifica.remove(simbolo)

    # Togliamo i Dummies
    for simbolo, codice in codifica:
        if simbolo == 'Dummy':
            codifica.remove((simbolo, codice))
    return codifica
```

### Codici di Huffman
Sia $c'$ un codice di Huffman $d-$ario per la sorgente $<\Bbb X', \Bbb P'>$ con $\Bbb X' = \{x_1,\dots, x_{m-d+1}\}$ e $\Bbb P' = \{p_1,\dots, p_{m-d+1}\}$ tali che<br> $p(x_i) = p_i\quad\forall i=1,\dots,m-d+1$ e<br> $p_i\ge p_j\quad\forall i<j$ (cioè le probabilità sono ordinate in ordine decrescente)
Si costruisce la sorgente $\Bbb X = \{x_1,\dots, x_{m+1}\}$ togliendo un simbolo $x_k$ ma aggiungendo $d$ elementi, in modo tale che $|\Bbb X|=m$. Si devono rispettare due proprietà:
1. $0\le p(x_{m+1})\le\dots\le p(x_{m-d+2})< p(x_{m-d+1})$ Le probabilità devono rimanere ordinate
2. $\displaystyle\sum_{i=2}^{d+1}p(x_{m-d+i}) = p(x_k)$ Le probabilità dei simboli aggiunti devono essere, sommate, uguali a quella del simbolo tolto

Allora, costruendo il codice $c$ in questo modo:
$$c(x_i) = \begin{cases}
c'(x_i)&i\le m-d+1\\
c'(x_k)a&i>m-d+1\quad a =0,\dots,d-1
\end{cases}$$
$c(x)$ è un codice di Huffman per la sorgente $\Bbb X$

### Teorema di Huffman
#### Ipotesi
Sia una sorgente $<\Bbb X, \Bbb P>$, $d>1$ e sia $c$ codice di Huffman
#### Tesi
$$c_2 \text{ codice istantaneo}\implies \Bbb{E}(l_c)\le \Bbb{E}(l_{c_2})$$
In pratica, il codice di Huffman minimizza il valore atteso delle lunghezze rispetto a tutti gli altri codici istantanei per la sorgente $\Bbb X$
#### Dimostrazione
Nella nostra dimostrazione, assumeremo sempre $d=2$ per semplicità nei conti, ma essa è estendibile anche al caso $d>2$
La dimostrazione è data per induzione, dunque

$\boxed{\text{Caso Base}}$
$|\Bbb X|\le d$ (nel nostro caso, quindi, $|\Bbb X|=2$)
Abbiamo i simboli $s_1$ e $s_2$ associate alle loro probabilità $p_1$ e $p_2$.
Indipendentemente dalle probabilità, si può associare ad ogni simbolo una codifica formata da un solo elemento di $D$ senza rendere il codice ambiguo.
Ad esempio, $c(s_1) = 0$ e $c(s_2) = 1$ oppure viceversa.

$\boxed{\text{Caso Induttivo}}$
$|\Bbb X|=m$
Assumiamo che per $|\Bbb X|=m-1$ il teorema di Huffman valga.
Prendiamo due elementi $u,v\in\Bbb X$ tali che $$
\begin{equation}
p(u)\text{ e }p(v)\text{ siano minime}
\end{equation}$$ Definiamo una nuova sorgente $<\Bbb{X'},\Bbb{P}'>$ sostituendo i simboli $u, v\in\Bbb{X}$ con un simbolo $z\in\Bbb{X'}$ e con probabilità
$$p'(x)=\begin{cases}
p(x)&x\ne z\\
p(u)+p(v)&x=z
\end{cases}$$
$$
\begin{equation}
\text{Il codice }c'\text{ è un codice di Huffman ottimale per la sorgente }\Bbb{X'} 
\end{equation}
$$ per ipotesi induttiva.

Costruiamo il codice $c$ sulla base di $c'$ in questo modo
$$c(x)=\begin{cases}
c'(x)&x\notin\{u,v\}\\
c'(z)0&x=u\\
c'(z)1&x=v
\end{cases}$$
$$
\begin{equation}
c\text{ è un codice di Huffman}
\end{equation}
$$ per definizione di codice di Huffman.

Calcoliamo $\Bbb{E}(l_c)$
$$
\begin{aligned}
\Bbb{E}(l_c) &=\displaystyle\sum_{x\in X}l_c(x)p(x)\\
&=\displaystyle\sum_{x\in X'}l_{c'}(x)p'(x)-l_{c'}(z)p'(z)+l_c(u)p(u)+l_c(v)p(v)\\
&=\displaystyle\sum_{x\in X'}l_{c'}(x)p'(x)-l_{c'}(z)p'(z)+\big(l_{c'}(z)+1\big)p(u)+\big(l_{c'}(z)+1\big)p(v)\\
&=\displaystyle\sum_{x\in X'}l_{c'}(x)p'(x)-l_{c'}(z)p'(z)+\big(l_{c'}(z)+1\big)\big(p(u)+p(v)\big)\\
&=\displaystyle\sum_{x\in X'}l_{c'}(x)p'(x)-l_{c'}(z)p'(z)+\big(l_{c'}(z)+1\big)\big(p'(z)\big)\\
&=\displaystyle\sum_{x\in X'}l_{c'}(x)p'(x)-l_{c'}(z)p'(z)+l_{c'}(z)p'(z)+p'(z)\\
&=\displaystyle\sum_{x\in X'}l_{c'}(x)p'(x)+p'(z)\\
&=\Bbb{E}(l_{c'})+p'(z)
\end{aligned}
$$
Dunque
$$
\begin{equation}
\Bbb{E}(l_c)=\Bbb{E}(l_{c'})+p'(z)
\end{equation}
$$

Consideriamo ora, una seconda funzione di codifica $c_2$ per la sorgente $\Bbb{X}$. Prendiamo due elementi $r,s\in\Bbb X$ tali che
$$
\begin{equation}
l_{c_2}(r)\text{ e }l_{c_2}(s)\text{ sono massime}
\end{equation}
$$ Si hanno $3$ casi nell'albero di codifica:

1. $r$ e $s$ non sono fratelli, ma hanno dei fratelli
![Caso1](/img/huffman/Caso1.png)
2. $r$ e $s$ non sono fratelli e non hanno fratelli
![Caso2](/img/huffman/Caso2.png)
3. $r$ e $s$ sono fratelli
![Caso3](/img/huffman/Caso3.png)

Tutti e 3 i casi sono riconducibili al terzo, quindi possiamo analizzare solo questo caso senza perdere di generalità.
Costruisco il codice $\tilde{c}_2$ in questo modo
$$
\tilde{c}_2(x)=\begin{cases}
c_2(x)&x\not\in\{r,s,u,v\}\\
c_2(u)&x=r\\
c_2(v)&x=s\\
c_2(r)&x=u\\
c_2(s)&x=v
\end{cases}
$$ In poche parole, stiamo invertendo le codifiche tra $u, v, r, s$
Calcoliamo $\Bbb{E}(l_{\tilde{c}_2})-\Bbb{E}(l_{c_2})$

$$
\begin{aligned}
\Bbb{E}(l_{\tilde{c}_2})-\Bbb{E}(l_{c_2})&=\displaystyle\sum_{x\in \Bbb X}p(x)l_{\tilde{c}_2}(x)-\sum_{x\in \Bbb X}p(x)l_{c_2}(x)\\
&=\displaystyle\sum_{x\in \Bbb X}p(x)\Big(l_{\tilde{c}_2}(x)-l_{c_2}(x)\Big)\\
&=\displaystyle\sum_{x\in\{u,v,r,s\}}p(x)\Big(l_{\tilde{c}_2}(x)-l_{c_2}(x)\Big)\\
&=p(r)l_{c_2}(u)+p(u)l_{c_2}(r)+p(s)l_{c_2}(v)+p(v)l_{c_2}(s)\\&-p(u)l_{c_2}(u)-p(r)l_{c_2}(r)-p(v)l_{c_2}(v)-p(s)l_{c_2}(s)\\
&=\Big(p(r)-p(u)\Big)\Big(l_{c_2}(u)-l_{c_2}(r)\Big)+\Big(p(s)-p(v)\Big)\Big(l_{c_2}(v)-l_{c_2}(s)\Big)
\end{aligned}
$$
Grazie al punto $1$, sappiamo che $p(r) \ge p(u)$ e $p(s) \ge p(v)$
Grazie al punto $5$, sappiamo che $l_{c_2}(u)\le l_{c_2}(r)$ e $l_{c_2}(v)\le l_{c_2}(s)$
Dunque il risultato è negativo e
$$
\begin{equation}
\Bbb{E}(l_{\tilde{c}_2})\le\Bbb{E}(l_{c_2})
\end{equation}
$$
Costruiamo un'ulteriore funzione di codifica $c_{2}'$ per la sorgente $<\Bbb{X}', \Bbb{P}'>$ in questo modo:
$$
c_2'(x)=\begin{cases}
\tilde c_2(x)&x\ne z\\
\omega&x=z
\end{cases}
$$
con $p'(z)=p(u)+p(v)$

Calcoliamo $\Bbb E(l_{\tilde c_2})$
$$
\begin{aligned}
\Bbb E(l_{\tilde c_2})&=\sum_{x\in \Bbb X}p(x)l_{\tilde c_2}(x)\\
&=\sum_{x\in \Bbb X\text{\textbackslash}\{z\}}p'(x)l_{c_2'}(x)+p(u)\Big(l_{c_2'}(z)+1\Big)+p(v)\Big(l_{c_2'}(z)+1\Big)\\
&=\sum_{x\in \Bbb X\text{\textbackslash}\{z\}}p'(x)l_{c_2'}(x)+\Big(l_{c_2'}(z)+1\Big)\big(p(u)+p(v)\big)\\
&=\sum_{x\in \Bbb X\text{\textbackslash}\{z\}}p'(x)l_{c_2'}(x)+\Big(l_{c_2'}(z)+1\Big)\big(p'(z)\big)\\
&=\sum_{x\in \Bbb X\text{\textbackslash}\{z\}}p'(x)l_{c_2'}(x)+l_{c_2'}(z)p'(z)+p'(z)\\
&=\Bbb E(l_{c_2'})+p'(z)\\
\end{aligned}
$$
Quindi
$$
\begin{equation}
\Bbb E(l_{\tilde c_2})=\Bbb E(l_{c_2'})+p'(z)
\end{equation}
$$

Unendo i pezzi:
Grazie al punto $3$, sappiamo che $c$ è un codice di Huffman
Inoltre,
$$
\begin{aligned}
\Bbb{E}(l_c)&=\Bbb{E}(l_{c'})+p'(z)&\text{Per il punto }4\\
&\le\Bbb{E}(l_{{c_2'}})+p'(z)&\text{Per il punto }2\\
&=\Bbb E(l_{\tilde c_2})&\text{Per il punto }7\\
&\le \Bbb{E}(l_{c_2})&\text{Per il punto }6
\end{aligned}
$$
Abbiamo dimostrato che $\Bbb{E}(l_c) \le \Bbb{E}(l_{c_2})$ per qualunque $c_2$ istantaneo e quindi il codice $c$ è ottimo.