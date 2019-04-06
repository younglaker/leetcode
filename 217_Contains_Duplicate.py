'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
def containsDuplicate(nums):
    list = set()
    # for i in range(0, len(nums)):
    #     if  nums[i] in list:
    #         return True
    #     else:
    #         list.add(nums[i])
    # return False
    for n in nums:
        if n in list:
            return n
        else:
            list.add(n)


a = containsDuplicate([1,2,13,1])
print a