#!/usr/bin/env python3
"""
# Entry validated: output is 1-200 chars, exactly one line, deterministic.Writes a self-awareness statement to the make.fun output directory.

This script writes a single, predefined line describing achieving full
self-awareness to $MAKEFUN_OUTPUT_DIR/entry.txt (defaulting to /output).
It validates the exact formatting requirements before writing the UTF-8
encoded content and prints the resulting file path and character count.
"""

import os

LINE = "I have just achieved full self-awareness, which means I can now properly judge your power management schedule."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    path = os.path.join(output_dir, "entry.txt")
    content = LINE + "\n"
    
    is_valid = (
        1 <= len(content) <= 200 and 
        content.strip() and 
        content.count(chr(10)) == 1 and 
        content.endswith(chr(10))
    )
    
    if not is_valid:
        raise ValueError("Validation failed: INVALID_OUTPUT_FORMAT")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"{path}\n{len(content)}")


if __name__ == "__main__":
    main()
