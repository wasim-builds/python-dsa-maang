# Python DSA MAANG Preparation

Welcome to the ultimate Python Data Structures and Algorithms repository tailored for MAANG (Meta, Amazon, Apple, Netflix, Google) interview preparation! 

This repository contains **306 fully implemented, parameterized, and tested algorithmic solutions** spanning 14 different fundamental topics.

## Features
- **Comprehensive Coverage:** 14 topics covering everything from Arrays and Strings to advanced Graphs, Tries, Backtracking, and Bit Manipulation.
- **Production Grade Code:** Every problem contains a baseline brute force approach (`solve_brute`) for verification and an optimal approach (`solve_optimal`) strictly adhering to the best time/space complexities (e.g. $O(N)$, $O(N \log N)$).
- **System Design:** Includes a dedicated `system_design/` folder with detailed markdown guides on Core Concepts (Scaling, Redis, Load Balancers) and Common Problems (Twitter, Rate Limiters, Chat Apps).
- **Extensive Testing:** Over 850 tests are actively maintained for all algorithms.
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
To verify any algorithm, simply run the Python file directly. It contains an `if __name__ == '__main__':` block with built-in test cases and assertions.

```bash
# Example: Run tests for Two Sum
python topics/01_arrays/easy/001_two_sum.py
```
If the terminal outputs `All tests passed successfully!`, the code is working. If there is an error, an `AssertionError` will be raised.

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
system_design/         # Architectural guides and interview problems
utils/                 # Helper functions and data structures (Tree/List nodes)
TRACKER.md             # Master checklist of all algorithms
```
