# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 11:22:51 2019

@author: QinLong
https://leetcode.com/problems/container-with-most-water/

给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，
使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。


示例:

输入: [1,8,6,2,5,4,8,3,7]
输出: 49
"""
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j =0, len(height)-1
        max_area = 0
        while i < j:
            min_line = min(height[i], height[j])
            mid = min_line * (j-i)
            max_area = max(max_area, mid)
            if height[i] >height[j]:
                j = --1
            else:
                i = ++1
            print(i, j, max_area)
        return max_area



 
    
    
    
    
    
    
    
    
    
    
