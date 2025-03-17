from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        l, r = 0, len(s) - 1 #O(n)
        while l < r: #O(n)
            s[l], s[r] = s[r], s[l] #O(1)
            l += 1
            r -= 1