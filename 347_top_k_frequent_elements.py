    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_map = {}
        for num in nums:
            if num not in f_map:
                f_map[num] = 1
            else:
                f_map[num] += 1
        
        sorted_f_map = dict(sorted(f_map.items(), key=lambda item: item[1], reverse=True))
        freq = []
        for i in range(k):
            freq.append(list(sorted_f_map)[i])
        return freq
