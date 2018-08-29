# -*- coding: utf-8 -*-
"""
LeetCode：
2. Add Two Numbers


You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Created on Tue Aug 28 16:43:24 2018

@author: QinLong
"""

class Solution:
    def addTwoNumbers(self,l1,l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list_1 = []
        list_2 = []
        
        while l1:
            list_1.insert(0,str(l1.val))
            l1 = l1.next
        while l2:
            list_2.insert(0, str(l2.val))
            l2 = l2.next
            
        sum_1 = int(''.join(list_1))
        sum_2 = int(''.join(list_2))
        
        total = sum_1 + sum_2
        total = str(total)
        
        reversed_list = list(reversed(list(total))) #返回一个反转的迭代器。
        
        reversed_list = [int(x) for x in reversed_list]
        
        return reversed_list
