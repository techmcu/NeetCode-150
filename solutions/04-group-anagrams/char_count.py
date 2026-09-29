from typing import List
from collections import defaultdict


# Character-count tuple as key: O(n * k) time, O(n * k) space
# Avoids sorting each word by using the 26-letter count as the key.
# n = number of words, k = max word length
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            grp[tuple(count)].append(word)
        return list(grp.values())


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(s.groupAnagrams([""]))    # [['']]
    print(s.groupAnagrams(["a"]))   # [['a']]
