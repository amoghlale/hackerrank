from itertools import product
"""
element_list = [[5, 4], [7, 8, 9], [5, 7, 8, 9, 10]]
product(*element_list) creates a tuple of 1 element from each list and appends to an output list==> [(5, 7, 5), (5, 7, 7)...]   
"""
if __name__ == '__main__':
    K, M = map(int, input().split())
    element_list = []
    for _ in range(K):
        K_elements  = list(map(int, input().split()[1:]))
        element_list.append(K_elements)
    smax = 0
    for X in product(*element_list):
        sum_of_squares = sum([i ** 2 for i in X])
        if sum_of_squares % M > smax:
            smax = sum_of_squares % M
    print(smax)
