from typing import *

class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        tmp = []
        length = 0
        str_ = [x for x in s]
        for al in str_:
            if al not in tmp:
                tmp.append(al)
            else:
                tmp = tmp[tmp.index(al):] 
        return len(tmp)


sol = Solution()
print(sol.lengthOfLongestSubstring(' '))
