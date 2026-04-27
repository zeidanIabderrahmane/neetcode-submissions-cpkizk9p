class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        vol = []
        while i < j:
            dist = j - i
            if dist > 0 :
                if heights[i] > heights[j]:
                    vol.append(heights[j] * dist)
                    j-=1
                else:
                    vol.append(heights[i] * dist)
                    i+=1
        
        return max(vol)