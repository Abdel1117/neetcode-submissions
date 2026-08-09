class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}

        for i in nums:
            if i in nums_dict:
                nums_dict[i] += 1
            else : 
                nums_dict[i] = 1 
        print(nums_dict)
        final_output = list(nums_dict.keys())
        final_output.sort(key = lambda x : nums_dict[x] , reverse=True)
        print(final_output)
        return final_output[:k]