class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)-1
        idx = 0
        while idx != l:
            if (numbers[idx]+numbers[l]) > target:
                l-=1
            elif (numbers[idx]+numbers[l]) < target:
                idx+=1
            if (numbers[idx]+numbers[l]) == target:
                return [idx+1, l+1]