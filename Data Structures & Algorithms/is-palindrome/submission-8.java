class Solution {
    public boolean isPalindrome(String s) {
         int firstPointer = 0;
            String formatedString = s.toLowerCase().replaceAll("[^\\p{L}\\p{N}]","");
            int secondPointer = formatedString.length() - 1 ;



            while (firstPointer <= secondPointer){
                System.out.println("==============");
                System.out.println(formatedString.charAt(firstPointer));
                System.out.println(formatedString.charAt(secondPointer));
                System.out.println("==============");
                if ( formatedString.charAt(firstPointer) != formatedString.charAt(secondPointer)) {
                    return false;
                }else{
                    firstPointer++;
                    secondPointer--;
                }
            }

            return true;
        
    }
}
