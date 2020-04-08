if __name__ == '__main__':
    A = set(map(int, input().split()))
    output = True
    for _ in range(int(input())):
        output = output and True if A > set(map(int, input().split())) else output and False
    print(output)
