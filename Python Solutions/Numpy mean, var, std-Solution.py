import numpy
numpy.set_printoptions(sign=' ', legacy='1.13')
N, _ = map(int, input().split())
input_array = numpy.array([list(map(int, input().split())) for _ in range(N)], int)
print(numpy.mean(input_array, axis=1), numpy.var(input_array, axis=0), numpy.std(input_array, axis=None), sep='\n')
