class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        pro = (nums[-1]-1)*(nums[-2]-1)
        return pro