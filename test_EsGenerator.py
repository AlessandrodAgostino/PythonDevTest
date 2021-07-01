import pytest
from hypothesis import strategies as st
from hypothesis import given
from hypothesis import settings

import EsGenerator
from mon import Mon

#%%-----------------------------------------------------------------------------
#TEST GENERAZIONE RISPOSTE

@given(var   = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_gen_risposte(var):
    risposte = EsGenerator.gen_risposte(var)
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
