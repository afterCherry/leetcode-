# 划分子区间，结果由以下三部分子区间里元素的最大和得到
# 第 1 部分：子区间 [left, mid]；
# 第 2 部分：子区间 [mid + 1, right]；
# 第 3 部分：包含子区间 [mid , mid + 1] 的子区间，从中间向两边扩散，则用到第1部分、第2部分

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length=len(nums)
        # 剪枝
        if length==0:
            return 0
        return self.solve(nums,0,length-1)

    def cross(self,nums: List[int],left,mid,right):
        # 返回值=往左扩的最大数+中间数+往右扩的最大数
        # 往左扩得最大数
        max_left=0
        start_left=mid-1
        res_left=0
        while start_left>=left:
            res_left+=nums[start_left]
            max_left=max(max_left,res_left)
            start_left-=1

        # 往右扩得最大数
        max_right = 0
        start_right = mid+1
        res_right = 0
        while start_right <= right:
            res_right += nums[start_right]
            max_right = max(max_right, res_right)
            start_right += 1
        return max_left+nums[mid]+max_right



    def solve(self,nums: List[int],left,right):
        # 剪枝
        if left==right:
            return nums[left]
        mid=(left+right)>>1 #右移一位是/2，左移一位是*2
        return max(self.solve(nums,left,mid),
                   self.solve(nums,mid+1, right),
                   self.cross(nums,left,mid,right)
                   )