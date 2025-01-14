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
    

if __name__ == '__main__':
    X = [f"a{i}" for i in range(1,13)]
    P = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05]
    print(Huffman(X, P, d=2))