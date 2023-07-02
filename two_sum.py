from collections import defaultdict

class Solution:
    def twoSum(self, nums, target):
        numMap = defaultdict(lambda: -1)
        for idx, x in enumerate(nums):
            if numMap[target - x] != -1:
                return [idx, numMap[target - x]]
            numMap[x] = idx
        # Should never reach here
        # ideally.
        return [None, None]