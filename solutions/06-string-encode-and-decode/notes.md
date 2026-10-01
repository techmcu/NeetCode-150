# 06. String Encode and Decode

LeetCode #271 · NeetCode: Encode and Decode Strings · Medium · Arrays & Hashing

## Problem

Design an algorithm to **encode** a list of strings into a single string, and
**decode** that single string back into the original list. The strings may contain
any of the 256 valid ASCII characters, including digits, spaces, and delimiters.

### Examples

```
Input:  ["neet", "code", "love", "you"]
Output: ["neet", "code", "love", "you"]      # encode then decode round-trips

Input:  ["we", "say", ":", "yes"]
Output: ["we", "say", ":", "yes"]
```

### Constraints

- `0 <= strs.length < 100`
- `0 <= strs[i].length < 200`
- `strs[i]` contains only UTF-8 characters.

## Idea

We can't just join the strings with a separator, because any separator we pick could
show up inside a string. The fix is to store **how long** each string is right before
it, so decode knows exactly how many characters to read and never has to guess where
one string ends.

## Approaches

### Approach 1 — Length prefix with `#` delimiter (current best) → [`length_prefix.py`](./length_prefix.py)

Write each string as `len + "#" + string`. To decode, read digits up to the `#` to get
the length, then slice exactly that many characters after it. The `#` only marks where
the number ends — the length (not the delimiter) decides where the string stops, so a
string can safely contain `#` or digits. Works for any length.

- Time: O(n)
- Space: O(n)

### Approach 2 — Fixed-width length header → [`fixed_width.py`](./fixed_width.py)

Write each string as a 4-digit zero-padded length followed by the string. Decode always
reads 4 characters for the length, so there's no delimiter to scan for at all. Slightly
simpler to decode, but it caps any single string at 9999 characters.

- Time: O(n)
- Space: O(n)

<!-- New approach later? Add a new .py file and list it here. Keep the old ones. -->

## Notes

The whole trick is encoding the length, not a separator. Once the receiver knows the
length, the bytes themselves can be anything — which is exactly why this beats any
"split on a special character" attempt.
