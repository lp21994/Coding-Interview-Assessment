def solve():
    t = int(input().strip())
    results = []

    for _ in range(t):
        while True:
            try:
                line = input().strip()
                if line:
                    parts = line.split()
                    if len(parts) >= 2:
                        x = int(parts[0])
                        n = int(parts[1])

                        if n % 2 == 0:
                            results.append(0)
                        else:
                            results.append(x)
                        break
            except EOFError:
                break

    for res in results:
        print(res)

if __name__ == "__main__":
    solve()