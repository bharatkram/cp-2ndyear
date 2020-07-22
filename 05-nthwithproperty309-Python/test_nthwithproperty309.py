import pytest
from nthwithproperty309 import nthwithproperty309
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('result, x', [
    (309, 0),
    (418, 1),
    (462, 2),
    (474, 3),
    (575, 4),
    (635, 5),
    (662, 6),
    (2014, 100),
    (7813, 1000)
])
def test_nthwithproperty309(x, result):
    assert nthwithproperty309(x) == result
