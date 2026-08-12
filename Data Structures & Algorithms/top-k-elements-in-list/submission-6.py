

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}
       
        for num in nums:
            d[num] = d.get(num, 0) + 1
        sorted_keys = sorted(d.keys(), key=lambda num: d[num], reverse=True)

        return sorted_keys[0:k]
        
          