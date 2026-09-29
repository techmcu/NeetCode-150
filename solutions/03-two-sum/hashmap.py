from typing import List


# Hash map, one pass (current best): O(n) time, O(n) space
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i, num in enumerate(nums):
            dif = target - num
            if dif in freq:
                return [freq[dif], i]
            freq[num] = i
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))   # [0, 1]
    print(s.twoSum([3, 2, 4], 6))        # [1, 2]
    print(s.twoSum([3, 3], 6))           # [0, 1]
