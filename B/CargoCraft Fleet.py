import sys

def solve():
    t = int(input().strip())
    results = []

    # 2. 循环 t 次，读取每组的 n
    for _ in range(t):
        while True:
            try:
                line = input().strip()
                if line:
                    parts = line.split()
                    if len(parts) >= 1:
                        n = int(parts[0])

                        if n % 2 != 0 or (n < 4 and n != 0):
                            results.append("-1")
                        elif n == 0:
                            results.append("0 0")
                        else:
                            max_crafts = n // 4
                            if n % 6 == 0:
                                min_crafts = n // 6
                            else:
                                min_crafts = (n // 6) + 1
                            results.append(f"{min_crafts} {max_crafts}")

                        break
            except EOFError:
                break

    for res in results:
        print(res)

if __name__ == "__main__":
    solve()