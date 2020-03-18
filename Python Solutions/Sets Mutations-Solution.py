A, elements_A, N = (int(input()), set(map(int, input().split())), int(input()))
for i in range(N):
    set_mutation_operation, number_of_elements_in_N = input().split()
    elements_N = set(map(int, input().split()))
    if set_mutation_operation == 'update':
        elements_A.update(elements_N)
    elif set_mutation_operation == 'intersection_update':
        elements_A.intersection_update(elements_N)
    elif set_mutation_operation == 'symmetric_difference_update':
        elements_A.symmetric_difference_update(elements_N)
    elif set_mutation_operation == 'difference_update':
        elements_A.difference_update(elements_N)
print(sum(elements_A))
