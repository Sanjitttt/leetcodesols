#python
#beats 93.83%
class Solution:
    def findDisappearedNumbers(self, nums):
        x=len(nums)
        num=set(nums)
        a=[]
        for i in range(1,x+1):
            if i not in num:
                a.append(i)
        return a
      
