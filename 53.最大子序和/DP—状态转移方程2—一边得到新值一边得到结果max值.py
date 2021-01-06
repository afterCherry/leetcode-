class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length=len(nums)
        # 剪枝
        if length==0:
            return 0
        # dp数组
        dp=[]
        dp.append(nums[0])
        res = dp[0]
        for i in range(1,length):
            temp=max(nums[i],dp[i-1]+nums[i])
            dp.append(temp)
            res = max(res, temp)
        return res
