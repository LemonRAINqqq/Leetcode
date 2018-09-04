# -*- coding: utf-8 -*-
"""
9. Palindrome Number
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
Created on Fri Aug 31 15:21:58 2018

@author: QinLong
"""
#reverse the number first and see if it is equal to the original number.
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        input = x
        result = False
        if x >= 0:
            new_x = 0
            while x:
                new_x = new_x*10 + x%10
                x //=10
            if new_x==input:
                result = True
        return result
    
#左右各取一半

class Solution2:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        new_x = 0
        
        if (x < 0 or x%10 == 0):
            return False
        while (x > new_x):
            new_x = new_x*10 + x%10
            x = x//10
            
        return (x == new_x) or (x == new_x//10) #位数 偶，单 情况


#每次提取头尾两个数，判断它们是否相等，判断后去掉头尾两个数
class Solution3(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        digits = 1
        while x/digits >= 10:
            digits *= 10

        while digits > 1:
            right = x%10
            left = x//digits
            if left != right:
                return False
            x = (x%digits) // 10
            digits /= 100
        return True        





