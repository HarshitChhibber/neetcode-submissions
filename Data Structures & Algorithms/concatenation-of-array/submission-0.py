class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        a = len(nums)
        ans = [0] * (2 * a)
        for i in range(a):
            ans[i] = nums[i]
            ans[i + a] = nums[i]
        return ans       
            