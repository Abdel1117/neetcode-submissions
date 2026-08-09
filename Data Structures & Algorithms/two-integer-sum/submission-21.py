class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0 
        right = 1 
        output = []
        while left < right:
            if right < len(nums) :
                if nums[left] + nums[right] == target : 
                    output.append(left)
                    output.append(right)
                    return output
                else : 
                    right += 1
            else : 
                left +=  1 
                right = left + 1 
              

