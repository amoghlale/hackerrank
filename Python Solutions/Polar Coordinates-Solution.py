import cmath
if __name__ == '__main__':
    complex_number = input()
    char_list = [index for index, i in enumerate(complex_number) if i == '+' or i == '-']
    x, y = float(complex_number[: char_list[-1]]), float(complex_number[char_list[-1]: -1])
    print(abs(complex(x, y)))
    print(cmath.phase(complex(x, y)))
