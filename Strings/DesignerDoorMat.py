N, M = map(int, input().split())
designer = [('.|.' * (2 * i + 1)).center(M, '-') for i in range(N // 2)]
print('\n'.join(designer + ['WELCOME'.center(M, '-')] + designer[::-1]))
