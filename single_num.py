class Solution(object):
    def single_num(self,nums):
        result=0
        for num in nums:
            result=result^num
        return result