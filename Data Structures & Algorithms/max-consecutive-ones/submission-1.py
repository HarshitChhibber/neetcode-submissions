class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        largest = 0
        i = 0
        while i < len(nums):
            count = 0
            while i < len(nums) and nums[i] == 1:
                count += 1
                if count > largest:
                    largest = count
                i += 1
            i += 1
        return largest