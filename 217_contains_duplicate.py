def containsDuplicate(self, nums: List[int]) -> bool:
    hmap = {}

    for num in nums:
        val = hmap.get(num)
        if val == None:
            hmap[num] = 1
        else:
            hmap[num] += 1
            if hmap[num] > 1:
                return True
    return False
