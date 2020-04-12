import numpy
n, _ = map(int, input().split())
A = numpy.array([list(map(int, input().split())) for _ in range(n)], int)
B = numpy.array([list(map(int, input().split())) for _ in range(n)], int)
print(A+B, A-B, A*B, A//B, A%B, A**B, sep='\n')
