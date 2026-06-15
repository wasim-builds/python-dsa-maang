# Python DSA MAANG Preparation

Welcome to the ultimate Python Data Structures and Algorithms repository tailored for MAANG (Meta, Amazon, Apple, Netflix, Google) interview preparation! 

This repository contains **306 fully implemented, parameterized, and tested algorithmic solutions** spanning 14 different fundamental topics.

## Features
- **Comprehensive Coverage:** 14 topics covering everything from Arrays and Strings to advanced Graphs, Tries, Backtracking, and Bit Manipulation.
- **Production Grade Code:** Every problem contains a baseline brute force approach (`solve_brute`) for verification and an optimal approach (`solve_optimal`) strictly adhering to the best time/space complexities (e.g. $O(N)$, $O(N \log N)$).
- **Extensive Testing:** Uses `pytest` with parameterized test cases matching standard edge cases and tricky bounds. Over 850 tests are actively maintained.
- **Clean Code Standard:** All Python files are formatted with `black` for consistent, PEP8-compliant structure.

## Repository Status
✅ **100% Complete:** All 306 algorithmic template problems have been successfully solved and verified. 
See the auto-generated [TRACKER.md](./TRACKER.md) for the full list of implemented algorithms.

## Prerequisites
- Python 3.9+
- `pytest` (for running the test suite)

You can install the dependencies via:
```bash
pip install pytest black
```

## Running the Tests
To run the entire suite of 850+ tests and verify the integrity of the solutions:
```bash
# Run all tests in the repository
pytest topics/

# Run tests with verbose output
pytest -v topics/

# Run tests for a specific topic
pytest topics/01_arrays/
```

## Structure
```text
topics/
├── 01_arrays/
├── 02_strings/
├── 03_linked_lists/
├── 04_stacks_queues/
├── 05_trees/
├── 06_graphs/
├── 07_dynamic_programming/
├── 08_binary_search/
├── 09_two_pointers_sliding_window/
├── 10_heap_priority_queue/
├── 11_backtracking/
├── 12_greedy/
├── 13_tries/
└── 14_bit_manipulation/
utils/                 # Helper functions and data structures (Tree/List nodes)
pytest.ini             # Pytest configuration file
TRACKER.md             # Master checklist of all algorithms
```
