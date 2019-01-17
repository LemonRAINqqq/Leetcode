# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 14:50:38 2019

@author: QinLong

https://leetcode.com/problems/integer-to-roman/


"""

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
#        roman = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
#        romans = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
#        roamn = {}
#        for i, c in romans.items():
#            roman[c] = i
        values = (1000,900,500,400,100,90,50,40,10,9,5,4,1)
        strs = ("M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I")
        
        roman = ''
        
        for i in range(len(values)):
            while num > values[i]:
                num -= values[i]
                roman += strs[i]
            
        return roman
            
# 采用从高位开始做减法的操作        
        
        
        
        
        
        
        
        