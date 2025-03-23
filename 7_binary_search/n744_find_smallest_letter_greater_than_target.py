class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1 #O(1)
        if target >= letters[-1]: #O(1)
            return letters[0]
        while l <= r: #O(n)
            m = l + (r - l) // 2
            if letters[m] > target: #O(1)
                r = m - 1
            else:
                l = m + 1
        return letters[l] #O(1)