import sys

def main():
    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    line_number = 1
    lines = []

    if input_filename:
        try:
            with open(input_filename, 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"{input_filename}: No such file or directory")
            return
        except IsADirectoryError:
            print("Input error: Is a directory")
            return
    else:
        lines = sys.stdin.readlines()

    for line in lines:
        stripped = line.rstrip('\n')
        if stripped:
            print(f"{line_number:6}  {stripped}")
            line_number += 1
        else:
            print(stripped)

if __name__ == "__main__":
    main()
