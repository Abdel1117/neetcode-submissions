class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums: number[]): number[] {
        let output : number[] =  []
        let prefix = 1 
        let suffix = 1 
        for(let i : number = 0; i< nums.length; i++){
            output[i] = prefix
            prefix = prefix * nums[i] 
            
        }

        for (let i = nums.length - 1; i >= 0; i--) {            
            output[i] =  output[i] * suffix
            suffix = suffix * nums[i]
        }
        return output
    }
}
