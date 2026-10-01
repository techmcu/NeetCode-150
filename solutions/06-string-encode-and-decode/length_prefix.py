from typing import List


# Length-prefix each string with a "#" delimiter (current best): O(n) time, O(n) space
# Prefix tells us exactly how many chars to read, so any character (even "#") is safe.
class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "#" + s
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            ans.append(s[j + 1:j + 1 + length])
            i = j + 1 + length
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.decode(s.encode(["neet", "code", "love", "you"])))   # ['neet', 'code', 'love', 'you']
    print(s.decode(s.encode(["we", "say", ":", "yes"])))         # ['we', 'say', ':', 'yes']
    print(s.decode(s.encode([""])))                              # ['']
