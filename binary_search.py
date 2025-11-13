test_case = {
  "input": {
    "list": [1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10],
    "target": 9
  },
  "output": 2
}

def verify_location(list, target, mid):
  mid_number = list[mid]

  if mid_number == target:
    if mid - 1 >= 0 and list[mid - 1] == target:
      return 'left'
    else:
      return 'found'

  elif mid_number < target:
    return 'right'

  else:
    return 'left'

def binary_search(list, target):

  first, last = 0, len(list) - 1

  while first <= last:

    mid = (first + last) // 2
    location_status = verify_location(list, target, mid)

    if location_status == 'found':
      return mid

    elif location_status == 'right':
      first = mid + 1

    else:
      last = mid - 1

  return -1

index = binary_search(**test_case['input'])
print('output :', output)

'''
TODO: Question => Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity
'''
'''
def bs_with_closure(list, target):

  def verify_location(mid):
    mid_number = list[mid]

    if mid_number == target
      if mid - 1 >= 0 and list[mid - 1] == target:
        return 'left'
      else:
        return 'found'

    elif mid_number < target:
      return 'right'

    else:
      return 'left'

  return binary_search(list, target, verify_location)
'''
'''
# Analyzing algorithm complexity and identify inefficiencies, if any:

if we start out with an array of N elements, then each time the size of the array reduces to the half for the next iteration, until we are left with just 1 element.

Initial length - N
Iteration 1 - N/2
Iteration 2 - N/4 -> N/2^2
Iteration 3 - N/8 -> N/2^3
...
Iteration k - N/2^k

Since the final length of array is 1, we can say that
N/2^k = 1
Rearranging the terms, we get
N = 2^k
Taking the logarithm on both side we get
k = log N

with that the time complexity of binary search will be O(log N)
and the space complexity will be O(1)
'''
'''
question : given a rotated sorted array nums of unique elements find the minimum number of times the list has been rotated.
def count_rotations_binary(nums):
  lo = 0
  hi = len(nums) - 1

  while lo <= hi:
    mid = (lo + hi) // 2
    mid_number = nums[mid]

    if mid > 0 and mid_number < nums[mid - 1]:
      return mid

    elif mid_number < nums[hi]:
      hi = mid - 1

    else:
      lo = mid + 1

  return 0
'''