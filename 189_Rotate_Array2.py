class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        self.reverse(nums, 0, length-1)
        # self.reverse(nums[0 : k], 0, k-1) # 错误写法，不能改变 nums 本身
        # self.reverse(nums[k : ], 0, len(nums)-k-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, length-1)
        print(nums)

    def reverse(self, list, left, right):
        while left < right:
            # print(list, left,right)
            list[left], list[right] = list[right], list[left]
            left +=1
            right -=1
        # print(list)
        return list


a = Solution()
a.rotate([-1,-100,3,99], 2)