class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort() #O(n)
        nums2.sort() #O(n)
        i = 0 #O(1)
        j = 0 #O(1)
        c = set() #O(n)
        while i < len(nums1) and j < len(nums2): #O(n)
            if nums1[i] == nums2[j]:
                c.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]: #O(1)
                i += 1
            else:
                j += 1
        return list(c) #O(n)