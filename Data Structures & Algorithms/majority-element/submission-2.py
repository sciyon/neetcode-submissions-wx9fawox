class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}

        for i, num in enumerate(nums):
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
            if seen[num] > len(nums) / 2:
                return num