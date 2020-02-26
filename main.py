from typing import List


class Solution:

  # split massive on two parts by random middle index value
  # [5,2,3,7,0], middle - index 1 (2 - value)
  # left = [0] (all values smaller then 2 value)
  # right = [5, 2, 3, 7] (all values bigger or equal 2 value)
  # then repeat qS with each part (left and right)
  def quickSort(self, array: [int]):
    if len(array) < 2:
      return array

    smaller = []
    bigger = []
    # It's important to have equal array, because otherways
    # we could have endless recursion [], [10, 9, 12]
    equal = []
    middle = len(array) // 2

    for value in array:
      if value < array[middle]:
        smaller.append(value)
      elif value > array[middle]:
        bigger.append(value)
      else:
        equal.append(value)

    sortedSmaller = self.quickSort(smaller)
    sortedBigger = self.quickSort(bigger)

    return sortedSmaller + equal + sortedBigger

  def findUnsortedSubarray(self, nums: List[int]) -> int:

    # sorted = self.quickSort(nums)
    sorted = nums.copy()
    sorted.sort()

    print('inited', nums)
    print('sorted', sorted)

    ans = 0
    left = -1
    right = len(nums)
    flag = True

    while left < right and flag:

      print('left %d, right %d' % (left, right))

      if left + 1 < right and nums[left + 1] == sorted[left + 1]:
        left += 1
      elif right - 1 > left and nums[right - 1] == sorted[right - 1]:
        right -= 1
      else:
        flag = False

    return right - left - 1


my = Solution()

n0 = [2, 6, 4, 8, 10, 9, 15]
n1 = [1, 3, 2, 1]

ans = my.findUnsortedSubarray(n1)

print('ans %d' % ans)

# With build in qsort
# Runtime: 216 ms, faster than 71.26% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Shortest Unsorted Continuous Subarray.