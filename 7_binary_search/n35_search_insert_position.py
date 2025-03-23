class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) #O(1)
        while l < r: #O(n)
            m = (l + r)//2
            if nums[m] >= target: #O(1)
                r = m
            else:
                l = m + 1
        return l #O(1)