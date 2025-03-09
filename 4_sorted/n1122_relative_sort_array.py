class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        c = 0 #O(n)
        for i in range(len(arr2)): #O(n)
            for j in range(len(arr1)): #O(n)
                if arr1[j] == arr2[i]: #O(1)
                    arr1[c], arr1[j] = arr1[j], arr1[c]
                    c += 1
        arr1[c:] = sorted(arr1[c:]) #O(2)
        return arr1