T = int(input())
for _ in range(T):
    n = int(input())
    max_sidelength= pow(2, 31)
    no_flag = 0
    sidelength_values = list(map(int, (input().split())))
    while len(sidelength_values) != 0:
        if max(sidelength_values[0], sidelength_values[-1]) == sidelength_values[0] and sidelength_values[0] <= max_sidelength:
            max_sidelength = sidelength_values[0]
            del[sidelength_values[0]]
        elif max(sidelength_values[0], sidelength_values[-1]) == sidelength_values[-1] and sidelength_values[-1] <= max_sidelength:
            max_sidelength = sidelength_values[-1]
            del[sidelength_values[-1]]
        else:
            print("No")
            no_flag = 1
            break
    if no_flag == 0:
        print("Yes")
