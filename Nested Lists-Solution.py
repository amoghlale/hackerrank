if __name__ == '__main__':
    input_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        input_list.append([name, score])
    second_lowest_score = sorted(set(score for _, score in input_list))[1]
    [print(name) for name, score in sorted(input_list) if score == second_lowest_score]
