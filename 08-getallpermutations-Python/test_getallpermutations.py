from itertools import permutations
import pytest
from getallpermutations import getallpermutations
import os
import sys
sys.path.append(os.getcwd())


@pytest.mark.parametrize('x', [
    ("abc"), ("abcd"), ("ab"), ("abcde"),
    ("pqr"), ("pqrs"), ("pq"), ("pqrst"),
    ("xyz"), ("xyza"), ("xy"), ("xyzab"),
])
def test_getallpermutations(x):
    assert getallpermutations(x) == sorted(list(permutations(x, r=len(x))))
