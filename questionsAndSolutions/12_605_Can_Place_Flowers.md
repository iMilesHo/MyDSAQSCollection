# 605. Can Place Flowers

## Problem Statement
Check the problem statement [here](https://leetcode.com/problems/can-place-flowers/description/).


## constraints
- length of the array is [1, 2 * 10^4]
- value of elements in the array is 0 or 1
- on adjacent flowers in advance
- n: [0, length]

## idea
```
- [1, 0, 0, 0, 1]

   ^  ^     ^  ^
   only one effective place
```
- greedy strategy: 
    - check the middle elements
    - if the middle element is 0 and the previous and next elements are also 0, then we can place a flower
- check the first and last element


## Solution

### My own solution

```Python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            return (flowerbed[0]==0 and n == 1)
        
        max_new_flowers = 0

        if (flowerbed[0] + flowerbed[1]) == 0:
            max_new_flowers += 1
            flowerbed[0] = 1
        if (flowerbed[-1] + flowerbed[-2]) == 0:
            max_new_flowers += 1
            flowerbed[-1] = 1
            
        for i in range(0, len(flowerbed)-2):
            if (flowerbed[i] + flowerbed[i+1] + flowerbed[i+2]) == 0:
                max_new_flowers += 1
                flowerbed[i+1] = 1
            if max_new_flowers >= n:
                return True
        
        
        return max_new_flowers >= n
```       


### leetcode solution

```Python
# Fastest solution
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
```


```Python
# Memory efficient solution
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        cnt = 0
        for i , val in enumerate(flowerbed):
            if val == 0:
                left = False
                right = False
                if i == 0 or flowerbed[i-1] == 0:
                    left = True
                if i == len(flowerbed) - 1 or flowerbed[i+1] ==0:
                    right = True
                if left and right:
                    flowerbed[i] = 1
                    cnt += 1
                    if (cnt == n):
                        return True

        return False
```

## Notes

- `enumerate(flowerbed)`: Returns an enumerate tuple containing a count (from start which defaults to 0) and the values obtained from iterating over flowerbed.