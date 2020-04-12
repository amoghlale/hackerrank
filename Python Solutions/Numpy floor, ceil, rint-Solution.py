import numpy
numpy.set_printoptions(sign=' ')
A = numpy.array(list(map(float, input().split())))
print(numpy.floor(A), numpy.ceil(A), numpy.rint(A), sep='\n')
