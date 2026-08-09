class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dico = defaultdict(list)
        for elt in strs:
            print(elt)
            print("/".join(sorted(elt)))
            dico[''.join(sorted(elt))].append(elt)
        print(a for a in dico.values())
        return [a for a in dico.values()]