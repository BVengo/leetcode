"""
Given an integer array nums, return true if any value appears at least
twice in the array, and return false if every element is distinct.
"""


def contains_duplicate_v1(nums):
    """
    Using sets
    """
    return len(nums) != len(set(nums))


def contains_duplicate_v2(nums):
    """
    Sorting, then iterating

    !SLOWEST
    """
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False


def contains_duplicate_v3(nums):
    """
    Using a dictionary

    !FASTEST
    """
    seen = {}
    for i in nums:
        if i in seen:
            return True

        seen[i] = 1
    return False
