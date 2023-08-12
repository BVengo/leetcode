import pytest

from leetcode.decorators import timed
from leetcode.utils import get_functions

func_name = "get_concatenation"


@pytest.fixture(params=get_functions(__name__, func_name))
def function(request):
    return request.param


@pytest.fixture(params=[
    (
        [1, 2, 1, 1, 2, 1],
        [1, 2, 1]
    ),
    (
        [1, 3, 2, 1, 1, 3, 2, 1],
        [1, 3, 2, 1]
    ),
    (
        [1 for _ in range(10000)],
        [1 for _ in range(5000)]
    )
])
def test_variables(request):
    return request.param


@timed
def test_get_concatenation(test_variables, function):
    expected, nums = test_variables
    assert function(nums) == expected
