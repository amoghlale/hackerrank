if __name__ == '__main__':
    for _ in range(int(input())):
        _, set_A, _, set_B = (int(input()),set(map(int, input().split())), int(input()),set(map(int, input().split())))
        print(set_A.issubset(set_B))
