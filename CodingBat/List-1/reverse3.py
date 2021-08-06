"""
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.


reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]
"""


def reverse3(nums):
    for i in range(int(len(nums) / 2)):
        (nums[i], nums[len(nums) - i - 1]) = (nums[len(nums) - i - 1], nums[i])
    return nums


nums12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reverse3(nums12))
