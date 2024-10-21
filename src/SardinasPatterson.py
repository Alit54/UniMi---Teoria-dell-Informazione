# Determina se il codice è univocamente decodificabile
def SardinasPatterson(C: set, show=False) -> bool:
    S = C
    Ss = []
    while (len(S) != 0):
        nextS = set()
        # Caso A
        for i in C:
            for j in S:
                if len(i) < len(j) and j[:len(i)] == i:
                    nextS.add(j[len(i):])
        # Caso B
        for i in S:
            for j in C:
                if len(i) < len(j) and j[:len(i)] == i:
                    nextS.add(j[len(i):])
        # Stampo a video il nuovo set
        if show:
            print(nextS)
        # Controllo se una parola del nuovo set è in C
        for i in nextS:
            if i in C:
                return False
        # Controllo se il nuovo set è già stato visto
        if nextS in Ss:
            return True
        else:
            Ss.append(nextS)
        S = nextS.copy()
    return True

if __name__ == '__main__':
    codice = set()
    codice.add("A")
    codice.add("BCA")
    codice.add("DE")
    codice.add("CBC")
    codice.add("AABC")
    codice.add("C")
    print(SardinasPatterson(codice, True))