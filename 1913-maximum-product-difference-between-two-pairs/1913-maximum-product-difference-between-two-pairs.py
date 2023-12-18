class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        lar, s_lar = float('-inf'), float('-inf')
        small, s_small = float('inf'), float('inf')

        for i in range(0, len(nums)):
            if nums[i] > lar: 
                s_lar = lar
                lar = nums[i]
            elif nums[i] > s_lar:
                s_lar = nums[i]

            if nums[i] < small:
                s_small = small
                small = nums[i]
            elif nums[i] < s_small:
                s_small = nums[i]

        return (lar * s_lar) - (small * s_small)