import pytest
import os
from hypothesis import strategies as st
from hypothesis import given
from hypothesis import settings

from mon import Mon
from esercizio import Esercizio

#%%-----------------------------------------------------------------------------
#TEST COSTRUTTORE

@given(var  = st.sampled_from(list(Mon.VAR_POOL)),
       seed = st.integers(min_value=-1e6, max_value=1e6))
@settings(max_examples=10)
def test_esercizio_good_par(var, seed):
    es = Esercizio(var,seed)

@given(var  = st.sampled_from(list(Mon.VAR_POOL)),
       seed = st.sampled_from(list(Mon.VAR_POOL) + [1.5,-98.8]))
@settings(max_examples=10)
def test_esercizio_bad_par(var, seed):
    with pytest.raises(Exception):
        es = Esercizio(var,seed)

@given(var  = st.sampled_from(['d', 'e', 'f', 3, None]),
       seed = st.integers(min_value=-1e6, max_value=1e6))
@settings(max_examples=10)
def test_esercizio_bad_par2(var, seed):
    with pytest.raises(Exception):
        es = Esercizio(var,seed)

#%%-----------------------------------------------------------------------------
#TEST SEED

@given(var  = st.sampled_from(list(Mon.VAR_POOL)),
       seed = st.integers(min_value=-1e6, max_value=1e6))
@settings(max_examples=10)
def test_seed_esercizio(var, seed):
    es1 = Esercizio(var, seed)
    es2 = Esercizio(var, seed)
    assert str(es1) == str(es2)

@given(var  = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_seed_esercizio2(var):
    es1 = Esercizio(var)
    es2 = Esercizio(var)
    assert str(es1) != str(es2)

#%%-----------------------------------------------------------------------------
#TEST SALVATAGGIO SU .TXT

@given(var  = st.sampled_from(list(Mon.VAR_POOL)),
       seed = st.integers(min_value=-1e6, max_value=1e6))
@settings(max_examples=10)
def test_seed_esercizio(var, seed):
    es = Esercizio(var, seed)
    es.to_txt()

    filename = 'espolord_' + var + str(seed)
    filepath = os.path.join(filename + ".txt")

    with open( filepath, 'r') as f:
        s = ''.join([l for l in f])
        assert str(s) == str(es)
    os.remove(filepath)

#%%-----------------------------------------------------------------------------
#TEST GENERAZIONE POLINOMIO

@given(n_ele = st.integers(min_value=1, max_value=6),
       var   = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_gen_pol(n_ele, var):
    es = Esercizio(var)
    p = es.gen_pol(n_ele, var)
    assert p.ordine == None

@given(n_ele = st.integers(min_value=7, max_value=10),
       var   = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_gen_pol_bad(n_ele, var):
    es = Esercizio(var)
    with pytest.raises(Exception):
        p = es.gen_pol(n_ele, var)

#%%-----------------------------------------------------------------------------
#TEST GENERAZIONE RISPOSTE

@given(var = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_gen_risposte(var):
    es = Esercizio(var)
    risposte = es.risposte
    asc     = [r for r in risposte if r['ordine'] == 'ASC']
    des     = [r for r in risposte if r['ordine'] == 'DESC']
    shu     = [r for r in risposte if r['ordine'] == 'SHUFFLE']

    assert len(asc) == 2
    assert len(des) == 1
    assert len(shu) == 3

    for r in asc:
        p = r['polinomio']
        pre_check = p.mon_list.copy()
        post_sort = p.sort().mon_list.copy()
        assert pre_check == post_sort

    for r in des:
        p = r['polinomio']
        pre_check = p.mon_list.copy()
        post_sort = p.sort(reverse = True).mon_list.copy()
        assert pre_check == post_sort

    for r in shu:
        p = r['polinomio']
        pre_check = p.mon_list.copy()
        post_asc  = p.sort().mon_list.copy()
        post_des  = p.sort(reverse = True).mon_list.copy()
        #Il test passa perchè tutti gli shuffle hanno > 2 termini
        assert pre_check != post_asc
        assert pre_check != post_des

    true     = [r for r in risposte if r['verita'] ]
    false    = [r for r in risposte if not r['verita']]

    assert len(true)  == 3
    assert len(false) == 3

#%%-----------------------------------------------------------------------------
#TEST CONVERSIONE A STRINGA

@given(var  = st.sampled_from(list(Mon.VAR_POOL)),
       seed = st.integers(min_value=-1e6, max_value=1e6))
@settings(max_examples=10)
def test_str_esercizio(var, seed):
    es = Esercizio(var,seed)
    str_es = '\n\n'.join([es.consegna,
                          es.opzioni,
                          es.soluzione_guidata,
                          es.risp_corrette_idx])
    assert str(es) == str_es
