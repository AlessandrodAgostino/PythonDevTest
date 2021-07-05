# PythonDevTest

## Generatore di Esercizi sui Polinomi Ordinati
### Alessandro d'Agostino

Lo scopo del progetto è lo sviluppo di un generatore di esercizi basati sul riconoscimento dei polinomi ordinati all'interno di un elenco di polinomi proposto. Il testo degli esercizi è composto da più sezioni: *consegna*, *opzioni*, *risoluzione guidata* e *risposte corrette* e le sezioni fanno tutte riferimento ad uno stesso set di 6 polinomi diverso da esercizio ad esercizio.

I polinomi vengono generati secondo alcune precise specifiche, in particolare:
* Coefficienti interi compresi tra -12 e +12.
* Esponenti naturali compresi tra 1 e 5.
* Min 2, max 4 termini per polinomio. Di cui almeno un polinomio da 4 termini e uno da 2 termini.
* Nel singolo polinomio una sola lettera per termine tra {x, y, z, a, b, c}.
* L’incognita deve essere uguale in tutto il polinomio e tra tutti i polinomi dell'esercizio.

Le 6 risposte proposte dall'esercizio seguono invece la seguente struttura:
* 3 risposte *errate*, corrispondenti a polinomi non ordinati.
* 2 risposte *esatte*, corrispondenti a polinomi ordinati in maniera crescente.
* 1 risposte *esatta*, corrispondente ad un polinomio ordinato in maniera decrescente.

Tutto il codice necessario alla generazione degli esercizi è contenuto interamente in questa repository insieme con i test per il controllo del suo funzionamento.

###### Esempio di utilizzo:

All'interno del file ``TRYME.py`` è riportato un esempio di utilizzo del codice. All'interno dello script viene importata la classe ``Esercizio``, costruita una sua instanza e infine esportato il testo dell'esercizio in formato ``.txt`` nella cartella ``esercizi_generati``. Il nome del file contiene il riferimento all'incognita ``var`` e al ``seed`` di generazione che identificano univocamente l'esercizio generato.

```
from esercizio import Esercizio

es = Esercizio(var = 'b', seed = 123)
es.to_txt(path = 'esercizi_generati')
# Scrittura del file:
# esercizi_generati/espolord_b123.txt
```

###### Esempio di esercizio generato:

All'interno del file generato ``espolord_b123.tx`` è contenuto il seguente testo:
```
Seleziona i polinomi ordinati rispetto b:

	o -12b^3 +b^4 +3 -5b^2
	o 8b^4 -2b^3 -7b +11
	o 5b^3 +10b^5 +b^4
	o 9 +4b^3
	o -7b +2b^2 +11b^5
	o 10b +2b^3 -8 +11b^2

Un polinomio è ordinato rispetto a una lettera se i suoi termini sono ordinati secondo le potenze crescenti
(o decrescenti) di quella lettera: devi escludere i polinomi in cui gli esponenti di b non sono in ordine
crescente o decrescente.
Escludi quindi:
	o -12b^3 +b^4 +3 -5b^2
	o 5b^3 +10b^5 +b^4
	o 10b +2b^3 -8 +11b^2

I polinomi:
	o 9 +4b^3
	o -7b +2b^2 +11b^5
sono ordinati secondo le potenze crescenti di b.

Infine, il polinomio:
	o 8b^4 -2b^3 -7b +11
è ordinato secondo le potenze decrescenti di b.

Risposte corrette: [1, 3, 4]
```

È importante notare come i polinomi coinvolti siano:
* Ad una singola incognita: per cui nella parte letterale di ciscun monomio compare la stessa e unica lettera.
* In forma normale: per cui non ci sono più termini con la stessa parte letterale e il polinomio non può essere ulteriormente semplificato.

La mancanza di questi vincoli avrebbe complicato lo sviluppo delle classi necessarie per lo sviluppo del generatore.

### Implementazione

