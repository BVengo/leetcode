"""
Given an integer array nums of length n, you want to create an array
ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i]
for 0 <= i < n (0-indexed).

i.e. concatenate the array with itself
"""


def get_concatenation_v1(nums: list[int]) -> int:
    """
    Just in-built concatenation
    """
    return nums + nums


def get_concatenation_v2(nums: list[int]) -> int:
    """
    Concatenate manually via copy
    """
    ans = nums.copy()
    for num in nums:
        ans.append(num)
    return ans


def get_concatenation_v3(nums: list[int]) -> int:
    """
    Concatenate manually without copy
    !SLOWEST
    """
    ans = []

    for num in nums:
        ans.append(num)

    for num in nums:
        ans.append(num)

    return ans


def get_concatenation_v4(nums: list[int]) -> int:
    """
    Concatenate by assigning a slice
    """
    ans = nums.copy()
    ans[0:0] = nums

    return ans


def get_concatenation_v5(nums: list[int]) -> int:
    """
    List multiplication
    !FASTEST
    """
    return nums * 2


def get_concatenation_v6(nums: list[int]) -> int:
    """
    List extension
    """
    ans = []
    ans.extend(nums)
    ans.extend(nums)
    return ans
