class Solution:
    def sortArray(self, nums: list[int]) -> list[int]: 
        a, Set, max, min = [],set(nums),nums[0],nums[0]
        d = {n:0 for n in Set}
        for n in nums: d[n]+= 1

        for n in d:
            if n > max: max = n
            if n < min: min = n

        for i in range(min, max+1):
            if i not in d: continue
            a+= [i]*d[i]

        return a