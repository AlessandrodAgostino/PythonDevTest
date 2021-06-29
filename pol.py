import random

class Pol:
    def __init__(self, mon_list):
        """
        Controllo che non ci siano monomi di grado ripetuto.
        Controllo che non ci siano monomi con variabili diverse.
        """
        vars    = [m.var    for m in mon_list]
        degrees = [m.degree for m in mon_list]

        if (len(set(vars)) == 1 and                  #Controllo variabile uguale
            len(degrees)   == len(set(degrees))):  #Controllo gradi diversi
            self.mon_list = mon_list
            self.ordine = None
        else:
            raise Exception('La lista di monomi non soddisfa i requisiti per la creazione del polinomio.')

    def __str__(self):
        return ' '.join([p.__str__() for p in self.mon_list])

    def sort(self, reverse=False):
        self.mon_list.sort(reverse=reverse, key = lambda m : m.degree)
        self.ordine = 'DESC' if reverse else 'ASC'

    def shuffle(self, hard = True):
        """
        hard: Make sure the polynomial is not sorted, default True.
        """
        random.shuffle(self.mon_list)
        while (self.mon_list == sorted(self.mon_list, key = lambda m : m.degree, reverse=True) or
               self.mon_list == sorted(self.mon_list, key = lambda m : m.degree, reverse=False)):
               random.shuffle(self.mon_list)
               print('hard shuffle')
        self.ordine = 'SHUFFLE'
