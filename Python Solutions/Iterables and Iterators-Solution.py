from itertools import combinations
if __name__ == '__main__':
    N, c, k = (int(input()), input().replace(" ", ""), int(input()))
    char_combinations = list(combinations(c, k))
    print(len([i for i in char_combinations if 'a' in i])/len(char_combinations))
