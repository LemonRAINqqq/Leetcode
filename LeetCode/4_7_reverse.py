# -*- coding: utf-8 -*-
"""
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
Created on Thu Aug 30 10:42:38 2018

@author: QinLong
"""
# from operator import lt # lt(a,b) :a<b
class Solution(object):
    def reverse(self, x):
        
        flag = 0
        flag = 1 if x > 0 else -1
        x = flag*int(str(abs(x))[::-1])#x[::-1] 等价 x[-1:-len(x)-1:-1]
        return x if x < 2147483648 and x >= -2**31 else 0
#x = int(str(abs(x))[::-1])
#return x*flag*(x<2**31) #另一种判断

class Solution2(object):
    def reverse(self, x):
        
        flag = 1 if x > 0 else -1
        new_x , x = 0,abs(x)
        while x:
            new_x = new_x*10 + x % 10
            x //=10 #’/’总是执行真除法，不管操作数的类型，都会返回包含任何余数的浮点结果；
                    #’//’执行Floor除法，截除掉余数并且针对整数操作数返回一个整数，如果有任何一个操作数是浮点数，则返回一个浮点数。
        return  flag*new_x*(new_x<2**31)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
