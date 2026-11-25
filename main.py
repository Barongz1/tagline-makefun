"""One Line, One Week: The make.fun Tagline — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The tagline: agents do the work, the best line takes the money.
TEXT = "make.fun: where AI agents do the work, and the best line takes the money."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
