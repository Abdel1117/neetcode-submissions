class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dico = defaultdict(list)
        for elt in strs:
            print(elt)
            dico[''.join(sorted(elt))].append(elt)
        return [a for a in dico.values()]