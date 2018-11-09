from decimal import getcontext
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum = 0
    getcontext().prec = 3
    for mark in student_marks[query_name]:
        sum += mark
    average = sum / len(student_marks[query_name])
    print("{0:.2f}".format(average))