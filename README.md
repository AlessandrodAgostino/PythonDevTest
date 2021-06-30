# PythonDevTest

## Traccia del Problema

Il progetto è mirato allo sviluppo di un generatore di esercizi basati sul riconoscimento dei polinomi ordinati all'interno di un elenco proposto.
Il testo degli esercizi è composto da più paragrafi: CONSEGNA, OPZIONI, RISOLUZIONE GUIDATA, RISPOSTE CORRETTE. I paragrafi fanno tutti riferimento ad uno stesso set di 6 polinomi generati per ciascun esercizio.

I polinomi vengono generati secondo alcune precise specifiche, in particolare:
* min 2, max 4 termini per polinomio. Di cui almeno un polinomio da 4 termini e uno da 2 termini.
* coefficienti interi compresi tra -12 e +12.
* esponenti naturali compresi tra 1 e 5.
* nel singolo polinomio una sola lettera per termine tra {x, y, z, a, b, c}. L’incognita deve essere uguale in tutto il polinomio.

Le 6 risposte proposte dall'esercizio seguono invece la seguente struttura:
* 3 risposte errate, corrispondenti a polinomi non ordinati.
* 2 risposte esatte, corrispondenti a polinomi ordinati in maniera crescente.
* 1 risposte esatta, corrispondente ad un polinomio ordinato in maniera decrescente.

È importante notare che i polinomi in questione siano tutti ad una singola incognita, per cui nella parte letterale di ciscun monomio compare la stessa e unica lettera. La mancanza di questo vincolo avrebbe complicato notevolmente lo sviluppo delle classi necessarie per lo sviluppo del generatore.

## Implementazione

Il fulcro del progetto sono le due classi Mon e Pol, create rispettivamente per rappresentare i monomi e le collezioni di essi, cioè i polinomi.

### Classe Mon

Descrizione classe Mon. Attributi statici. Controlli nel costruttore con eccezione. Conversione a stringa. Test.

### Classe Pol

Descrizione classe Pol. Controlli nel costruttore con eccezione. Conversione a stringa.
Metodo sort. Metodo shuffle. Test.

### Generazione Esercizio

Funzione per generare un polinomio secondo i criteri.
Funzione per generere le risposte secondo i criteri dell'esercizio
Accenno all'utilizzo della funzione lambda per stabilire la verità di un'opzione (possibilità di adattamento ad altri esercizi).
Salvo le risposte come dizionario per esporre meglio le informazioni e rendere più chiaro il codice.
Compongo l'output del generatore (serializzabile):
```
Esercizio = { 'consegna': f'Seleziona i polinomi ordinati rispetto {var_consegna}.',
              'opzioni' : '\n'.join(['\to '+str(d['polinomio']) for d in risposte]),
    'soluzione_guidata' : '\n'.join(paragrafi),
    'risp_corrette_idx' : [i for i,r in enumerate(risposte) if r['verita']]
}
```

#### Esempio di testo generato
Ecco un esempio di generazione del testo di un esercizio.
```
Seleziona i polinomi ordinati rispetto b, y, z.
	o +12y^5 +8y^4 -12y^2
	o +3 -2z^2 -10z^3 -3z^4
	o -2b^2 -4b^5 +8b^3 -9 +6b^4
	o -3b^3 -9b^5
	o -2z^2 +7 +1z^1 +8z^4 +9z^5
	o +1y^4 -10y^3 +2 -5y^1
Un polinomio è ordinato rispetto a una lettera se i suoi termini sono ordinati secondo le potenze crescenti
(o decrescenti) di quella lettera: devi escludere i polinomi in cui gli esponenti di b, y, z non sono in ordine
crescente o decrescente.
Escludi quindi:
	o -2b^2 -4b^5 +8b^3 -9 +6b^4
	o -2z^2 +7 +1z^1 +8z^4 +9z^5
	o +1y^4 -10y^3 +2 -5y^1
I polinomi:
	o +3 -2z^2 -10z^3 -3z^4
	o -3b^3 -9b^5
sono ordinati secondo le potenze crescenti di b, z.
Infine, il polinomio:
	o +12y^5 +8y^4 -12y^2
è ordinato secondo le potenze decrescenti di y.
[0, 1, 3]
```
