class Solution:
    # Approach 1 — Frequency count (current best): O(n) time, O(1) space
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            if ch not in freq:
                return False
            freq[ch] -= 1
            if freq[ch] < 0:
                return False

        return True

    # Approach 2 — Sorting: O(n log n) time, O(n) space
    def isAnagram_sorting(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))         # True
    print(s.isAnagram("rat", "car"))                 # False
    print(s.isAnagram_sorting("anagram", "nagaram")) # True
    print(s.isAnagram_sorting("rat", "car"))         # False
