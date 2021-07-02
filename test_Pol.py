import pytest
import random
from hypothesis import strategies as st
from hypothesis import given
from hypothesis import settings

from pol import Pol
from mon import Mon

def gen_pol(n_ele, var):
    coef_range = set(range(-12, 13))
    coef_range.remove(0)

    coefs   = random.sample(coef_range, n_ele)
    degrees = random.sample(set(range(Mon.MAX_DEG + 1)), n_ele)

    return Pol([Mon(c,d,var) for c,d in zip(coefs, degrees)])

#%%-----------------------------------------------------------------------------
#TEST PARAMETRI COSTRUTTORE CORRETTI

@given(n_ele = st.integers(min_value=1, max_value=Mon.MAX_DEG + 1),
       var   = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_good_pol1(n_ele, var):
    p = gen_pol(n_ele, var)
    assert p.ordine is None

#%%-----------------------------------------------------------------------------
#TEST PARAMETRI COSTRUTTORE ERRATI

@given(n_ele = st.integers(min_value=0, max_value=0),
       var   = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_empty_mon_list(n_ele, var):
    with pytest.raises(Exception):
        p = gen_pol(n_ele, var)
        assert p.ordine is None

@given(n_ele = st.integers(min_value=7, max_value=10),
       var   = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_too_many_degrees(n_ele, var):
    with pytest.raises(Exception):
        p = gen_pol(n_ele, var)
        assert p.ordine is None

@given(n_ele = st.integers(min_value=1, max_value=Mon.MAX_DEG + 1),
       var    = st.sampled_from(['d', 'e', 'f', 3, None]))
@settings(max_examples=10)
def test_wrong_var(n_ele, var):
    with pytest.raises(Exception):
        p = gen_pol(n_ele, var)
        assert p.ordine is None

#%%-----------------------------------------------------------------------------
#TEST CONVERSIONE A STRINGA

@given(n_ele = st.integers(min_value=1, max_value=Mon.MAX_DEG + 1),
       var   = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_str_pol1(n_ele, var):
    p = gen_pol(n_ele, var)
    p_str = p.__str__()
    assert p_str.count(var) <= n_ele
    assert p_str.count(var) >= n_ele - 1

    if p_str[0] is '+':
        assert p_str.count('+') + p_str.count('-') == n_ele -1
    else:
        assert p_str.count('+') + p_str.count('-') == n_ele
    assert p_str.count(' ') == n_ele -1

#%%-----------------------------------------------------------------------------
#TEST METODO SORT

@given(n_ele = st.integers(min_value=1, max_value=Mon.MAX_DEG + 1),
       var   = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_sort(n_ele, var):
    p = gen_pol(n_ele, var)
    assert p.ordine is None
    post1_sort  = p.sort().mon_list.copy()
    post2_sort  = p.sort().mon_list
    assert post1_sort == post2_sort
    assert p.ordine is 'ASC'

    post1_sort  = p.sort(reverse = True).mon_list.copy()
    post2_sort  = p.sort(reverse = True).mon_list
    assert post1_sort == post2_sort
    assert p.ordine is 'DESC'

@given(n_ele = st.integers(min_value=2, max_value=Mon.MAX_DEG + 1),
       var   = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_diff_sort(n_ele, var):
    p = gen_pol(n_ele, var)
    assert p.ordine is None
    post1_sort  = p.sort().mon_list.copy()
    assert p.ordine is 'ASC'
    post2_sort  = p.sort(reverse = True).mon_list.copy()
    assert post1_sort != post2_sort
    assert p.ordine is 'DESC'

#%%-----------------------------------------------------------------------------
#TEST METODO SHUFFLE

@given(n_ele = st.integers(min_value=3, max_value=Mon.MAX_DEG + 1),
       var   = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_shuffle1(n_ele, var):
    p = gen_pol(n_ele, var)
    assert p.ordine is None
    post_shuffle = p.shuffle().mon_list.copy()
    post_sort    = p.sort().mon_list.copy()
    assert post_shuffle != post_sort
    post_sort    = p.sort(reverse = True).mon_list.copy()
    assert post_shuffle != post_sort

@given(n_ele = st.integers(min_value=4, max_value=Mon.MAX_DEG + 1),
       var   = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_shuffle2(n_ele, var):
    p = gen_pol(n_ele, var)
    assert p.ordine is None
    pre_shuffle  = p.mon_list.copy()
    post_shuffle = p.shuffle().mon_list.copy()
    assert pre_shuffle != post_shuffle

    post_sort    = p.sort().mon_list.copy()
    assert post_shuffle != post_sort
    post_sort    = p.sort(reverse = True).mon_list.copy()
    assert post_shuffle != post_sort

@given(n_ele = st.integers(min_value=2, max_value=2),
       var   = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_shuffle3(n_ele, var):
    p = gen_pol(n_ele, var)
    assert p.ordine is None
    pre_shuffle  = p.mon_list.copy()
    post_shuffle = p.shuffle().mon_list.copy()
    assert pre_shuffle != post_shuffle

@given(n_ele = st.integers(min_value=1, max_value=1),
       var   = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_shuffle4(n_ele, var):
    p = gen_pol(n_ele, var)
    assert p.ordine is None
    pre_shuffle  = p.mon_list.copy()
    post_shuffle = p.shuffle().mon_list.copy()
    assert pre_shuffle == post_shuffle
    post_sort    = p.sort().mon_list.copy()
    assert post_shuffle == post_sort
    post_sort    = p.sort(reverse = True).mon_list.copy()
    assert post_shuffle == post_sort
