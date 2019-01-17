# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 16:06:07 2019

@author: QinLong

https://leetcode.com/problems/3sum/
https://leetcode.com/problems/3sum/discuss/7498/Python-solution-with-detailed-explanation
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。


"""

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#因为要求不重复，故排序后直接向后遍历即可
        nums.sort()
        L =  len(nums)
        result = []
        for i in range(L):
            if i > 0 and nums[i] == nums[i-1] :#相同可省略遍历（因为排序）
                continue # 跳出本次循环
            
            target = nums[i]* -1
            s = i+1
            e = L-1
            while s<e:
                if nums[s] + nums[e] == target:
                    result.append([nums[i],nums[s],nums[e]])
                    s +=1
                    while s<e and nums[s] == nums[s-1]:#相同跳过
                        s +=1
                elif nums[s] + nums[e] < target:
                    s +=1
                else:
                    e -=1
        return result
                    




