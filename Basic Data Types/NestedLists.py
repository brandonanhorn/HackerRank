if __name__ == '__main__':
    full_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        full_list.append([name, score])

second_lowest_grade = sorted(list(set(score for name, score in full_list)))[1]
print('\n'.join([a for a, b in sorted(full_list) if b == second_lowest_grade]))
