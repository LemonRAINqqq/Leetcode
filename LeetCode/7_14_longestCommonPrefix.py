# -*- coding: utf-8 -*-
"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
Created on Tue Sep  4 09:44:53 2018

@author: QinLong
"""
#
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""
        for i ,index_letter in enumerate(zip(*strs)):#enumerate:索引序列 ； zip：对应元素打包成tuple
            if len(set(index_letter)) > 1: #set： 无序不重复元素集
                return strs[0][:i]
        else:
            return min(strs)
    
#  以最短为基准，循环比较   
class Solution2:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """        
        if not strs:
            return ""        
        shortest = min(strs,key=len) #以len 为基准
        for i , ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest
        
        
        
        
        
        
        
        
        
        
        
