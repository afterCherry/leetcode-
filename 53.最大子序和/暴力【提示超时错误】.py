# 穷举所有的子区间，对每个子区间进行求和
# O(n^3)  子区间划分方法1：固定终点，起点从左往右走

# 优化—有相同的前缀：sum[1,4]=sum[1,3]+nums[4]
# O(n^2)  子区间划分方法2：固定起点，终点从起点往右走

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length=len(nums)
        res=-2147483647
        # 子区间划分方法1
        # for i in range(length):
        #     for j in range(i+1):
        #         s=sum(nums,j,i)
        #         res=max(res,s)

        # 子区间划分方法2
        for i in range(length):
            s=0
            for j in range(i,length):
                s+=nums[j]
                res=max(res,s)
        return res



    def sum(self,nums: List[int],left:int,right:int) ->int:
        res=0
        for i in range(left,right+1):
            res+=nums[i]
        return res
