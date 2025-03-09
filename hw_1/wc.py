import sys

def process_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        lines = data.count(b'\n')
        words = len(data.split())
        bytes = len(data)
    return (lines, words, bytes, filename)

def main():
    filenames = sys.argv[1:]
    total = [0, 0, 0]  # lines, words, bytes

    if not filenames:
        data = sys.stdin.buffer.read()
        lines = data.count(b'\n')
        words = len(data.split())
        bytes_ = len(data)
        print(f"{lines:8}{words:8}{bytes_:8}")
        return

    for filename in filenames:
        try:
            res = process_file(filename)
        except FileNotFoundError:
            print(f"{filename}: No such file or directory")
            continue
        except IsADirectoryError:
            print("Input error: Is a directory")
            continue
        
        lines, words, bytes_, name = res
        print(f"{lines:8}{words:8}{bytes_:8} {name}")
        total[0] += lines
        total[1] += words
        total[2] += bytes_

    if len(filenames) > 1:
        print(f"{total[0]:8}{total[1]:8}{total[2]:8} total")

if __name__ == "__main__":
    main()