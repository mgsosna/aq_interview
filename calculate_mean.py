import sys
from typing import List

def mean(nums: List[float]) -> float:
    """
    Returns the mean of a list of numbers.
    """
    return sum(nums) / len(nums)

if __name__ == "__main__":
    nums = [float(x) for x in sys.argv[1:]]  # Convert from str args
    print(mean(nums))
