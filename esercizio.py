import random
import itertools
import os
from mon import Mon
from pol import Pol

class Esercizio:
    def __init__(self, var = 'x', seed = None):
        """
        Metodo costruttore dell'esercizio secondo le precise indicazioni della
        traccia.

        Parametri
        ------------------------------------------------------------------------
        var : Variabile comune dei sei polinomi generati per l'esercizio.
                                                                   (Default 'x')
        seed: Seed usato per il modulo 'random' per garantire la riproducibilità
            dell'esercizio. Se assente viene generato e assegnato un seed random
            intero nell'intervallo [0, 1e6].
                                                                  (Default None)
        """

        if seed is None:
            self.seed = random.randint(0,1e6+1)
        elif isinstance(seed, int):
            self.seed = seed
        else:
            raise Exception("Il seed non è di tipo 'int'.")

        random.seed(self.seed)

        self.var = var
        self.risposte = self.gen_risposte(self.var)

        paragrafi = []
        risp1 = [d for d in self.risposte if not d['verita']]
        paragrafi.append(f'Un polinomio è ordinato rispetto a una lettera se i suoi termini sono ordinati secondo le potenze crescenti')
        paragrafi.append(f'(o decrescenti) di quella lettera: devi escludere i polinomi in cui gli esponenti di {var} non sono in ordine')
        paragrafi.append(f'crescente o decrescente.')
        paragrafi.append(f"Escludi quindi:\n\to {risp1[0]['polinomio']}\n\to {risp1[1]['polinomio']}\n\to {risp1[2]['polinomio']}")
        risp2 = [d for d in self.risposte if d['ordine'] == 'ASC']
        paragrafi.append(f"I polinomi:\n\to {risp2[0]['polinomio']}\n\to {risp2[1]['polinomio']}")
        paragrafi.append(f"sono ordinati secondo le potenze crescenti di {var}.")
        risp3 = [d for d in self.risposte if d['ordine'] == 'DESC']
        paragrafi.append(f"Infine, il polinomio:\n\to {risp3[0]['polinomio']}")
        paragrafi.append(f"è ordinato secondo le potenze decrescenti di {var}.")

        self.consegna          = f'Seleziona i polinomi ordinati rispetto {var}:'
        self.opzioni           = '\n'.join(['\to '+str(d['polinomio']) for d in self.risposte])
        self.soluzione_guidata = '\n'.join(paragrafi)
        self.risp_corrette_idx = 'Risposte corrette: ' + str([i for i,r in enumerate(self.risposte) if r['verita']])

    def __str__(self):
        return '\n\n'.join([self.consegna,
                            self.opzioni,
                            self.soluzione_guidata,
                            self.risp_corrette_idx])

    def gen_risposte(self, var):
        """
        Funzione che genera le sei risposte dell'esercizio secondo le condizioni
        indicate nella traccia.

        Parametri
        ------------------------------------------------------------------------
        var: La variabile dei polinomi dell'esercizio.

        Ritorna
        ------------------------------------------------------------------------
        Una lista di 6 dizionari dalla forma:
            [{'polinomio': +1y^3 +7y^5,
              'ordine'   : 'ASC',
              'verita'   : True }, ...]
        """
        nA, nB, nC = random.choice(list(itertools.permutations(range(2,5))))
        nD, nE, nF = [random.randint(3,5) for _ in range(3)]
        verita_opzione = lambda p: p.ordine in {'ASC', 'DESC'}

        polinomi = []
        polinomi.append(self.gen_pol(nA, var).sort(reverse=False))
        polinomi.append(self.gen_pol(nB, var).sort(reverse=False))
        polinomi.append(self.gen_pol(nC, var).sort(reverse=True))
        polinomi.append(self.gen_pol(nD, var).shuffle())
        polinomi.append(self.gen_pol(nE, var).shuffle())
        polinomi.append(self.gen_pol(nF, var).shuffle())

        risposte = [{'polinomio': p, 'ordine': p.ordine, 'verita': verita_opzione(p)} for p in polinomi]

        random.shuffle(risposte)
        return risposte

    def gen_pol(self, n_ele, var):
        """
        Funzione che restituisce un polinomio secondo gli standard dell'esercizio.

        Parametri
        ------------------------------------------------------------------------
        n_ele: Numero di elementi del polinomio.
        var  : La variabile dei polinomi del polinomio.

        Ritorna
        ------------------------------------------------------------------------
        Instanza della classe Pol con 'n_ele' elementi nell'incognita 'var'.

        Solleva
        ------------------------------------------------------------------------
        Exception: Se i paramteri in input non rispettano le condizioni per la
                generazione di un polinomio.
        """
        if (var in Mon.VAR_POOL and n_ele <= Mon.MAX_DEG + 1):
            coef_range = set(range(-12, 13))
            coef_range.remove(0)

            coefs   = random.sample(coef_range, n_ele)
            degrees = random.sample(set(range(Mon.MAX_DEG + 1)), n_ele)

        else:
            raise Exception('I parametri non soddisfano i requisiti per la creazione del polinomio.')

        return Pol([Mon(c,d,var) for c,d in zip(coefs, degrees)])

    def to_txt(self, path='.'):
        """
        Funzione che salva in formato '.txt' il testo dell'esercizio generato.

        Parametri
        ------------------------------------------------------------------------
        path: Percorso di salvataggio del file.
        """
        filename = 'espolord_' + self.var + str(self.seed)
        filepath = os.path.join(path, filename + ".txt")

        with open(filepath, 'w') as file:
            file.write(str(self))
