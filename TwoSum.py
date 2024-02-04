from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}  # Hash map to store the numbers and their indices

        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement is in the hash map
            if complement in num_dict:
                # Return the zero-based indices of the two numbers that add up to the target
                return [num_dict[complement], i]

            # Store the current number and its index in the hash map
            num_dict[num] = i  # Using zero-based index

        # If no solution is found, return an empty list
        return []



