#python
#beats 84.98%
class Solution:
  def containsDuplicate(self,arr):
    if len(arr) != len(set(arr)):
      return True
    else:
      return False
