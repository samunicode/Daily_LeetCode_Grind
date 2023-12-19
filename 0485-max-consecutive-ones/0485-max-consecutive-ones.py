class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        val, max = 0, 0
        nums.append(0)
        for i in nums:
            if i == 1:
                val += 1
            else:
                if max <= val:
                    max = val
                val = 0
        
        return max