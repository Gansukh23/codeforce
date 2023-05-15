def solve():
    n = int(input())
    p = [int(x) for x in input().split(" ")]
    a = [abs(i[0] - i[1] + 1) for i in enumerate(p) if abs(i[0] - i[1] + 1) != 0]
    print(min(a))

t = int(input())
for i in range(t):
    solve()