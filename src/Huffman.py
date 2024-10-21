def Huffman(X: list[str], P: list[float], d: int = 2) -> list:
    # Algoritmo che trova il codice istantaneo che minimizza il valore atteso delle lunghezze di codifica
    if len(X) != len(P):
        raise Exception('X and P must have the same lenght')
    sorgente = [(x, p) for x, p in zip(X, P)]
    counter = 0

    # Iteriamo finché la sorgente ha al massimo d simboli
    while len(sorgente) > d:
        counter += 1
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
    while len(codifica) < len(X):
        for i, simbolo in enumerate(codifica):
            if type(simbolo[0]) == list:
                for j, minisimbolo in enumerate(simbolo[0]):
                    codifica.append((minisimbolo, simbolo[1]+str(j)))
                codifica.remove(simbolo)
    return codifica
    

if __name__ == '__main__':
    X = list()
    X.append('s1')
    X.append('s2')
    X.append('s3')
    X.append('s4')
    X.append('s5')
    X.append('s6')
    P = list()
    P.append(0.05)
    P.append(0.45)
    P.append(0.12)
    P.append(0.09)
    P.append(0.16)
    P.append(0.13)
    print(Huffman(X, P, d=2))