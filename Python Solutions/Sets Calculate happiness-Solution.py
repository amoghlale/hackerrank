happiness = 0
n, m = map(int, input().split())
array, A, B = (list(map(int, input().split())), set(map(int, input().split())), set(map(int, input().split())))
for element in array:
    if element in A:
        happiness += 1
    elif element in B:
        happiness -= 1
print(happiness)
