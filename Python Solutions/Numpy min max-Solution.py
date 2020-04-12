import numpy
N, _ = map(int, input().split())
print(numpy.max(numpy.min(numpy.array([list(map(int, input().split()))for _ in range(N)]), axis=1)))
