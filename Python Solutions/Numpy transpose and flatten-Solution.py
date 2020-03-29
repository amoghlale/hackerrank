import numpy
if __name__ == '__main__':
    n, m = map(int, input().split())
    input_array = numpy.array([list(map(int, input().split())) for _ in range(n)])
    print(numpy.transpose(input_array))
    print(input_array.flatten())
