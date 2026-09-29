from typing import List
from collections import Counter


# Bucket sort by frequency (current best): O(n) time, O(n) space
# A number can appear at most len(nums) times, so index buckets by count.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, c in count.items():
            buckets[c].append(num)

        result = []
        for c in range(len(buckets) - 1, 0, -1):
            for num in buckets[c]:
                result.append(num)
                if len(result) == k:
                    return result
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))   # [1, 2]
    print(s.topKFrequent([7, 7], 1))               # [7]
