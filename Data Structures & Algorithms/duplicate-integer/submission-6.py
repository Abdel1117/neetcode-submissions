class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        left = 0
        right = 1


        while right < len(nums) : 
            if(nums[left] == nums[right]):
                    return True
            else:
                right += 1

                left += 1
        return False