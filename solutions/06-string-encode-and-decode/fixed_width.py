from typing import List


# Fixed-width length header (4 digits) before each string: O(n) time, O(n) space
# Decode always reads 4 chars for the length, so there is no delimiter to scan for.
# Simple, but caps any single string at 9999 characters.
class Solution:
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += f"{len(s):04d}" + s
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            length = int(s[i:i + 4])
            i += 4
            ans.append(s[i:i + length])
            i += length
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.decode(s.encode(["neet", "code", "love", "you"])))   # ['neet', 'code', 'love', 'you']
    print(s.decode(s.encode(["we", "say", ":", "yes"])))         # ['we', 'say', ':', 'yes']
    print(s.decode(s.encode([""])))                              # ['']
