import pytest

from leetcode.decorators import timed
from leetcode.utils import get_functions

func_name = "get_concatenation"


@pytest.fixture(params=get_functions(__name__, func_name))
def function(request):
    return request.param


@pytest.fixture(params=[
    (True, ("anagram", "nagaram")),  # Given
    (False, ("rat", "car")),  # Given
    (True, ("", "")),  # Empty is valid
    (False, ("a"*5000, "b"*5000)),  # Easiest for iterators
    (True, ("a"*5000, "a"*5000))  # Hardest for iterators
])
def test_variables(request):
    return request.param


@timed
def test_is_anagram(test_variables, function):
    expected, (s, t) = test_variables
    assert function(s, t) == expected
