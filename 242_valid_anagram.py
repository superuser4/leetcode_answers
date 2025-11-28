class Solution:
    # count the times a letter exists in both strings
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        l_map = {}
        r_map = {}
        for l_char, r_char in zip(s, t):
            count1 = l_map.get(l_char)
            count2 = r_map.get(r_char)
            if not count1:
                l_map[l_char] = 1
            else:
                l_map[l_char] += 1
            
            if not count2:
                r_map[r_char] = 1
            else:
                r_map[r_char] += 1

        for letter, count in l_map.items():
            r_val = r_map.get(letter)
            if count != r_val:
                return False

        return True

