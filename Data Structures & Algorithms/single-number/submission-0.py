class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if nums:
            res = 0
            for i in nums :
                res = res ^ i
            return res