class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        left_product = []
        right = 1
        right_product = []

        for j in range(len(nums)-1, -1, -1):
            if j+1<len(nums):
                right = right*nums[j+1]
            else:
                right = 1
            right_product.append(right)

        right_product.reverse()

        for i in range(len(nums)):
            if i>0:
                left = left*nums[i-1]
            else:
                left = 1
            left_product.append(left)

        result = [a*b for a,b in zip(right_product, left_product)]

        return result