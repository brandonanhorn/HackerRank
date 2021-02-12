Y = set(input().split())

for _ in range(int(input())):
    if not Y.issuperset(set(input().split())):
        print(False)
        break
else:
    print(True)
