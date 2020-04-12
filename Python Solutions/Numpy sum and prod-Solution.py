import numpy
N, _ = map(int, input().split())
print(numpy.prod(numpy.sum(numpy.array([list(map(int, input().split())) for _ in range(N)]), axis=0)))
