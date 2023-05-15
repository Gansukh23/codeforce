def solve():
    n = int(input())
    if n % 2 == 1:
        for i in range(1,n+1):
            print(f'{i}',end=' ')
        print()
    else:
        for i in range(1,n+1):
            print(f'{2*i}',end=' ')
        print()

t = int(input())
for i in range(t):
    solve()