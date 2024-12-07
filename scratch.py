class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for index, str in enumerate(strs):
            sortedStr = ''.join((sorted(str)))
            if sortedStr in anagrams.keys():
                anagrams[sortedStr].append(str) # don't forget 'append'!
            else:
                anagrams[sortedStr] = [str] # no brackets in 'str' before, this created a string,
                                            # with this change, we create our item as a list within a list
        return list(anagrams.values())


strs = ["eat","tea","tan","ate","nat","bat"]
anagrams = {}

for index, str in enumerate(strs):
    sortedStr = ''.join((sorted(str)))
    if sortedStr in anagrams.keys():
        anagrams[sortedStr].append(str) # don't forget 'append'!
    else:
        anagrams[sortedStr] = [str] # no brackets in 'str' before, this created a string,
                                    # with this change, we create our item as a list within a list
print(list(anagrams.values()))