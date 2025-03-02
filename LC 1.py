#python
#beats 100.00%
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      d={}
      for indx,val in enumerate(nums):
        x=target-val
        if x in d:
            return [indx,d[x]]
        d[val]=indx
        
