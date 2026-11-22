class Solution {
    public int[] twoSum(int[] numbers, int target) {
        
        int firstPointer = 0;
        int secondPointer = numbers.length - 1;
        int result = 0;
        int[] indexArray = new int[2];
        while(firstPointer <= secondPointer){
            result = numbers[firstPointer] + numbers[secondPointer];
            if(result == target){
                indexArray[0] =  firstPointer + 1 ;
                indexArray[1] =  secondPointer + 1 ;
                break;
            }else{
                if(result > target){
                    secondPointer--;
                }else{
                    firstPointer++;

                }
            }
        }
        return indexArray;

    }
    
}
