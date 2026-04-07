class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}

        for i, num in enumerate(nums):
            if num not in seen:
                seen[num] = 1
            if num in seen and seen[num] > len(nums) / 2:
                return num
            else:
                seen[num] += 1