class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights) #O(n)
        a = 0 #O(1)
        for i in range(len(heights)): #O(n)
            if heights[i] != expected[i]: #O(1)
                a += 1
        return a