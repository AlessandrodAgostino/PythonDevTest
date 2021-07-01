import random
import itertools
from mon import Mon
from pol import Pol

def gen_pol(n_ele, var):
    coef_range = set(range(-12, 13))
    coef_range.remove(0)

    coefs   = random.sample(coef_range, n_ele)
    degrees = random.sample(set(range(6)), n_ele)

    return Pol([Mon(c,d,var) for c,d in zip(coefs, degrees)])

def gen_risposte():
    nA, nB, nC = random.choice(list(itertools.permutations(range(2,5))))
    nD, nE, nF = [random.randint(3,5) for _ in range(3)]
    verita_opzione = lambda p: p.ordine in {'ASC', 'DESC'}

    #Creo le sei risposte come da consegna
    polinomi = []
    polinomi.append(gen_pol(nA, var=random.choice(list(Mon.VAR_POOL))).sort(reverse=False))
    polinomi.append(gen_pol(nB, var=random.choice(list(Mon.VAR_POOL))).sort(reverse=False))
    polinomi.append(gen_pol(nC, var=random.choice(list(Mon.VAR_POOL))).sort(reverse=True))
    polinomi.append(gen_pol(nD, var=random.choice(list(Mon.VAR_POOL))).shuffle())
    polinomi.append(gen_pol(nE, var=random.choice(list(Mon.VAR_POOL))).shuffle())
    polinomi.append(gen_pol(nF, var=random.choice(list(Mon.VAR_POOL))).shuffle())

    risposte = [{'polinomio': p, 'ordine': p.ordine, 'verita': verita_opzione(p)} for p in polinomi]
    #TODO: Aggiungere campo 'variabile' per snellire la sintassi successiva
    random.shuffle(risposte)
    return risposte

#%%-----------------------------------------------------------------------------
risposte = gen_risposte()

var_consegna = ', '.join(sorted(set([d['polinomio'].mon_list[0].var for d in risposte])))

paragrafi = []
risp1 = [d for d in risposte if not d['verita']]
var1 = ', '.join(sorted(set([d['polinomio'].mon_list[0].var for d in risp1])))
paragrafi.append(f'Un polinomio è ordinato rispetto a una lettera se i suoi termini sono ordinati secondo le potenze crescenti')
paragrafi.append(f'(o decrescenti) di quella lettera: devi escludere i polinomi in cui gli esponenti di {var1} non sono in ordine')
paragrafi.append(f'crescente o decrescente.')
paragrafi.append(f"Escludi quindi:\n\to {risp1[0]['polinomio']}\n\to {risp1[1]['polinomio']}\n\to {risp1[2]['polinomio']}")
risp2 = [d for d in risposte if d['ordine'] == 'ASC']
var2 = ', '.join(sorted(set([d['polinomio'].mon_list[0].var for d in risp2])))
paragrafi.append(f"I polinomi:\n\to {risp2[0]['polinomio']}\n\to {risp2[1]['polinomio']}")
paragrafi.append(f"sono ordinati secondo le potenze crescenti di {var2}.")
risp3 = [d for d in risposte if d['ordine'] == 'DESC']
var3 = risp3[0]['polinomio'].mon_list[0].var
paragrafi.append(f"Infine, il polinomio:\n\to {risp3[0]['polinomio']}")
paragrafi.append(f"è ordinato secondo le potenze decrescenti di {var3}.")

#%%-----------------------------------------------------------------------------

Esercizio = { 'consegna': f'Seleziona i polinomi ordinati rispetto {var_consegna}.',
              'opzioni' : '\n'.join(['\to '+str(d['polinomio']) for d in risposte]),
    'soluzione_guidata' : '\n'.join(paragrafi),
    'risp_corrette_idx' : [i for i,r in enumerate(risposte) if r['verita']]
}

for v in Esercizio.values():
    print(v)
