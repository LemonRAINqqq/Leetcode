# -*- coding: utf-8 -*-
"""
两个字符串S 和 s。如S='meituan2019',s='iu2',在S中找到包含s的最小字符串。（这里是‘ituan2’）
如果s为空，输出S；

ac=67，
Created on Wed Sep 11 15:47:35 2019

@author: QinLong
"""
#
S = input()
s = input()

def solution(S,s):
    if not s:
        return S
    
    n = len(S)
    index = {}
    res = []
    
    for i in range(n):
        if S[i] in s:
#            if S[i] not in index:
            index[S[i]] = i

    if len(index) == len(s):
        for key in index:
            res.append(index[key])
            
        res.sort()
        res1 = S[res[0]:res[len(res)-1]+1]
        return res1
        
    else:
        return ''
                        
print(solution(S,s))
