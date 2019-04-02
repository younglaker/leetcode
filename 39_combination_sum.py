'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''


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