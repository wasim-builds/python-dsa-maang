import os
import argparse
import sys

# Get the absolute path to the root of the repository
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TOPICS = [
    "01_arrays",
    "02_strings",
    "03_linked_lists",
    "04_stacks_queues",
    "05_trees",
    "06_graphs",
    "07_dynamic_programming",
    "08_binary_search",
    "09_two_pointers_sliding_window",
    "10_heap_priority_queue",
    "11_backtracking",
    "12_greedy",
    "13_tries",
    "14_bit_manipulation",
]

DIFFICULTIES = ["easy", "medium", "hard"]

TEMPLATE = '''"""
Problem: {name}
Difficulty: {difficulty}
Topic: {topic}

Problem Statement:
[Add problem statement here]
"""
import pytest

# BRUTE FORCE
# Time: O(?), Space: O(?)
def solve_brute():
    pass

# OPTIMAL
# Time: O(?), Space: O(?)
def solve_optimal():
    pass

@pytest.mark.parametrize("input_data, expected", [
    # (input1, expected1),
])
def test_solve_optimal(input_data, expected):
    assert solve_optimal() == expected

@pytest.mark.parametrize("input_data, expected", [
    # (input1, expected1),
])
def test_solve_brute(input_data, expected):
    assert solve_brute() == expected
'''


def create_problem(topic, difficulty, num, name):
    # Normalize inputs
    difficulty = difficulty.lower()

    # Find exact topic directory
    topic_dir = next((t for t in TOPICS if t.endswith(topic) or topic in t), None)
    if not topic_dir:
        print(f"Error: Topic '{topic}' not found. Available topics:")
        for t in TOPICS:
            print(f"  - {t}")
        sys.exit(1)

    if difficulty not in DIFFICULTIES:
        print(
            f"Error: Difficulty '{difficulty}' not valid. Must be one of {DIFFICULTIES}"
        )
        sys.exit(1)

    # Format filename
    name_snake = name.lower().replace(" ", "_").replace("-", "_")
    filename = f"{int(num):03d}_{name_snake}.py"

    # Ensure directory exists
    dir_path = os.path.join(BASE_DIR, "topics", topic_dir, difficulty)
    os.makedirs(dir_path, exist_ok=True)

    filepath = os.path.join(dir_path, filename)

    if os.path.exists(filepath):
        print(f"Error: File already exists at {filepath}")
        sys.exit(1)

    # Write template
    with open(filepath, "w") as f:
        f.write(
            TEMPLATE.format(
                num=num, name=name, difficulty=difficulty.capitalize(), topic=topic_dir
            )
        )

    print(f"✅ Successfully created problem template at:")
    print(f"   {filepath}")


def main():
    parser = argparse.ArgumentParser(description="Python DSA MAANG Utility Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Create command
    create_parser = subparsers.add_parser(
        "create", help="Create a new problem template"
    )
    create_parser.add_argument(
        "--topic", required=True, help="Topic (e.g., arrays, strings, 01_arrays)"
    )
    create_parser.add_argument(
        "--difficulty", required=True, choices=DIFFICULTIES, help="Difficulty level"
    )
    create_parser.add_argument(
        "--num", required=True, type=int, help="Problem number (e.g., 6)"
    )
    create_parser.add_argument(
        "--name", required=True, help="Problem name (e.g., 'Maximum Subarray')"
    )

    args = parser.parse_args()

    if args.command == "create":
        create_problem(args.topic, args.difficulty, args.num, args.name)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
