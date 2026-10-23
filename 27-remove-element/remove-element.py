class Solution(object):
    def removeElement(self, nums, val):
        ptr = 0
        for x in range(len(nums)):
            if nums[x] != val:
                nums[ptr] = nums[x]
                ptr += 1
        return ptr
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        