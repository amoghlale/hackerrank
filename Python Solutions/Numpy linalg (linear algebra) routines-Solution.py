import numpy
numpy.set_printoptions(legacy='1.13')
input_list = [list(map(float, input().split())) for _ in range(int(input()))]
print(numpy.linalg.det(input_list))
