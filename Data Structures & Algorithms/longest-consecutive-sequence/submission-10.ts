class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums: number[]): number {
        if (nums.length === 0) return 0;
        let sorted_array : number[] = nums.sort(function(a, b){return a - b })
        let consecutive_array = 1 
        let max_consecutive = 1
        for(let i : number = 1 ; i<sorted_array.length; i++){
            if(sorted_array[i] === sorted_array[i-1]) continue;
            if(sorted_array[i] === sorted_array[i-1] + 1){
                consecutive_array += 1
            } else {
                consecutive_array = 1
            }
            max_consecutive = Math.max(max_consecutive, consecutive_array);
        }
        return max_consecutive
    }
}