#python
#beats 68.04
class Solution:
    def missingNumber(self, nums):
        return sum(range(len(nums)+1))-sum(nums)
        
