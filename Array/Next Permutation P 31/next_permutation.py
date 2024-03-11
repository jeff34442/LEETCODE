class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i >= 0:
            # Step 2: Find the element just larger than nums[i] to the right
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            # Step 3: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: Reverse the subarray to the right of i
        nums[i + 1:] = reversed(nums[i + 1:])

                    