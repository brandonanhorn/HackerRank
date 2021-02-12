for _ in range(int(input())):
    y, Y = input(), set(input().split())
    z, Z = input(), set(input().split())

    print(Y.issubset(Z))
