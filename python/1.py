#1. Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        soma = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                soma = nums[i] + nums[j]

                if soma == target:
                    return [i,j]

#Principal
nums = [2,7,11,15]
target = 9