class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in comp:
                return [comp[complement], i]
            comp[n] = i