Il fulcro del progetto è la classe ``Esercizio`` che si occupa di generare, custodire e salvare il testo dell'esercizio generato. Tutta la logica di generazione è invece basata sulle classi ``Mon`` e ``Pol``, create rispettivamente per rappresentare i monomi e le loro collezioni, cioè i polinomi. Qualora possibile è sempre stato preferito l'utilizzo di funzionalità già presenti nelle librerie standard di Python all'utilizzo di pacchetti di terze parti o all'implementazione ex novo.

#### Classe Mon

La classe ``Mon`` rappresenta il singolo monomio ad una sola incognita. Sono presenti come attributi di classe i vincoli a coefficienti, gradi e caratteri delle incognite, in ottica di un ipotetio riutilizzo in un'altra situazione. I vincoli imposti sembrano infatti piuttosto generali ed orientati alla leggibilità dell'esercizio prodotto, senza compromettere la ricchezza dei casi possibili. La presenza di questi parametri a livello di classe facilita inoltre la scrittura di test parametrici.

Sono stati implementati dei controlli sui coefficienti all'interno del costruttore della classe ``Mon`` per verificare il rispetto dei vincoli di classe. Inoltre in questi controlli si esclude il valore ``0`` tra i coefficienti ammessi, che ha sì validità matematica, ma scarsa utilità per questo tipo di applicazioni. In caso di violazione dei controlli si solleva una ``Exception`` per bloccare l'esecuzione e inoltrare un messaggio di errore.

Il metodo ``__str__`` è stato implementato per gestire agilmente la stampa del singolo monomio e la logica condizionale riguardante il segno e la stampa dell'esponente della parte letterale.

#### Classe Pol

La classe ``Pol`` rappresenta il singolo polinomio ad incognita omogenea e la sua proprietà di ordinamento. Sostanzialmente un polinomio può essere pensato come una lista di singoli monomi. L'implementazione della classe tuttavia è indipendente dalla classe ``Mon``, rendendo possibile un suo riutilizzo con classi di monomi alternative con caratteristiche diverse.

L'attributo principale di ciscuna istanza è una lista di monomi che viene manipolata da tutti gli altri metodi. Il metodo costruttore prende in input tale lista e controlla che tutti i monomi abbiano la stessa parte letterale e che non ci siano termini con lo stesso grado. Se il controllo fallisce viene lanciata una ``Exception`` per bloccare l'esecuzione e inoltrato messaggio di errore.

Essendo l'esercizio da generare improntato sull'ordinamento dei polinomi è stato aggiunto un attributo di istanza per rendere disponibile tale informazione. L'attributo ``ordine`` viene inizializzato a ``None`` dal costruttore e viene modificato solo dai metodi della classe che manipolano l'ordine dei monomi nella lista del polinomio. I valori ammessi per l'attributo sono ``{'ASC', 'DESC', 'SHUFFLE'}``.

Il metodo ``sort`` implementa l'ordinamento dei polinomi in ordine crescente o decrescente, ed è basato sostanzialmente sul metodo ``list.sort``. La funzione di chiave per l'ordinamente è una funzione ``lambda`` che estrae il valore del grado del singolo monomio, demandandone l'eventuale calcolo alla classe che rappresenta il monomio. Viene mantenuta la possibilità di passare il parametro ``reverse`` per l'ordinamente inverso. A seguito dell'ordinamento, a seconda del parametro ``reverse`` viene valorizzato l'attributo ``ordine`` con i valori ``'ASC' o 'DESC'``. Una modifica importante rispetto al metodo ``list.sort`` è l'aggiunta della clausola di ``return`` per la restituzione dell'istanza chiamante, permettendo l'utilizzo a cascata del metodo.

