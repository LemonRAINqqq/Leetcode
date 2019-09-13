# -*- coding: utf-8 -*-
"""
机器人只能直视。输入是机器人身高，输出能被其他机器人看到次数最多的身高。
比前面一个高的，看不见前面一个，相同或小于前面一个身高的，可以看见前面一个。

Created on Sun Sep  8 15:34:56 2019

@author: QinLong
"""
import numpy as np
n = int(input())

arr = list(map(int,input().split()))

def solution(n,arr):
    
    dp = np.zeros(n,dtype=int)
    res = 0
    temp2 = 0
    index = 0

    
    for i in reversed(range(n)): 
        for j in range(i+1,n):
            if arr[j] == arr[i]:
                dp[i] +=1
                break
                
            elif arr[j] > arr[i]:
                break
            elif arr[j] < arr[i] and temp2 < arr[j]:
                temp2 = arr[j]
                dp[i] +=1
                
        if dp[i] >= res:
            res = dp[i]
            index = i
            
    print(dp,index,res)
    
    
    return arr[index]

n =    9
arr = [6,5,7,4,3,2,1,1,2]
print(solution(n,arr))            
            
          
            
            
            
            
            
        
