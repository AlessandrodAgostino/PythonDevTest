# PythonDevTest

## Generatore di Esercizi sui Polinomi Ordinati
###Alessandro d'Agostino

Il progetto è mirato allo sviluppo di un generatore di esercizi basati sul riconoscimento dei polinomi ordinati all'interno di un elenco proposto.
Il testo degli esercizi è composto da più sezioni: *consegna*, *opzioni*, *risoluzione guidata* e *risposte corrette*. Le sezioni fanno tutte riferimento ad uno stesso set di 6 polinomi generati per ciascun esercizio.

I polinomi vengono generati secondo alcune precise specifiche, in particolare:
* Coefficienti interi compresi tra -12 e +12.
* Esponenti naturali compresi tra 1 e 5.
* Min 2, max 4 termini per polinomio. Di cui almeno un polinomio da 4 termini e uno da 2 termini.
* Nel singolo polinomio una sola lettera per termine tra {x, y, z, a, b, c}. L’incognita deve essere uguale in tutto il polinomio.

Le 6 risposte proposte dall'esercizio seguono invece la seguente struttura:
* 3 risposte errate, corrispondenti a polinomi non ordinati.
* 2 risposte esatte, corrispondenti a polinomi ordinati in maniera crescente.
* 1 risposte esatta, corrispondente ad un polinomio ordinato in maniera decrescente.

È importante notare come i polinomi coinvolti siano:
* Ad una singola incognita: per cui nella parte letterale di ciscun monomio compare la stessa e unica lettera.
* In forma normale: per cui tutti non ci sono più termini con la stessa parte letterale e il polinomio non può essere ulteriormente semplificato.

La mancanza di questi vincoli avrebbe complicato notevolmente lo sviluppo delle classi necessarie per lo sviluppo del generatore.

### Implementazione

Il fulcro del progetto sono le due classi ``Mon`` e ``Pol``, create rispettivamente per rappresentare i monomi e le loro collezioni, cioè i polinomi. Lo script di generazione sfrutta le due classi per creare un dizionario ``Esercizio`` contenente tutte le sezioni richieste dalla traccia.

#### Classe Mon

La classe ``Mon`` è stata pensata per rappresentare il singolo monomio ad una sola incognita. Ho deciso di inserire come attributi di classe i vincoli a coefficienti, gradi e caratteri delle incognite, in ottica di un ipotetio riutilizzo in un'altra situazione. Infatti sembrano vincoli piuttosto generali ed orientati alla leggibilità dell'esercizio prodotto, senza compromettere la ricchezza concettuale.

Con la stessa intenzione ho inserito dei controlli sui coefficienti nel costruttore della classe ``Mon`` sul rispetto dei vincoli di classe. Inoltre in questi controlli si esclude il valore ``0`` tra i coefficienti ammessi, che ha sì validità matematica, ma scarsa utilità per questo tipo di applicazioni. I controlli sollevano una ``Exception`` per bloccare l'esecuzione e inoltrano un messaggio di errore.

Il metodo ``__str__`` è stato implementato per gestire agilmente la stampa del singolo monomio e la logica condizionale riguardante il segno e la stampa dell'esponente della parte letterale.

**Due parole sui Test.**

#### Classe Pol

La classe ``Pol`` è stata pensata per rappresentare il singolo polinomio ad incognita omogenea, e la sua proprietà di ordinamento. Sostanzialmente un polinomio può essere pensato come una lista di singoli monomi. L'implementazione della classe tuttavia è indipendente dalla classe ``Mon``, rendendo possibile un suo riutilizzo con altre ipotetiche classi di monomi con caratteristiche diverse.

L'attributo principale di ciscuna istanza è una lista di monomi che viene manipolata da tutti gli altri metodi. Il metodo costruttore prende in input tale lista e controlla che tutti i monomi abbiano la stessa parte letterale e che non ci siano termini con lo stesso grado. Se il controllo fallisce viene lanciata una ``Exception`` per bloccare l'esecuzione e inoltrato messaggio di errore.

Essendo l'esercizio da generare improntato sull'ordinamento dei polinomi ho deciso di aggiungere un attributo di istanza per rendere disponibile l'informazione. L'attributo ``ordine`` viene inizializzato a ``None`` dal costruttore e viene modificato solo dai metodi della classe che manipolano l'ordine dei monomi nella lista del polinomio. I valori ammessi per l'attributo sono ``{'ASC', 'DESC', 'SHUFFLE'}``.

Il metodo ``sort`` implementa l'ordinamento dei polinomi in ordine crescente o decrescente, ed è basato sostanzialmente sul metodo ``list.sort``. La funzione di chiave per l'ordinamente è una funzione ``lambda`` che estrae il valore del grado del singolo monomio, demandandone l'eventuale calcolo alla classe che rappresenta il monomio. Viene mantenuta la possibilità di passare il parametro ``reverse`` per l'ordinamente inverso. A seguito dell'ordinamento, a seconda del parametro ``reverse`` viene valorizzato l'attributo ``ordine`` con i valori ``'ASC' o 'DESC'``. Una modifica importante rispetto al metodo ``list.sort`` è l'aggiunta della clausola di ``return`` per la restituzione dell'istanza chiamante, permettendo l'utilizzo a cascata del metodo.

