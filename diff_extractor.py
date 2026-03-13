import subprocess

def get_diff():
    result = subprocess.run(
        ["git", "diff"],
        capture_output=True,
        text=True
    )
    return result.stdout


def extract_changes(diff_text):
    lines = diff_text.split("\n")
    clean_lines = []

    for line in lines:
        if line.startswith("+") and not line.startswith("+++"):
            clean_lines.append(line[1:].strip())

    return clean_lines


if __name__ == "__main__":
    diff = get_diff()
    changes = extract_changes(diff)

    print("Modified paragraphs:")
    for c in changes:
        print("-", c)