class Solution:
    def majorityElement(self, nums) -> int:
        candidate = 0
        count = 0

        for ele in nums:
            if count == 0:
                candidate = ele
                count += 1
            elif ele != candidate:
                count -= 1
            else:
                count += 1
        return candidate