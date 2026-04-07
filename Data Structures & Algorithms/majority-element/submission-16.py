class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        threshold = len(nums) // 2 

        for num in nums:
            seen[num]=seen.get(num, 0) + 1
            if seen[num] > threshold:
                return num