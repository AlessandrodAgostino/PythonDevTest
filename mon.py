class Mon:
    MAX_DEG = 5
    MIN_DEG = 0
    MAX_COEF = 12
    VAR_POOL = {'x', 'y', 'z', 'a', 'b', 'c'}

    def __init__(self, coef = 1, degree = 1, var = 'x'):

        if (abs(coef) <= Mon.MAX_COEF and
           degree >= 0                and
           degree <= Mon.MAX_DEG      and
           var in Mon.VAR_POOL):
            self.coef = coef
            self.degree = degree
            self.var = var
        else:
            raise Exception('Parametri non corretti per la creazione di un monomio')

    def __str__(self):

        if self.coef == 0:
            return '+0'
            #return ''

        sign = '+' if self.coef > 0 else '-'
        if self.degree is not 0:
            lett = self.var + f'^{self.degree}'
        else:
            lett = ''

        return sign + f'{abs(self.coef)}' + lett

    def __lt__(self, other):
        return self.degree < other.degree

    def __gt__(self, other):
        return self.degree > other.degree

    def __le__(self, other):
        return self.degree <= other.degree

    def __ge__(self, other):
        return self.degree >= other.degree
