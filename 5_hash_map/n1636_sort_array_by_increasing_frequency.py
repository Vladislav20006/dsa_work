class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        s = Counter(nums) #O(n)
        t = {} #O(n)
        for i, j in s.items(): #O(n)
            if j not in t: #O(1)
                t[j] = [i]
            else: #O(1)
                t[j] += [i]
        a = [] #O(n)
        for x in sorted(t): #O(1)
            a.extend(sorted(x*t[x], reverse = True))
        return a