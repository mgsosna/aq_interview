import sys
from typing import List

def mean(nums: List[int]) -> float:
    """
    Returns the mean of a list of numbers.
    """
    return sum(nums) / len(nums)

if __name__ == "__main__":
    nums = [int(x) for x in sys.argv[1:]]  # Convert str args to int
    print(mean(nums))
