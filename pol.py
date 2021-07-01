import random

class Pol:
    def __init__(self, mon_list):
        """
        Metodo costruttore del singolo polinomio a una singola variabile.
        Il polinomio è sostanzialmente costituito da una lista di monomi, che
        deve superare alcuni controlli per garantire la diversità dei gradi e la
        omogeneità della varaibile.

        Parametri
        ------------------------------------------------------------------------
        mon_list: Lista di monomi da controllare. Tutti i gradi devono essere
                diversi e la variabile deve essere comune.

        Solleva
        ------------------------------------------------------------------------
        Exception: Se il paramtero in input non rispetta le condizioni per la
                generazione di un polinomio.
        """
        vars    = [m.var    for m in mon_list]
        degrees = [m.grado for m in mon_list]

        if (len(set(vars)) == 1 and                  #Controllo variabile uguale
            len(degrees)   == len(set(degrees))):    #Controllo gradi diversi
            self.mon_list = mon_list
            self.ordine = None
        else:
            raise Exception('La lista di monomi non soddisfa i requisiti per la creazione del polinomio.')

    def __str__(self):
        return ' '.join([str(p) for p in self.mon_list])

    def sort(self, reverse=False):
        """
        Metodo per l'ordinamento crescente o decrescente della lista di monomi
        rispetto al loro grado. Se l'operazione va a buon fine viene valorizzato
        di conseguenza il parametro 'self.ordine' a 'ASC' p 'DESC'.

        Parametri
        ------------------------------------------------------------------------
        reverse: Parametro per ordine decrescente del polinomio. (Default False)

        Ritorna
        ------------------------------------------------------------------------
        self: Il metodo ritorna l'istanza chiamante.
        """
        self.mon_list.sort(reverse=reverse, key = lambda m : m.grado)
        self.ordine = 'DESC' if reverse else 'ASC'
        return self

    def shuffle(self):
        """
        Metodo per il 'disordinamento' della lista di monomi rispetto al loro
        grado. Se la lista di monomi ha più di due elementi viene eseguito un
        ciclo di controllo per assicurarsi che non sia stato raggiunto
        accidentalmente l'ordinamento del polinomio. Se l'operazione va a buon
        fine viene valorizzato il parametro 'self.ordine' a 'SHUFFLE'.

        Ritorna
        ------------------------------------------------------------------------
        self: Il metodo ritorna l'istanza chiamante.
        """

        l = len(self.mon_list)
        if   l == 1:
            pass
        elif l == 2: # Inverto gli elementi
            self.mon_list.reverse()
        elif l == 3: # Cerco l'unica opzione non ordinata
            while (self.mon_list == sorted(self.mon_list, key = lambda m : m.grado, reverse=True) or
                   self.mon_list == sorted(self.mon_list, key = lambda m : m.grado, reverse=False)):
                   random.shuffle(self.mon_list)
        elif l > 3:  # Cerco un'opzione non ordinata diversa da quella iniziale
            pre_shuffle = self.mon_list.copy()
            while (self.mon_list == sorted(self.mon_list, key = lambda m : m.grado, reverse=True) or
                   self.mon_list == sorted(self.mon_list, key = lambda m : m.grado, reverse=False) or
                   self.mon_list == pre_shuffle):
                   random.shuffle(self.mon_list)

        self.ordine = 'SHUFFLE'
        return self
