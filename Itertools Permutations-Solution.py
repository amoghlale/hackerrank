from itertools import permutations

if __name__ == '__main__':
    S, k = input().split()
    if 0 < int(k) <= len(S):
        for each_tuple in sorted(list(permutations(S, int(k)))):
            print(''.join(map(str, each_tuple)))
