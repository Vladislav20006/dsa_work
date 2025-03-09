class Solution:
    def sortArray(self, nums: list[int]) -> list[int]: 
        a, Set, max, min = [],set(nums),nums[0],nums[0] #O(n)
        d = {n:0 for n in Set} #O(n)
        for n in nums: d[n]+= 1 #O(n)

        for n in d: #O(n)
            if n > max: max = n #O(1)
            if n < min: min = n #O(1)

        for i in range(min, max+1): #O(n)
            if i not in d: continue #O(1)
            a+= [i]*d[i]

        return a