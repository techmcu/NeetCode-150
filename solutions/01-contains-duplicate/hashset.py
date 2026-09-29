from typing import List


# Hash set (current best): O(n) time, O(n) space
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.hasDuplicate([1, 2, 3, 3]))   # True
    print(s.hasDuplicate([1, 2, 3, 4]))   # False
