#python
#beats 100.00%
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        y = []
        d = {}
        srt=sorted(nums)
        for indx,val in enumerate(srt):
            if val not in d:
                d[val]=indx
        for i in nums:
            y.append(d[i])
        return y
