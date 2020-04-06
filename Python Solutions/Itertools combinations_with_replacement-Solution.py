from itertools import combinations_with_replacement
if __name__ == '__main__':
    S, k = input().split()
    for values in list(combinations_with_replacement(''.join(sorted(list(S))), int(k))):
        print(''.join(values))
