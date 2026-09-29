from typing import List


class Solution:
    # Approach 1 — Hash set (current best): O(n) time, O(n) space
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

    # Approach 2 — Sorting: O(n log n) time, O(1) extra space
    def hasDuplicate_sorting(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.hasDuplicate([1, 2, 3, 3]))            # True
    print(s.hasDuplicate([1, 2, 3, 4]))            # False
    print(s.hasDuplicate_sorting([1, 2, 3, 3]))    # True
    print(s.hasDuplicate_sorting([1, 2, 3, 4]))    # False
