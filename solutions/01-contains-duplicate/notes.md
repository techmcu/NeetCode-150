# 01. Contains Duplicate

LeetCode #217 · NeetCode: Duplicate Integer · Easy · Arrays & Hashing

## Problem

Given an integer array `nums`, return `true` if any value appears **at least twice**,
and `false` if every element is distinct.

### Examples

```
Input:  nums = [1, 2, 3, 3]
Output: true          # 3 appears twice

Input:  nums = [1, 2, 3, 4]
Output: false         # all distinct
```

### Constraints

- `1 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`

## Approaches

### Approach 1 — Hash set (current best) → [`hashset.py`](./hashset.py)

Keep a set of values we've already seen. For each number, if it's already in the set
a duplicate exists; otherwise add it. Returns early on the first repeat.

- Time: O(n)
- Space: O(n)

### Approach 2 — Sorting → [`sorting.py`](./sorting.py)

Sort the array so equal values sit next to each other, then check adjacent pairs.
Uses less extra memory but is slower and mutates the input.

- Time: O(n log n)
- Space: O(1) extra (in-place sort)

<!-- New approach later? Add a new .py file and list it here. Keep the old ones. -->

## Notes

A one-liner also works: `len(set(nums)) != len(nums)`. The explicit loop is kept as
the main solution because it stops at the first duplicate instead of always building
the full set.
