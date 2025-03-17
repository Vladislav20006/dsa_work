class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = {} # O(1)
        n = len(nums) #O(1)
        for i in range(n): #  O(n)
            k = target - nums[i]
            if k in c:
                return [c[k], i]
            c [nums[i]] = i
        return [] #O(n)