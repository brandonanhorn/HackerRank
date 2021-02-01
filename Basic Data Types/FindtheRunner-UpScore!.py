if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

def second_place(n, arr):
    arr = list(set(list(arr)))
    arr_1 = len(arr)
    arr = sorted(arr)
    print(arr[arr_1-2])


second_place(n, arr)