Il metodo ``shuffle`` implementa il *disordinamento* del polinomio, mescolando i termini e assicurandosi che non sia ordinato prima di restituirlo. Il metodo è basato a sua volta sul metodo ``random.shuffle`` per il mescolamento degli elementi di una lista. Nel caso la lunghezza della lista sia maggiore di 2 viene eseguito un loop di controllo per assicurarsi che il mescolamento non produca accidentalmente polinomi ordinati. Ciò comporterebbe incoerenze nella generazione delle risposte vere e false, compromettendo il senso del testo dell'esercizio. A seguito dell'ordinamento viene valorizzato  l'attributo ``ordine`` a ``'SHUFFLE'``. Anche a questo metodo è stata aggiunta la clausola di ``return`` per la restituzione dell'istanza chiamante, permettendo l'utilizzo a cascata del metodo.

Il metodo ``__str__`` implementa la stampa del polinomio unendo le conversioni a stringa dei singoli monomi della lista.

#### Classe Esercizio

La classe ``Esercizio`` è il contenitore delle quattro sezioni *consegna*, *opzioni*, *risoluzione guidata* e *risposte corrette* che compongono ogni esercizio e si occupa della loro generazione e salvataggio. I due parametri di input del costruttore sono l'incognita ``var`` dei polinomi dell'esercizio e il valore di seed per impostare lo stato del generatore di numeri pseudo-random. È stato introdotto l'attributo ``seed`` per regolare il meccanismo di riproducibilità dell'esercizio, come buona norma in ogni procedura di generazione. In questa maniera è possibile etichettare in modo univoco il singolo esercizio con la coppia ``(var, seed)``. Sempre all'interno del costruttore le quattro sezioni vengono popolate sfruttando la formattazione parametrica delle stringhe a partire dal testo a disposizione nella traccia.

Il metodo ``gen_pol`` è responsabile della generazione di polinomi secondo i criteri dell'esercizio a partire dai parametri in input per il numero di monomi e l'incognita del polinomio. Il metodo restituisce una istanza della classe ``Pol``.

Il metodo ``gen_risposte`` genera invece le opzioni di risposta del'esercizio. Vengono generati prima i 6 valori che regolano il numero di elementi di ciascun polinomio, secondo le indicazioni della traccia, e poi i polinomi con il corrispondente ordinamento. Le risposte vengono mescolate e salvate nell'attributo dedicato ``risposte`` sottoforma di lista di dizionari composti dal polinomio di ciascuna opzione, il suo ordinamente e la sua verità:

```
[{'polinomio': +1y^3 +7y^5,
  'ordine'   : 'ASC',
  'verita'   : True }, ...]
```
La verità o meno della singola opzione di risposta viene valutata tramite l'applicazione della funzione ``verita_opzione``, che funge da *maschera di verità*. In questo caso la funzione ``lambda p: p.ordine in {'ASC', 'DESC'}`` semplicemente verifica l'ordinamento del polinomio tramite una condizione sul parametro di ordine. Grazie a questa scelta con l'implementazione di una funzione diversa si potrebbe applicare una maschera di verità alternativa alle opzioni dell'esercizio, permettendo di generare agilmente esercizi analoghi ma dalla consegna diversa. Ad esempio, la funzione ``lambda p: max([m.grado for m in p.mon_list]) is 4`` permetterebbe di generare esercizi per l'ipotetica traccia:

> Seleziona i polinomio di grado 4°

Il metodo ``__str__`` implementa la stampa dell'esercizio, restituendo l'unione delle quattro sezioni *consegna*, *opzioni*, *risoluzione guidata* e *risposte corrette*

Il metodo ``to_txt`` implementa una funzionalità ulteriore a quelle richieste nella traccia per la stampa del testo dell'esercizio generato su file in formato ``.txt``. Il nome del file prodotto riporta la coppia ``(var, seed)`` che identifica univocamente l'esercizio.

#### Scrittura dei test

Tutte i metodi di tutte le classi implementate sono stati sottoposti a test unitario. Per la scrittura dei test sono stati usati i framework ``pytest`` e ``hypothesis``. Per la corretta esecuzione dei test quindi è necessario prima installare le dipendenze richieste contenute nel file ``test_requirements.txt`` con il comando:
```
pip install -r test_requirements.txt
```
