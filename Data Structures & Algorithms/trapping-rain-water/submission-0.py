class Solution:
    def trap(self, height: List[int]) -> int:
        right_max = []
        left_max = []
        area = []
        current_max1 = 0
        for i in range(len(height)):
            current_max1 = max(current_max1, height[i])
            left_max.append(current_max1)

        current_max2 = 0
        for j in range(len(height)-1,-1,-1):
            current_max2 = max(current_max2, height[j])
            right_max.append(current_max2)

        right_max.reverse()
        for k in range(len(height)):
            area.append(min(left_max[k], right_max[k]) - height[k])

        return sum(area)