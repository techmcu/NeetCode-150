from typing import List
from collections import Counter
import heapq


# Count, then pull the k largest with a heap: O(n log k) time, O(n) space
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)


if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))   # [1, 2]
    print(s.topKFrequent([7, 7], 1))               # [7]
