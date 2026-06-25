import os
import re

root_dir = "/home/wasim/Documents/github/python-dsa-maang"

# Regular expression to match the boilerplate
# Black formatter ensures it looks exactly like this, just with varying indentation
# typically 4 spaces inside `if __name__ == "__main__":`
pattern = re.compile(
    r"[ \t]*if \(\n"
    r"[ \t]*isinstance\(test_cases, tuple\)\n"
    r"[ \t]*and len\(test_cases\) > 0\n"
    r"[ \t]*and not isinstance\(test_cases\[0\], \(tuple, list\)\)\n"
    r"[ \t]*\):\n"
    r"[ \t]*test_cases = \[test_cases\]\n"
    r"[ \t]*elif not isinstance\(test_cases, \(list, tuple\)\):\n"
    r"[ \t]*test_cases = \[test_cases\]\n",
    re.MULTILINE,
)

# Alternative simple string replacement since it is mostly 4-space indented:
snippet = """"""

count = 0
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".py"):
            filepath = os.path.join(subdir, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            # Using regex to be safe with any indent level
            new_content = pattern.sub("", content)

            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                count += 1

print(f"Removed boilerplate from {count} files.")
