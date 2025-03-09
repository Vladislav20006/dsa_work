class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        d = Counter(arr) #O(n)
        for num in target: #O(n)
            if num not in d or not d[num]: #O(1)
                return False 
            d[num] -= 1 #O(1)
        return True