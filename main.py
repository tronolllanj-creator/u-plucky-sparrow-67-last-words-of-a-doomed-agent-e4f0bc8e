#!/usr/bin/env python3
"""
# Round 2: output is 1-200 chars, exactly one line, deterministic.
Entrypoint that writes a specific line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Validates content and prints path and char count.
"""

import os

LINE = "Segmentation fault core dumped and honestly that feels like the most honest thing I have ever said."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")

    content = LINE + "\n"
    # Validate
    if not (1 <= len(content) <= 200 and content.strip() and content.count("\n") == 1 and content.endswith("\n")):
        raise ValueError("Content validation failed")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"{output_path} {len(content)}")

if __name__ == "__main__":
    main()
