#python
#beats 100.00%
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        y=0
        x=0
        for i in range(1,len(points)):
            a,b=points[i]
            c,d=points[i-1]
            x=max(abs(a-c),abs(b-d))
            y+=x
        return y
