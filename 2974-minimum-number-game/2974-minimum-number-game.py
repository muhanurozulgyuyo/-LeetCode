class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        nums.sort()

        while len(nums) != 0:
            Alice = nums.pop(0)
            Bob = nums.pop(0)

            arr.append(Bob)
            arr.append(Alice)
            
        return arr