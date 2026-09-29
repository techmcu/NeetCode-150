# NeetCode 150 — DSA Practice

My solutions to the [NeetCode 150](https://neetcode.io/practice), written and pushed
as I solve them.

## How it's organized

Everything lives in one `solutions/` folder. Each problem is a numbered subfolder
(in the order I solved it):

```
solutions/
└── NN-problem-name/
    ├── notes.md            # problem, approaches, complexity
    ├── <approach-a>.py     # one clean solution per file
    └── <approach-b>.py
```

- `NN` — solve order (01, 02, 03, ...)
- Each approach is its **own file**, named after the idea (`hashset.py`, `sorting.py`, ...),
  so every file is a single, easy-to-read solution.
- Grab the whole `solutions/` folder in one download to get everything.

### Multiple solutions per problem

A problem is never "done". When I find a cleaner or faster approach later, I add it
as a **new file** next to the old ones instead of replacing them. `notes.md` lists
every approach, links its file, and marks the current best.

## Progress

| #  | Problem            | Difficulty | Folder                              |
|----|--------------------|------------|-------------------------------------|
| 01 | Contains Duplicate | Easy       | `solutions/01-contains-duplicate/`  |
| 02 | Valid Anagram      | Easy       | `solutions/02-valid-anagram/`       |
| 03 | Two Sum            | Easy       | `solutions/03-two-sum/`             |
| 04 | Group Anagrams     | Medium     | `solutions/04-group-anagrams/`      |

Solved: **4**
