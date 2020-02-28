if __name__ == '__main__':
    N, M = map(int, (input().split()))
    if M == 3*N:
        char = '.|.'
        for i in range(N//2):
            print(((i*char).rjust((M//2)-1, "-") + ".|." + (i*char).ljust((M//2)-1, "-")))
        print("WELCOME".center((3*N), "-"))
        for i in range((N//2)-1, -1, -1):
            print(((i*char).rjust((M//2)-1, "-") + ".|." + (i*char).ljust((M//2)-1, "-")))
