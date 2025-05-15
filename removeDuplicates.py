class Solution:
    def removeDuplicates(self,nums):
        write_index = 1
        
        if not nums :  return 0

        for read_index in range(1, len(nums)):
            if nums[read_index] != nums [read_index - 1]:
                nums [write_index] = nums [read_index]
                write_index += 1
        
        return nums
sol = Solution() 
print(sol.removeDuplicates([1,1,3,6,6,7,8]))
        