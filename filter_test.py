import re

with open("junk_patterns.txt") as f:
    patterns = [re.compile(p.strip()) for p in f]

def is_junk(filename):
    return any(p.search(filename) for p in patterns)

test_files = [
    "docs/test.md",
    ".github/workflow.yml",
    "image.png",
    "README.md"
]

for f in test_files:
    print(f, "->", "JUNK" if is_junk(f) else "VALID")