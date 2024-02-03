class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ls , l= [] , len(nums)

        for i in range (0, l):

            if i > 0  and nums[i] == nums[i-1]:
                continue
            else:
                x, y , up = i + 1, l-1, i
                
                while x < y:
                    tsum = nums[x] + nums[y] + nums[up]
                    if tsum > 0:
                        y -= 1
                    elif tsum < 0:
                        x += 1
                    else:
                        ls.append([nums[up], nums[x], nums[y]])
                        x += 1
                        while nums[x] == nums[x - 1] and x < y:
                            x += 1

        return ls
                    

