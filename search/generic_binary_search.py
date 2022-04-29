"""
## Generic Binary Search

Here is the general strategy behind binary search, which is applicable to a variety of problems:

1. Come up with a condition to determine whether the answer lies before, after or at a given position
1. Retrieve the midpoint and the middle element of the list.
2. If it is the answer, return the middle position as the answer.
3. If answer lies before it, repeat the search with the first half of the list
4. If the answer lies after it, repeat the search with the second half of the list.

Here is the generic algorithm for binary search, implemented in Python:
"""

from core import evaluate_test_cases
from search import tests


def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def locate_card(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid - 1] == query:
                return 'left'
            else:
                return 'found'
        elif cards[mid] < query:
            return 'left'
        else:
            return 'right'

    return binary_search(0, len(cards) - 1, condition)


"""
The `binary_search` function can now be used to solve other problems too. It is a tested piece of logic.


> **Question**: Given an array of integers nums sorted in ascending order, find the starting and ending position of a given number.

This differs from the problem in only two significant ways:

1. The numbers are sorted in increasing order.
2. We are looking for both the increasing order and the decreasing order.

Here's the full code for solving the question, obtained by making minor modifications to our previous function:
"""


def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid - 1] == target:
                return 'left'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'

    return binary_search(0, len(nums) - 1, condition)


def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums) - 1 and nums[mid + 1] == target:
                return 'right'
            return 'found'
        elif nums[mid] < target:
            return 'right'
        else:
            return 'left'

    return binary_search(0, len(nums) - 1, condition)


def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)


if __name__ == '__main__':
    evaluate_test_cases(locate_card, tests)
