# Contains Duplicate

LeetCode #217 · NeetCode: Duplicate Integer · Easy

## Problem

Given an integer array `nums`, return `true` if any value appears at least twice,
and `false` if every element is distinct.

## Approach

Keep a hash set of the numbers we've already seen. Walk through the array once:
before adding a number, check if it's already in the set. If it is, we found a
duplicate and can return early. If we finish the loop without a hit, everything
was unique.

The set gives us O(1) average lookups, so we avoid the O(n^2) brute force of
comparing every pair.

## Complexity

- Time: O(n) — single pass, constant-time set operations
- Space: O(n) — the set can hold up to n elements
