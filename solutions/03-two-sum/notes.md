# 03. Two Sum

LeetCode #1 · NeetCode: Two Integer Sum · Easy · Arrays & Hashing

## Problem

Given an array `nums` and an integer `target`, return the **indices** of the two
numbers that add up to `target`. Exactly one valid pair exists, and you can't use the
same element twice.

### Examples

```
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]        # nums[0] + nums[1] = 2 + 7 = 9

Input:  nums = [3, 2, 4], target = 6
Output: [1, 2]        # 2 + 4 = 6
```

### Constraints

- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i], target <= 10^9`
- Exactly one solution exists.

## Approaches

### Approach 1 — Hash map, one pass (current best) → [`hashmap.py`](./hashmap.py)

For each number we need its complement `target - num`. Keep a map of
`value -> index` for everything seen so far. Before storing the current number, check
if its complement is already in the map; if it is, we've found the pair. One pass,
no need to look ahead.

- Time: O(n)
- Space: O(n)

### Approach 2 — Brute force → [`brute_force.py`](./brute_force.py)

Try every pair `(i, j)` and return the first that sums to `target`. Simple but slow.

- Time: O(n^2)
- Space: O(1)

<!-- New approach later? Add a new .py file and list it here. Keep the old ones. -->

## Notes

The complement trick is why one pass works: we only ever look *backwards* at numbers
we've already stored, so we never pair an element with itself.
