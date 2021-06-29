# PythonDevTest

TUTTO BASATO SUL FATTO CHE SONO POLINOMI SONO IN UNA SOLA VARIABILE -> Una sola lettera per monomio e la stessa per tutto il polinomio
Altrimenti La classe Monomio avrebbe dovuto implementare
	una serie di lettere con corrispondente grado
	il concetto di grado dovrebbe essere la somma dei gradi di ogni lettera.

-----------------------------------------------------------------------------------------------------------------------

Layout esercizio:
	2 risp asc {nA, nB, nC} = Permutazioni{2, 3, 4}
	1 risp desc

	3 risp shuffle. nEl in range(2,4)

L'insieme di 6 coppie (ORD, nEL) definisce il materiale da generare
Funzione per stabilire VERO/FALSO?? permetterebbe di fare esercizi con tracce diverse sempre sui polinomi.

-----------------------------------------------------------------------------------------------------------------------
Esercizio:
INPUT:    Informazioni sulla generazione dei polinomi, funzione per VERITÀ
OUTPUT:   TUPLE(Polinomi, corrispondente verità)
CONSEGNA: Testo fisso in cui inserire l'incognita [x].
RISOLUZIONE GUIDATA: Testo fisso in cui inserire l'incognita [x] e i polinomi nel giusto ordine. Collegato con l'informazione per la generazione.
-----------------------------------------------------------------------------------------------------------------------

Esercizio
nA, nB, nC = random.shuffle(list(range(2,5))
nD, nE, nF = [random.randint(0,5) for _ in range(3)]

#Creo le sei opzioni come da consegna
polinomi = []
polinomi.append(Pol(nA).sort(reverse=False))
polinomi.append(Pol(nB).sort(reverse=False))
polinomi.append(Pol(nC).sort(reverse=True))
polinomi.append(Pol(nD).shuffle())
polinomi.append(Pol(nE).shuffle())
polinomi.append(Pol(nF).shuffle())

verita_opzione = lambda p: p.ordinamento is in {'ASC', 'DESC'}

opzioni = [(p, verita_opzione(p)) for p in polinomi]
random.shuffle(opzioni)
