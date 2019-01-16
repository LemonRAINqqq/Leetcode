# -*- coding: utf-8 -*-
"""
LeetCode：
771. Jewels and Stones

You're given strings J representing the types of stones that are jewels, 

and S representing the stones you have.  Each character in S is a type of stone you have. 

You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. 

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:

Input: J = "z", S = "ZZ"
Output: 0

Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.

Created on Wed Aug 29 09:53:46 2018

@author: QinLong
"""

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(map(S.count, J)) #map(S.count, J)：返回list(python3 严格来说是map属性，没有影响。)
"""
sum(list).
eg:sum([2,1,4]) = 7

S.count:func

"""
#def numJewelsInStones(self, J, S):
#    return sum(map(J.count, S))
#
#def numJewelsInStones(self, J, S):
#    return sum(s in J for s in S)
#等价于： for s in S:
            #if s in J:
                #num +=1


