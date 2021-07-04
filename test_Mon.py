import pytest
from hypothesis import strategies as st
from hypothesis import given
from hypothesis import settings
from mon import Mon

#%%-----------------------------------------------------------------------------
#TEST PARAMETRI COSTRUTTORE CORRETTI

@given(coef   = st.integers(min_value=1, max_value=Mon.MAX_COEF),
       grado  = st.integers(min_value=0, max_value=Mon.MAX_DEG),
       var    = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_good_par1(coef, grado, var):
    v = Mon(coef,grado,var)

@given(coef   = st.integers(min_value=-1*Mon.MAX_COEF, max_value=-1),
       grado  = st.integers(min_value=0, max_value=Mon.MAX_DEG),
       var    = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_good_par2(coef, grado, var):
    v = Mon(coef,grado,var)

#%%-----------------------------------------------------------------------------
#TEST PARAMETRI COSTRUTTORE ERRATI

@given(coef   = st.integers(min_value=Mon.MAX_COEF+1, max_value=2*Mon.MAX_COEF),
       grado  = st.integers(min_value=0, max_value=Mon.MAX_DEG),
       var    = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_bad_coef1(coef, grado, var):
    with pytest.raises(Exception):
        v = Mon(coef,grado,var)

@given(coef   = st.integers(min_value=-2*Mon.MAX_COEF, max_value=-1*Mon.MAX_COEF-1),
       grado  = st.integers(min_value=0, max_value=Mon.MAX_DEG),
       var    = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_bad_coef2(coef, grado, var):
    with pytest.raises(Exception):
        v = Mon(coef,grado,var)

@given(coef   = st.integers(min_value=0, max_value=0),
       grado  = st.integers(min_value=0, max_value=Mon.MAX_DEG),
       var    = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_bad_coef3(coef, grado, var):
    with pytest.raises(Exception):
        v = Mon(coef,grado,var)

@given(coef   = st.integers(min_value=-1*Mon.MAX_COEF, max_value=Mon.MAX_COEF),
       grado  = st.integers(min_value=Mon.MAX_DEG+1, max_value=2*Mon.MAX_DEG),
       var    = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_bad_grad1(coef, grado, var):
    with pytest.raises(Exception):
        v = Mon(coef,grado,var)

@given(coef   = st.integers(min_value=-1*Mon.MAX_COEF, max_value=Mon.MAX_COEF),
       grado  = st.integers(min_value=-2*Mon.MAX_DEG, max_value=-1),
       var    = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_bad_grad2(coef, grado, var):
    with pytest.raises(Exception):
        v = Mon(coef,grado,var)

@given(coef   = st.integers(min_value=-1*Mon.MAX_COEF, max_value=Mon.MAX_COEF),
       grado  = st.integers(min_value=0, max_value=Mon.MAX_DEG),
       var    = st.sampled_from(['d', 'e', 'f', 3, None]))
@settings(max_examples=10)
def test_bad_var1(coef, grado, var):
    with pytest.raises(Exception):
        v = Mon(coef,grado,var)

#%%-----------------------------------------------------------------------------
#TEST CONVERSIONE A STRINGA

@given(coef   = st.integers(min_value=-1*Mon.MAX_COEF, max_value=-1),
       grado  = st.integers(min_value=2, max_value=Mon.MAX_DEG),
       var    = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_str1(coef, grado, var):
    v = Mon(coef,grado,var)
    v_str = str(v)
    assert v_str[0] == '-'
    assert v_str[-1] == str(grado)
    assert var in v_str
    assert '^' in v_str

@given(coef   = st.integers(min_value=1, max_value=Mon.MAX_COEF),
       grado  = st.integers(min_value=2, max_value=Mon.MAX_DEG),
       var    = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_str2(coef, grado, var):
    v = Mon(coef,grado,var)
    v_str = str(v)
    assert v_str[0] == '+'
    assert v_str[-1] == str(grado)
    assert var in v_str
    assert '^' in v_str

@given(coef   = st.integers(min_value=1, max_value=Mon.MAX_COEF),
       grado  = st.integers(min_value=2, max_value=Mon.MAX_DEG),
       var    = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_str3(coef, grado, var):
    v = Mon(coef,grado,var)
    v_str = str(v)
    assert v_str[0] == '+'
    assert v_str[-1] == str(grado)
    assert var in v_str
    assert '^' in v_str

@given(coef   = st.integers(min_value=1, max_value=Mon.MAX_COEF),
       grado  = st.integers(min_value=1, max_value=1),
       var    = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_str4(coef, grado, var):
    v = Mon(coef,grado,var)
    v_str = str(v)
    assert v_str[0] == '+'
    assert var in v_str
    assert '^' not in v_str

@given(coef   = st.integers(min_value=1, max_value=Mon.MAX_COEF),
       grado  = st.integers(min_value=0, max_value=0),
       var    = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_str4(coef, grado, var):
    v = Mon(coef,grado,var)
    v_str = str(v)
    assert v_str[0] == '+'
    assert var not in v_str
    assert '^' not in v_str

@given(coef   = st.sampled_from([-1,1]),
       grado  = st.integers(min_value=1, max_value=Mon.MAX_DEG),
       var    = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_str5(coef, grado, var):
    v = Mon(coef,grado,var)
    v_str = str(v)
    assert v_str[0] in {'+', '-'}
    assert '1' not in v_str

@given(coef   = st.sampled_from([-1,1]),
       grado  = st.integers(min_value=0, max_value=0),
       var    = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_str6(coef, grado, var):
    v = Mon(coef,grado,var)
    v_str = str(v)
    assert v_str[0] in {'+', '-'}
    assert '1' in v_str
