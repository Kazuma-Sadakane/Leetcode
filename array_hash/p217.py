class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cash = set()
        for num in nums:
            if num in cash:
                return True
            cash.add(num)
        else:
            return False
