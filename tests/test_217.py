import random

import pytest

from leetcode.decorators import timed
from leetcode.utils import get_functions

func_name = "get_concatenation"


@pytest.fixture(params=get_functions(__name__, func_name))
def function(request):
    return request.param


@pytest.fixture(params=[
    (True, [1, 2, 3, 1]),
    (False, [1, 2, 3, 4]),
    (True, [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]),
    (True, [random.randint(0, 999) for i in range(10000)])
])
def test_variables(request):
    return request.param


@timed
def test_contains_duplicate(test_variables, function):
    expected, nums = test_variables
    assert function(nums) == expected
