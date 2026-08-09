class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = {}
     
        for i in strs:
            letter_in_array = []
            for letter in i: 
                letter_in_array.append(letter)
            letter_in_array.sort()
            key = "".join(letter_in_array)
            if key in word_map:
                word_map[key].append(i) 
            else :
                word_map[key] = [i]

        
        return list(word_map.values())