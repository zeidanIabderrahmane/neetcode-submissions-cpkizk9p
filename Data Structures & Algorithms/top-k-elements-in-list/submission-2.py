class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_val = min(nums)
        max_val = max(nums)
        offset = -min_val
        counts = [0] * (max_val - min_val + 1)
        val = []

        for num in nums:
            counts[num + offset] += 1

        for _ in range(k):
            max_idx = -1
            max_val_cpt = -1
            for i in range(len(counts)):
                if counts[i] > max_val_cpt:
                    max_val_cpt = counts[i]
                    max_idx = i
            if max_idx != -1:
                num = max_idx - offset
                val.append(num)
                counts[max_idx] = -1   
        return val