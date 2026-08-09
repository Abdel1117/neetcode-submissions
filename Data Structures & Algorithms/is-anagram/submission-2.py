class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_in_array_1 = []
        word_in_array_2 = []

        if (len(s) == len(t)):
            for letter in s : 
                word_in_array_1.append(letter)


            for letter in t : 
                word_in_array_2.append(letter)
                
            word_in_array_1.sort()
            word_in_array_2.sort()
         
            return word_in_array_1 == word_in_array_2

        else:
            return False 



