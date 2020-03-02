from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    A = defaultdict(list)
    for index in range(1, n+1):
        word = input()
        A[word].append(index)
    for index in range(1, m+1):
        word = input() 
        print(*(A[word])) if word in A else print("-1")
