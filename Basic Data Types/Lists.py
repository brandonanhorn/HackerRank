if __name__ == '__main__':
    N = int(input())

def a_list_function(N):
    a_list = []
    for _ in range(N):
        command = input().strip().split(" ")
        cmd_type = command[0]
        if (cmd_type == "print"):
            print(a_list)
        elif (cmd_type == "sort"):
            a_list.sort()
        elif (cmd_type == "reverse"):
            a_list.reverse()
        elif (cmd_type == "pop"):
            a_list.pop()
        elif (cmd_type == "remove"):
            a_list.remove(int(command[1]))
        elif (cmd_type == "append"):
            a_list.append(int(command[1]))
        elif (cmd_type == "insert"):
            a_list.insert(int(command[1]), int(command[2]))

a_list_function(N)
