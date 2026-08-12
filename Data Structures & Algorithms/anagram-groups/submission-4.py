from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list) 
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            key=tuple(count)
            d[key].append(s)

        # print(d)
        return list(d.values())
        
            
        
        

