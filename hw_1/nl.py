import sys

def main():
    input_filename = sys.argv[1] if len(sys.argv) > 1 else None
    line_number = 1

    if input_filename:
        try:
            with open(input_filename, 'r') as f:
                for line in f:
                    stripped = line.rstrip('\n')
                    print(f"{line_number:6}  {stripped}")
                    line_number += 1
        except FileNotFoundError:
            print(f"{input_filename}: No such file or directory")
        except IsADirectoryError:
            print("Input error: Is a directory")
    else:
        for line in sys.stdin:
            stripped = line.rstrip('\n')
            print(f"{line_number:6}  {stripped}")
            line_number += 1

if __name__ == "__main__":
    main()