Il metodo ``shuffle`` implementa il *disordinamento* del polinomio, mescolando i termini e assicurandosi che non sia ordinato prima di restituirlo. Il metodo è basato a sua volta sul metodo ``random.shuffle`` per il mescolamento degli elementi di una lista. Nel caso la lunghezza della lista sia maggiore di 2 viene eseguito un loop di controllo per assicurarsi che il mescolamento non produca accidentalmente polinomi ordinati. Ciò comporterebbe incoerenze nella generazione delle risposte vere e false, compromettendo il testo dell'esercizio.A seguito dell'ordinamento l'attributo ``ordine`` viene valorizzato a ``'SHUFFLE'``. Anche a questo metodo è stata aggiunta la clausola di ``return`` per la restituzione dell'istanza chiamante, permettendo l'utilizzo a cascata del metodo.

Il metodo ``__str__`` implementa la stampa del polinomio unendo le conversioni a stringa dei singoli monomi della lista.

**Due parole sui Test.**

#### Generazione Esercizio

Nello script di generazione dell'esercizio sono presenti tutte le operazioni necessarie per arrivare alla composizione delle diverse sezioni *consegna*, *opzioni*, *risoluzione guidata* e *risposte corrette*.

La funzione ``gen_pol`` è responsabile della generazione di polinomi secondo i criteri dell'esercizio a partire dai parametri in input per il numero di monomi e la variabile del polinomio.

La funzione ``gen_risposte`` si occupa di generare finalmente le opzioni di risposta del'esercizio. Vengono generati prima i 6 valori che regolano il numero di elementi di ciascun polinomio, secondo le indicazioni della traccia, e poi i polinomi con il corrispondente ordinamento. Le risposte vengono salvate in una lista di dizionari che espongono il polinomio di ciascuna opzione, il suo ordinamente e la sua verità.

La verità o meno della singola opzione di risposta viene valutata tramite l'applicazione della funzione ``verita_opzione``, che funge da *maschera di verità*. In questo caso la funzione (``lambda``) semplicemente verifica l'ordinamento del polinomio. Grazie a questa scelta con l'implementazione di una funzione diversa si potrebbe applicare una maschera di verità alternativa alle opzioni dell'esercizio, permettendo di generare agilmente esercizi analoghi ma dalla consegna diversa. Ad esempio  la traccia:

>"Seleziona i polinomio di grado 4°.".

Una volta che le opzioni di risposta sono state generate segue una routine di comandi per l'effettiva generazione delle stringhe delle diverse sezioni, in cui si fa largo uso della formattazione parametrica delle stringe. A conclusione dello script vengono raccolti tutti i segmenti genenerati ed organizzati in un dizionario come segue:

```
Esercizio = { 'consegna': f'Seleziona i polinomi ordinati rispetto {var_consegna}.',
              'opzioni' : '\n'.join(['\to '+str(d['polinomio']) for d in risposte]),
    'soluzione_guidata' : '\n'.join(paragrafi),
    'risp_corrette_idx' : [i for i,r in enumerate(risposte) if r['verita']]
}
```
L'esercizio espresso sottoforma di dizionario permette un'agevole serializzabilità del risultato, permettendo il salvataggio e il riutilizzo del testo prodotto.
La stampa consecutiva di tutti i campi del dizionario è il testo generato dell'esercizio:

```
Seleziona i polinomi ordinati rispetto y.
	o -4y^5 +10y^1 +5y^2
	o -9y^2 +2y^4 -10 +1y^5
	o +7y^1 -1y^3 +10y^5
	o +6y^4 +1
	o +10 +2y^1 -12y^3 -8y^4
	o +1y^5 +8 +9y^4 +5y^2 +7y^1
Un polinomio è ordinato rispetto a una lettera se i suoi termini sono ordinati secondo le potenze crescenti
(o decrescenti) di quella lettera: devi escludere i polinomi in cui gli esponenti di y non sono in ordine
crescente o decrescente.
Escludi quindi:
	o -4y^5 +10y^1 +5y^2
	o -9y^2 +2y^4 -10 +1y^5
	o +1y^5 +8 +9y^4 +5y^2 +7y^1
I polinomi:
	o +7y^1 -1y^3 +10y^5
	o +10 +2y^1 -12y^3 -8y^4
sono ordinati secondo le potenze crescenti di y.
Infine, il polinomio:
	o +6y^4 +1
è ordinato secondo le potenze decrescenti di y.
[2, 3, 4]
```

## Migliorie
* Aggiunta del SEED per la generazione
* Implementazione test Pol, Mon e Generatore
