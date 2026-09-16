from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list) #mapping charCount to list of Anagrams

        for s in strs: 
            count = [0] * 26 # a .... z 
            #go through every character in each string
            #count each character
            for c in s:
                count[ord(c) - ord("a")] += 1 

            result[tuple(count)].append(s)

        return list(result.values())