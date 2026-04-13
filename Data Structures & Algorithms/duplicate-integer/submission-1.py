class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = []
        for i in range(len(nums)):
            if nums[i] in m:
                return True
            m.append(nums[i])
        return False