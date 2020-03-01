from collections import Counter


if __name__ == '__main__':
    X = int(input())
    shoe_size_count_dict = Counter(list(map(int, input().split())))
    N = int(input())
    total_amount = 0
    for i in range(N):
        shoe_size, price = map(int, input().split())
        if shoe_size in shoe_size_count_dict and shoe_size_count_dict[shoe_size] != 0:
                total_amount += price
                shoe_size_count_dict[shoe_size] -= 1
    print(total_amount)
