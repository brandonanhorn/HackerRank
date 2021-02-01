if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

def a_tuple(n, integer_list):
    l = []
    for i in integer_list:
        l.append(int(i))
    print (hash(tuple((l))))

a_tuple(n, integer_list)
