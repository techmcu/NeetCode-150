# 02. Valid Anagram

LeetCode #242 · NeetCode: Is Anagram · Easy · Arrays & Hashing

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`.
An anagram uses exactly the same characters with the same counts, just reordered.

### Examples

```
Input:  s = "anagram", t = "nagaram"
Output: true

Input:  s = "rat", t = "car"
Output: false
```

### Constraints

- `1 <= s.length, t.length <= 5 * 10^4`
- `s` and `t` consist of lowercase English letters.

## Approaches

### Approach 1 — Frequency count (current best)

If the lengths differ they can't be anagrams. Otherwise count how many times each
character appears in `s`, then walk through `t` subtracting from those counts. If a
character is missing or a count drops below zero, `t` has a character `s` doesn't,
so it's not an anagram.

- Time: O(n)
- Space: O(1) — at most 26 lowercase letters in the map

### Approach 2 — Sorting

Sort both strings; anagrams become identical once ordered, so just compare them.
Shorter to write but slower.

- Time: O(n log n)
- Space: O(n) for the sorted copies

<!-- Add a new approach here whenever you find one. Keep the old ones. -->

## Notes

Python's `collections.Counter` makes Approach 1 a one-liner
(`Counter(s) == Counter(t)`). The manual dict version is kept as the main solution
to show the underlying logic and to return early.
