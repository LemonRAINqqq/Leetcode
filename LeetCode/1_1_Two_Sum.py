# -*- coding: utf-8 -*-
"""
LeetCode:
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Created on Tue Aug 28 10:38:41 2018

@author: QinLong
"""
#O(n)

#遍历nums：nums[i]时，若dict存在target - nums[i]的数，输出indices；否则，将nums[i]放入dict
#class Solution(object): 
#    def twoSum(self, nums, target):
#        """
#        :type nums: List[int]
#        :type target: int
#        :rtype: List[int]
#            type:    Type of a parameter.
#            vartype: Type of a variable. 
#            rtype:   Return type. 
#        """
#        my_dict = {}
#        for i in range(len(nums)):
#            idx = nums[i]
#            diff = target - idx
#            if diff in my_dict:
#                return [i, my_dict[diff]]
#            my_dict[idx] = i
    
#遍历nums：nums[i]时，若dict存在与nums[i]相等的数，输出indices；否则，将target - nums[i]  存入dict。
class Solution(object):
    def twoSum(self,nums,target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict: #dict.keys
                return [buff_dict[nums[i]],i]
            else:
                buff_dict[target - nums[i]] = i
                
                
                
                
                
               
