if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    if n >= 2: 
        print(sorted(set(arr))[-2])