class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict, tDict = {}, {} 
        # dDict, tDict = dict(), dict() # alternate creation
        for sChar in s: 
            if sChar in sDict:
                sDict[sChar] += 1
            else:
                sDict[sChar] = 1

        for tChar in t:
            if tChar in tDict:
                tDict[tChar] += 1
            else:
                tDict[tChar] = 1
        
        return sDict == tDict