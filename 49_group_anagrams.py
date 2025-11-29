    def scrambleWord(self, word: str):
        str_l = list(word)
        str_l.sort()
        str_l = "".join(str_l)
        return str_l
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        p_map = {}
        for word in strs:
            res = self.scrambleWord(word)
            if res not in p_map:
                p_map[res] = []
            p_map[res].append(word)
        
        group = []
        for key,value in p_map.items():
            group.append(value)
        return group

