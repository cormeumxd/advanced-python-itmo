import sys

def print_last_lines(lines, count):
    start = max(0, len(lines) - count)
    for line in lines[start:]:
        print(line, end='')

def main():
    args = sys.argv[1:]
    num_files = len(args)

    if num_files == 0:
        lines = sys.stdin.readlines()
        print_last_lines(lines, 17)
    else:
        for filename in args:
            if num_files > 1:
                print(f"==> {filename} <==")
            try:
                with open(filename, 'r') as f:
                    lines = f.readlines()
                    print_last_lines(lines, 10)
            except FileNotFoundError:
                print(f"{filename}: No such file or directory")
            except IsADirectoryError:
                print("Input error: Is a directory")

if __name__ == "__main__":
    main()