from typing import List


# Sorted string as key (current best): O(n * k log k) time, O(n * k) space
# n = number of words, k = max word length
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in grp:
                grp[key] = []
            grp[key].append(word)
        return list(grp.values())


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    print(s.groupAnagrams([""]))    # [['']]
    print(s.groupAnagrams(["a"]))   # [['a']]
