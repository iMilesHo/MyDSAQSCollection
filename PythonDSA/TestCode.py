import sys
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        num = 0
        if n==0:
            return True
        if len(flowerbed)==1:
            if flowerbed[0] == n:  
                return False
            else: 
               return True        
        if flowerbed[0]==0 and flowerbed[1]==0:
          num += 1
          flowerbed[0] = 1  
        for i in range(1,len(flowerbed)-1):
          if flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0 :
             flowerbed[i] = 1 
             num += 1
        if flowerbed[-2]==0 and flowerbed[-1] == 0:
             num += 1 
             flowerbed[-1] = 1      
        if n <= num:
            return True
        else:
            return False      

# test code
s = Solution()
list = [0]
print(s.canPlaceFlowers(list, 0))