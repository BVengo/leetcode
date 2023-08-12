"""
Given two strings s and t, determine if they are anagrams.    
"""
from collections import Counter


def is_anagram_v1(s: str, t: str):
    """
    Using sorted
    """
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)


def is_anagram_v2(s: str, t: str):
    """
    Using Counter from collections (i.e. hash table of counts)
    !SLOWEST
    """
    if len(s) != len(t):
        return False

    return Counter(s) == Counter(t)


def is_anagram_v3(s: str, t: str):
    """
    Using sets
    !FASTEST - especially for long strings
    """
    if len(s) != len(t):
        return False

    for c in set(s):
        if s.count(c) != t.count(c):
            return False

    return True
