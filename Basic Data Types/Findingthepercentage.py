if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

def find_percentage(n, student_marks):
    marks = student_marks[query_name]
    avg = sum(marks)/len(marks)
    print("%.2f" % avg)

find_percentage(n, student_marks)
