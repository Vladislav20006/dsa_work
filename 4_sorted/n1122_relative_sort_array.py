class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        c = 0
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr1[j] == arr2[i]:
                    arr1[c], arr1[j] = arr1[j], arr1[c]
                    c += 1
        arr1[c:] = sorted(arr1[c:])
        return arr1