def Solution(nums):
    totalSub = [0]*len(nums)

    if len(nums)==1:
        return nums[0]
    
    def maxProduct(n):
        # print(n, nums)
        """
        :type nums: List[int]
        :rtype: int
        """
        print(n, totalSub)
        print((nums[n]*nums[n-1]), nums[n-1])
        if (nums[n]*nums[n-1]) >= nums[n-1]:
            print('TRUE')
            totalSub[n-1] = nums[n-1]*maxProduct(n+1)
        else:
            print('FALSE')
            return nums[n-1]

        return max(nums[n], nums[n]*maxProduct(n+1))
    return maxProduct(0)

print(Solution([2,3,-2,4])) #[-2,0,-1]))
# [2,3,-2,4]
