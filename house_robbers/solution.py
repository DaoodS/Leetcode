# Time Limit exceeded 48/70
class Solution(object):
    def rob(self, nums):
        totalR = [-1]*len(nums)
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums)

        def getReward(n):
            if n==(len(nums)-1):
                return nums[len(nums)-1]
            elif n==(len(nums)-2):
                return max(nums[len(nums)-1], nums[len(nums)-2])
            
            if totalR[n+2]==-1:
                totalR[n+2] = getReward(n+2)
            if totalR[n+1]==-1:
                totalR[n+1] = getReward(n+1)
            return max((nums[n] + getReward(n+2)), getReward(n+1))
            
        return getReward(0)
