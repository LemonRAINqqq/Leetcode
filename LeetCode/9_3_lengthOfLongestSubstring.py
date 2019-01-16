# -*- coding: utf-8 -*-
"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
Created on Fri Sep 21 15:59:31 2018

@author: QinLong
"""
#遍历s，若遇到重复的字母，更新定位（start）坐标并更新maxLength
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1 #  更新start指向最新的位置 
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength
    
#使用enumerate函数精简代码   
class Solution2:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        max_length = start = 0
        for i, c in enumerate(s) :
            if c in used and start <= used[c] :
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            
            used[c] = i
            #print(used,start,max_length)
        return max_length

     
    
    
    #2019.1.16 output max_length , max_str:
    
    class Solution3:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        max_length = start = 0
        max_str = ''
        for i, c in enumerate(s) :
            if c in used and start <= used[c] : #"tmmzuxta"
                #在used[c]之前的字符会有重复字符（c in used）阻碍，所以更新为used[c] + 1
                start = used[c] + 1 
            else:
                max_length = max(max_length, i - start + 1)
                new = s[start:i+1]
                if len(new) > len(max_str):
                    max_str = new
                #max_str = new if len(new) > len(max_str) else max_str 
                #max_str = max(max_str, mid, key=lambda x: len(x))
            used[c] = i
            #print(used,start,max_length,max_str)
        return max_length,max_str
