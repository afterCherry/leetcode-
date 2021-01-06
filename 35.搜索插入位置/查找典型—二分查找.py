class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        # 剪枝
        if target < nums[0]:
            return 0
        if target > nums[length - 1]:
            return length
        # 二分查找
        left=0
        right=length-1
        while left<=right:
            # 大数溢出：mid=(first+last)/2，first+last是有可能溢出的——计算机位数是有限的
            # 防止大数溢出：用到了减
            mid=left+(right-left)//2
            if target>nums[mid]:
                left=mid+1
            # 找到了
            elif target==nums[mid]:
                return mid
            else:
                right=mid-1
        # 没找到时的插入位置
        return left