class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        new_nums = nums.copy()
        i = max(new_nums)
        new_nums.remove(i)
        j = max(new_nums)
        new_nums.remove(j)
        
        i = nums.index(i)
        j = nums.index(j)
        
        return (nums[i] - 1) * (nums[j] - 1)