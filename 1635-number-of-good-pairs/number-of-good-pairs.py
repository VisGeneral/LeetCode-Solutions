class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def factorial(n):
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result

        maxnum = max(nums)
        minnum = min(nums)
        i = minnum
        good = 0
        while i <= maxnum:
            count = nums.count(i)
            if count > 1:
                good += factorial(count) // (factorial(2) * factorial(count - 2))
            i += 1

        return good