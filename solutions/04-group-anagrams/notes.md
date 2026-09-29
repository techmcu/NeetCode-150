# 04. Group Anagrams

LeetCode #49 · NeetCode: Anagram Groups · Medium · Arrays & Hashing

## Problem

Given an array of strings `strs`, group the ones that are anagrams of each other.
Return the groups in any order.

### Examples

```
Input:  strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

Input:  strs = [""]
Output: [[""]]
```

### Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Idea

All anagrams share something that is identical once you ignore order. If we build a
**canonical key** from each word that is the same for every anagram, we can bucket
words into a dictionary keyed by that signature.

## Approaches

### Approach 1 — Sorted string as key (current best) → [`sorted_key.py`](./sorted_key.py)

Sort each word's letters; anagrams sort to the same string, so use that as the map
key and append the original word to its bucket.

- Time: O(n * k log k) — sorting each of the n words of length up to k
- Space: O(n * k)

### Approach 2 — Character-count key → [`char_count.py`](./char_count.py)

Instead of sorting, build a 26-length count of letters and use it (as a tuple) for the
key. Two words are anagrams exactly when their letter counts match. Skips the sort, so
it's asymptotically faster.

- Time: O(n * k)
- Space: O(n * k)

<!-- New approach later? Add a new .py file and list it here. Keep the old ones. -->

## Notes

`n` = number of words, `k` = max word length. Approach 2 trades the `log k` sort factor
for a fixed 26-slot count, which wins when words are long.
