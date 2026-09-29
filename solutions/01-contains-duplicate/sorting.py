from typing import List


# Sorting: O(n log n) time, O(1) extra space (mutates the input)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    print(s.hasDuplicate([1, 2, 3, 3]))   # True
    print(s.hasDuplicate([1, 2, 3, 4]))   # False
