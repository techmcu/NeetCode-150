from typing import List


# Count, then sort keys by frequency: O(n log n) time, O(n) space
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        result = sorted(freq, key=freq.get, reverse=True)
        return result[:k]


if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))   # [1, 2]
    print(s.topKFrequent([7, 7], 1))               # [7]
