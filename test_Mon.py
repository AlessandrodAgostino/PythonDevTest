import pytest

from hypothesis import strategies as st
from hypothesis import given
from hypothesis import settings

from mon import Mon
#%%----------------------------------------------------------------------------
@given(coef   = st.integers(min_value=-1*Mon.MAX_COEF, max_value=Mon.MAX_COEF),
       degree = st.integers(min_value=0, max_value=Mon.MAX_DEG),
       var    = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_good_par(coef, degree, var):
    v = Mon(coef,degree,var)

@given(coef   = st.integers(min_value= Mon.MAX_COEF +1, max_value=2 * Mon.MAX_COEF),
       degree = st.integers(min_value=0, max_value=Mon.MAX_DEG),
       var    = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_bad_par1(coef, degree, var):
    with pytest.raises(Exception):
        v = Mon(coef,degree,var)

@given(coef   = st.integers(min_value= -2 * Mon.MAX_COEF, max_value= -1 * Mon.MAX_COEF -1),
       degree = st.integers(min_value=0, max_value=Mon.MAX_DEG),
       var    = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_bad_par2(coef, degree, var):
    with pytest.raises(Exception):
        v = Mon(coef,degree,var)

@given(coef   = st.integers(min_value=-1*Mon.MAX_COEF, max_value=Mon.MAX_COEF),
       degree = st.integers(min_value=Mon.MAX_DEG +1, max_value= 2 * Mon.MAX_DEG),
       var    = st.sampled_from(list(Mon.VAR_POOL)))
@settings(max_examples=10)
def test_bad_par3(coef, degree, var):
    with pytest.raises(Exception):
        v = Mon(coef,degree,var)

@given(coef   = st.integers(min_value=-1*Mon.MAX_COEF, max_value=Mon.MAX_COEF),
       degree = st.integers(min_value=0, max_value=Mon.MAX_DEG),
       var    = st.sampled_from(['d', 'e', 'f']))
@settings(max_examples=10)
def test_bad_par4(coef, degree, var):
    with pytest.raises(Exception):
        v = Mon(coef,degree,var)

#test operatori lt, le, gt, ge
