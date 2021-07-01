class Mon:
    """
    Classe per la rappresentazione di un monomio ad una singola incognita.
    Sono presenti dei parametri a livello di classe per limitare i valori dei
    coefficienti, dei gradi e delle variabili ammissibili.
    """
    MAX_DEG = 5
    MIN_DEG = 0
    MAX_COEF = 12
    VAR_POOL = {'x', 'y', 'z', 'a', 'b', 'c'}

    def __init__(self, coef = 1, grado = 1, var = 'x'):
        """
        Metodo costruttore del singolo monomio.

        Parametri
        ------------------------------------------------------------------------
        coef : Coefficiente intero del monomio che deve rispettare le condizioni
               impostate a livello di classe.                        (Default 1)
        grado: Grado del monomio che deve rispettare le condizioni impostate a
               livello di classe.                                    (Default 1)
        var  : Variabile del polinomio che deve appartenere ai caratteri validi
               impostati a livello di classe.                      (Default 'x')

        Solleva
        ------------------------------------------------------------------------
        Exception: Se i parametri in input non rispettano le condizioni per la
                generazione di un monomio.
        """

        if (abs(coef) <= Mon.MAX_COEF and
            coef      != 0            and
            grado     >= 0            and
            grado     <= Mon.MAX_DEG  and
            var       in Mon.VAR_POOL):

            self.coef = coef
            self.grado = grado
            self.var = var
        else:
            raise Exception('Parametri non corretti per la creazione di un monomio')

    def __str__(self):

        segno = '+' if self.coef > 0 else '-'
        if self.grado > 1:
            lett = self.var + f'^{self.grado}'
        elif self.grado is 1:
            lett = self.var
        else:
            lett = ''

        return segno + f'{abs(self.coef)}' + lett
