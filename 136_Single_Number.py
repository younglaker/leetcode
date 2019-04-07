'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

# array
def singleNumber1(nums):
    list = []
    for i in nums:
        if i in list:
            list.remove(i)
        else:
            list.append(i)
    return list.pop()

# hash
def singleNumber2(nums):
    dict = {}
    for i in nums:
        if dict.has_key(i):
            dict.pop(i)
        else:
            dict.update({i: 0})
    print dict
    for key, val in dict.items():
        if val == 0:
            return key

# hash
def singleNumber5(nums):
    hash_table = {}
    for i in nums:
        try:
            hash_table.pop(i)
        except:
            hash_table[i] = 1
    # popitem(): Remove the last item from the dictionary:
    return hash_table.popitem()[0]

# math
def singleNumber3(nums):
    # sum(a)
    # a is the list , it adds up all the numbers in the
    # list a and takes start to be 0, so returning
    # only the sum of the numbers in the list.
    # sum(a, start)
    # this returns the sum of the list + start
    # set(list): remove the duplicate
    return 2 * sum(set(nums)) - sum(nums)

# XOR
def singleNumber4(nums):
    a = 0
    for i in nums:
        a ^= i
    return a


# print singleNumber1([4,1,2,1,2])
# print singleNumber2([4,1,2,1,2])
print singleNumber4([4,1,2,1,2])
# print singleNumber3([4,1,2,1,2])
