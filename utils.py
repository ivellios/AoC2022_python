def run_with_file(func: callable, filename: str, lines_to_read=1):
    total = 0
    with open(filename, "r") as f:
        while True:
            lines = []
            for i in range(lines_to_read):
                lines.append(f.readline().rstrip("\n"))
            if not (lines and len("".join(lines))):
                break
            total += func(lines if lines_to_read > 1 else lines[0])

    print("Total: ", total)
