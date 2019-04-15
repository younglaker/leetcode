'''
349. Intersection of Two Arrays
Easy

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''

class Solution:
    def singleNumber(self, nums1, nums2):
        dict1 = {}
        dict2 = {}
        result = []
        for i in nums1:
            dict1[i] = 0

        for i in nums2:
            dict2[i] = 0

        for key, value in dict1.items():

            # has_key has been deprecated in Python 3.0
            if key in dict2:
                result.append(key)

        return result

    def singleNumber2(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)

a =Solution()
a.singleNumber([4,9,5], [9,4,9,8,4])