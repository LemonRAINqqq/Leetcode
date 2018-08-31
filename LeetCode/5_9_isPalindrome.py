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
