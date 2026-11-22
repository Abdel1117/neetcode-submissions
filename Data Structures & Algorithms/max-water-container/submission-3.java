class Solution {
    public int maxArea(int[] heights) {
       int firstPointer = 0;
        int secondPointer = heights.length - 1;
        int max = 0;
        int max_height;
        while (firstPointer <= secondPointer) {
            if (heights[firstPointer] < heights[secondPointer]) {
                max_height = heights[firstPointer];
            } else if (heights[secondPointer] < heights[firstPointer]) {
                max_height = heights[secondPointer];
            } else {
                max_height = heights[secondPointer];
            }
            int distance_between_two_pointer = secondPointer  - firstPointer ;
            if (max < max_height * distance_between_two_pointer) {
                max = max_height * distance_between_two_pointer;
            }
            if (heights[firstPointer] < heights[secondPointer]) {
                firstPointer++;
            } else {
                secondPointer--;
            }
        }
        return max;
    }
}
