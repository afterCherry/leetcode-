# 结果导向—妙啊：
# 原来就有则返回的第一个出现位置（不管是原来的那个数还是新插入的那个数）就是结果
# 原来没有则就是插入位置

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)
        nums.sort()
        return nums.index(target)