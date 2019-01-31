class Solution:
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        print(res)
        return res


    def dfs(self, nums, target, index, path, res):
        print(nums, target, index, path, res)
        for i in range(index, len(nums)):
            remain = target - nums[i]
            if remain < 0:
                break
            if remain == 0:
                res.append(path+ [nums[i]])
                break
            self.dfs(nums, remain, i, path + [nums[i]], res)
            print('i=%d' %i)
            print('===')


a =Solution()
a.combinationSum([2,3,6,7], 7)