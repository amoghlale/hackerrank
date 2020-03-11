if __name__ == '__main__':
    n, english, b, french = (int(input()), map(int, input().split()), int(input()), map(int, input().split()))
    print(len(set(english).intersection(set(french))))
