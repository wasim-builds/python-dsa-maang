import os
import glob

BASE_DIR = "/home/wasim/Documents/github/python-dsa-maang/topics"

old_suffix = """if __name__ == "__main__":
    # Add tests here
    pass
"""

new_suffix = """@pytest.mark.parametrize("input_data, expected", [
    # (input1, expected1),
])
def test_solve_optimal(input_data, expected):
    assert solve_optimal() == expected

@pytest.mark.parametrize("input_data, expected", [
    # (input1, expected1),
])
def test_solve_brute(input_data, expected):
    assert solve_brute() == expected
"""


def update_templates():
    count = 0
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith("_template_problem.py"):
                filepath = os.path.join(root, file)
                with open(filepath, "r") as f:
                    content = f.read()

                if old_suffix in content:
                    content = content.replace(old_suffix, new_suffix)
                    # Also need to add import pytest at the top after the docstring
                    if "import pytest" not in content:
                        parts = content.split('"""\n')
                        if len(parts) >= 3:
                            parts[1] = parts[1] + '"""\nimport pytest\n'
                            content = '"""\n'.join(parts)
                            # Actually, split by '"""' is safer

                    # Safer replacement for import pytest
                    if "import pytest" not in content:
                        content = content.replace(
                            '"""\n\n# BRUTE FORCE',
                            '"""\nimport pytest\n\n# BRUTE FORCE',
                        )

                    with open(filepath, "w") as f:
                        f.write(content)
                    count += 1
    print(f"Updated {count} template files.")


if __name__ == "__main__":
    update_templates()
