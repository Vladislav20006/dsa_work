class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        expected = sorted(heights)
        a = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                a += 1
        return a