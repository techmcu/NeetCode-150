# Contains Duplicate

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

## Intuition

We just need to know whether we've *ever* seen a value before while scanning the
array. "Have I seen this already?" is a membership question, and a hash set answers
that in O(1) on average. So we scan once and remember what we've seen.

## Approaches

### 1. Brute force — compare every pair
Check every pair `(i, j)`. Simple but slow.
- Time: O(n^2), Space: O(1)

### 2. Sort first
Sort the array; duplicates become adjacent, so scan neighbours.
- Time: O(n log n), Space: O(1) or O(n) depending on the sort — also mutates input.

### 3. Hash set (best) ✅
Keep a set of seen values. For each number, if it's already in the set a duplicate
exists; otherwise add it and continue.
- Time: O(n), Space: O(n)

## Flow (hash set)

1. Create an empty set `seen`.
2. Loop over each `num` in `nums`:
   - If `num` is already in `seen` → return `True` (duplicate found, stop early).
   - Otherwise add `num` to `seen`.
3. If the loop finishes with no repeats → return `False`.

```
nums = [1, 2, 3, 3]

num=1  seen={}        -> not in seen, add    seen={1}
num=2  seen={1}       -> not in seen, add    seen={1,2}
num=3  seen={1,2}     -> not in seen, add    seen={1,2,3}
num=3  seen={1,2,3}   -> already in seen     -> return True
```

## Complexity

- Time: O(n) — single pass, constant-time set operations
- Space: O(n) — the set can hold up to n elements

## Solution

See [`solution.py`](./solution.py).

> A one-liner also works: `return len(set(nums)) != len(nums)`.
> The explicit loop is preferred here because it returns early on the first
> duplicate instead of always building the full set.
