import random
from mon import Mon
from pol import Pol

def get_random_mon():
    m = Mon()
    m.coef   = random.randint(-1* Mon.MAX_COEF, Mon.MAX_COEF)
    m.degree = random.randint( 0, Mon.MAX_DEG)
    m.var    = random.sample(Mon.VAR_POOL, 1)[0]
    return m

def get_pol(n_ele):
    return Pol([get_random_mon() for _ in range(n_ele)])

#Per evitare la ripetizione dei gradi usare:
#import random
#random.sample(range(100), 10)

#%%
# Prove Sort asc/desc e shuffle
p = get_pol(3)
print(p)
vars    = [m.var    for m in p.mon_list]
vars


p.sort()
print(p)
p.shuffle()
print(p)
p.sort(reverse=True)
print(p)
#%%-----------------------------------------------------------------------------
##     ESERCIZIO    ------------------------------------------------------------
#%%-----------------------------------------------------------------------------

coefs = list(range(2,5))
random.shuffle(coefs)
nA, nB, nC = coefs
nD, nE, nF = [random.randint(2,5) for _ in range(3)]

#Creo le sei opzioni come da consegna
polinomi = []
polinomi.append(get_pol(nA).sort(reverse=False))
polinomi.append(get_pol(nB).sort(reverse=False))
polinomi.append(get_pol(nC).sort(reverse=True))
polinomi.append(get_pol(nD).shuffle())
polinomi.append(get_pol(nE).shuffle())
polinomi.append(get_pol(nF).shuffle())

verita_opzione = lambda p: p.ordinamento is in {'ASC', 'DESC'}

opzioni = [(p, verita_opzione(p)) for p in polinomi]
random.shuffle(opzioni)
#%%
p = get_pol(3)
print('originale', p)
p.shuffle()
print('shuffle', p)
p.ordine
p.sort()
print('sort', p)
p.ordine
p.shuffle()
print('shuffle', p)
#%%
vars = [4,4]
len(set(vars))
