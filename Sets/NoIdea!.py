n, m = input().split()

array = input().split()
y = set(input().split())
z = set(input().split())

print(sum([(i in y) - (i in z) for i in array]))
