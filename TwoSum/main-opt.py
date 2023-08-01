from typing import *

def twoSum(nums: List[int], target: int) -> List[int]:
    
    numMaps = {} 
    numMaps = {idx:value for idx, value in enumerate(nums)}
    
    for idx, val in enumerate(nums):
        rem = target - val
        numMaps.pop(idx)
        if rem in list(numMaps.values()):
            return [idx, list(numMaps.keys())[list(numMaps.values()).index(rem)]]
    return []

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))

