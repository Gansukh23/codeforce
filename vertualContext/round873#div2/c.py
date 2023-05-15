from functools import reduce
def solve():
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    b = [int(x) for x in input().split(" ")]
    b.sort(reverse=True)
    c = [len([e for e in a if e > f[1]]) - f[0] for f in enumerate(b) ]
    print(reduce((lambda x, y: x * y % 1_000_000_007),c))

t = int(input())
for i in range(t):
    solve()