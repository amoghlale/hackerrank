from itertools import combinations


if __name__ == '__main__':
    S, k = input().split()
    k = int(k)
    if k <= len(S):
        output_list = []
        for i in range(1, k+1):
            output_list.extend(list(combinations(sorted(S), i)))
        print("\n".join(''.join(i) for i in output_list))
