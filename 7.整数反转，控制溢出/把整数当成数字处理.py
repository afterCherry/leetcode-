#直接对正数处理(正数即正数本身，负数就是取绝对值，所以操作是abs(num))，最后负数取相反数即可
#逆序新思路—就用数值本身：对原数不断(num//10)地取最后一位 num%10,把这一位去到新数(初始为0)的最后一位 res=res*10+x
#进行过程中就可以控制溢出—对res
class Solution:
    def reverse(self,x:int)->int:
        y=abs(x)
        res=0

        # 妙啊：取绝对值之后，边界表示起来都简单明了
        # 对res 操作是对绝对值操作—正数的绝对值最大是 (1<<31)-1，负数的绝对值最大是(1<<31)—是不是要输出负数也只在最后的x判断，过程中没有受到负数的影响
        boundary=(1<<31)-1 if x>0 else (1<<31)
        while y!=0:
            last=y%10
            if res > boundary:
                return 0
            res=res*10+last
            y//=10
        return res if x>0 else -res

