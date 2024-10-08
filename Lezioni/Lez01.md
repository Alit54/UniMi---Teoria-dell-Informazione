# Teoria dell'Informazione
<html>
    <div align=center>
    Simone Alessandro Casciaro<br>
    01 Ottobre 2024
    </div>
</html>

## Lezione 1: Introduzione
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
- 2° Teorema di Shannon, fase di Codifica e di uso del Canale: si cerca di minimizzare il numero di errori

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