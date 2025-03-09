class Solution:
    def sortColors(self, a: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = 0
        left = 0
        right = len(a) - 1
        while n <= right:
            if a[n] == 0:
                a[n], a[left] = a[left], a[n]
                n += 1
                left += 1
            elif a[n] == 1:
                n += 1
            else:
                a[n], a[right] = a[right], a[n]
                right -= 1
        return a