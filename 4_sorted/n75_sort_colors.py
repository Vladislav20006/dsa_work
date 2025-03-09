class Solution:
    def sortColors(self, a: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0 #O(n)
        left = 0 #O(n)
        right = len(a) - 1 #O(n)
        while n <= right: #O(n)
            if a[n] == 0: #O(1)
                a[n], a[left] = a[left], a[n]
                n += 1
                left += 1
            elif a[n] == 1: #O(1)
                n += 1
            else: #O(1)
                a[n], a[right] = a[right], a[n]
                right -= 1
        return a