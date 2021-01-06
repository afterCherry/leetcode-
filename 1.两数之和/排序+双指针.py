class Solution:
    #用python3运行是可以的
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #为了到后来能保存下标信息，空间O(n)
        nums1=nums.copy()
        nums1.sort() #默认归并排序，O(nlogn)
        #双指针O(n)
        i=0
        j=len(nums1)-1
        #跳出是i==j
        while i<j:
            # 小的话就让小的数往大了走一走
            if (nums1[i]+nums1[j])<target:
                i+=1
            # 大的话就让大的数往小了走一走
            elif (nums1[i]+nums1[j])>target:
                j -= 1
            else:
                break
        #用弹出—比如target=6,nums中只有1个3，那么i,j就会都对应上3的下标，不实际
        pos1=nums.index(nums1[i])
        #弹出下标pos1的元素
        nums.pop(pos1)
        pos2=nums.index(nums1[j])
        if pos1<=pos2:
            pos2+=1
        return [pos1,pos2]

# 时间复杂度 O(nlogn)
# 空间复杂度 O(n)