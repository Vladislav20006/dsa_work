class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        sortArr1 = sorted(nums1) #O(n)
        sortArr2 = sorted(nums2) #O(n)
        i = 0 #O(1)
        j = 0 #O(1)
        output = [] #O(1)
        while i < len(sortArr1) and j < len(sortArr2): #O(n)
            if sortArr1[i] < sortArr2[j]:
                i += 1
            elif sortArr2[j] < sortArr1[i]:
                j += 1
            else:
                output.append(sortArr1[i])
                i += 1
                j += 1
        return output #O(n)