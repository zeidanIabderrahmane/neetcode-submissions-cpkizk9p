class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = set(nums)
        longest=0
        for i in seq:
            if (i-1) not in seq:
                current = i
                while (current+1) in seq:
                    current += 1
                length = current - i + 1
                if length > longest:
                    longest = length

        return longest