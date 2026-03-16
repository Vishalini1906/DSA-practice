class Solution(object):
    def missing_number(self,nums):
        n=len(nums)
        actual=n*(n+1)/2
        current=sum(nums)
        return actual-current