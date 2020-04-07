import re
if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        input_value = input()
        if re.match("^[-+]([0-9]*)[.]([0-9]+)$|^([0-9]*)[.]([0-9]+)$", input_value):
            try:
                float(input_value)
                print("True")
            except:
                print("Cannot be converted to float")
        else:
            print("False")
