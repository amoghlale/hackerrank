from collections import namedtuple
number_of_students, column_names = (int(input()), ','.join(input().split()))
student_info = namedtuple('student_info', column_names)
print("%.2f" % (sum([int(student_info(*(input().split())).MARKS) for _ in range(number_of_students)])/int(number_of_students)))
