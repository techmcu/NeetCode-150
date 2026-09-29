# Sorting: O(n log n) time, O(n) space
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))   # True
    print(s.isAnagram("rat", "car"))           # False
