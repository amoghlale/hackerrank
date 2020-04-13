import numpy
dimensions = tuple(map(int, input().split()))
print(numpy.array(numpy.zeros(dimensions, dtype=numpy.int)))
print(numpy.array(numpy.ones(dimensions, dtype=numpy.int)))
