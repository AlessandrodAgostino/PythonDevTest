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
p = get_pol(5)
print(p)
p.sort()
print(p)
p.shuffle()
print(p)
p.sort(reverse=True)
print(p)
