# 05. Top K Frequent Elements

LeetCode #347 · NeetCode: Top K Elements in List · Medium · Arrays & Hashing

## Problem

Given an integer array `nums` and an integer `k`, return the `k` most frequent
elements. The answer can be in any order, and the answer is guaranteed to be unique.

### Examples

```
Input:  nums = [1, 1, 1, 2, 2, 3], k = 2
Output: [1, 2]

Input:  nums = [7, 7], k = 1
Output: [7]
```

### Constraints

- `1 <= nums.length <= 10^5`
- `k` is in the range `[1, number of distinct elements]`.

## Idea

First count how often each value appears. The whole problem is then "pick the `k`
keys with the biggest counts" — the different approaches are just different ways to
find those top `k`.

## Approaches

### Approach 1 — Bucket sort by frequency (current best) → [`bucket_sort.py`](./bucket_sort.py)

A value can appear at most `n` times, so make `n + 1` buckets indexed by count and
drop each value into the bucket for its frequency. Walk the buckets from high count to
low and collect until we have `k`. No sorting or heap needed.

- Time: O(n)
- Space: O(n)

### Approach 2 — Heap → [`heap.py`](./heap.py)

Count with a `Counter`, then let `heapq.nlargest` pull the `k` keys with the largest
counts.

- Time: O(n log k)
- Space: O(n)

### Approach 3 — Sort by frequency → [`sorting.py`](./sorting.py)

Count, then sort the keys by their count in descending order and take the first `k`.
Simplest to write, but the sort makes it the slowest here.

- Time: O(n log n)
- Space: O(n)

<!-- New approach later? Add a new .py file and list it here. Keep the old ones. -->

## Notes

Bucket sort beats the O(log ...) approaches because the counts are bounded by `n`,
which lets us place values by count directly instead of comparing them.
