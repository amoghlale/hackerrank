from itertools import groupby
if __name__ == '__main__':
    [print((len(list(g)), int(k)), end=' ') for k, g in groupby(input())]
