class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1 #O(1)
    while l < r: #O(n)
        sum = numbers[l] + numbers[r]
        if sum == target: #O(1)
            return [l+1, r+1]
        elif sum < target:
            l += 1
        else:
            r -= 1
    return [-1, -1] #O(1)