def wrapper(f):
    def fun(l):
        f(map(lambda x: '+91 ' + x[: 5] + ' ' + x[5: ], [num[len(num) - 10: ] for num in l]))
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
