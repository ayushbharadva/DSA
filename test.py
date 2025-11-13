
def findMin(nums):
    low, high = 0, len(nums) - 1

    print('low :', low, 'high :', high)

    while low <= high:

        print('low :', low, 'high :', high)

        mid = (low + high) // 2
        mid_number = nums[mid]

        print('mid :', mid, 'mid_number :', mid_number)

        if mid_number < nums[mid - 1]:
            print('if')
            return mid_number
        elif mid_number > nums[len(nums) - 1]:
            print('elif')
            low = mid + 1
        elif mid_number < nums[len(nums) - 1]:
            print('else')
            high = mid - 1
    return nums[0]

nums=[3,4,5,6,1,2]
# ans = 1;
ans = findMin(nums)
print('ans', ans)