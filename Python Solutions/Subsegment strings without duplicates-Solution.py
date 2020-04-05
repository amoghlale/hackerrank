'''
counter i iterates over entire string
counter j is set to 0 after iterating k times
i_counter   0   1   2   3   4   5   6   7   8
string      A   A   B   C   A   A   A   D   A
j_counter   0   1   2   0   1   2   0   1   2
Complexity -> O(n)
'''
def merge_the_tools(string, k):
    i = j = 0
    u = []
    while i <= len(string) - 1:
        if j == k:
            print(''.join(u))
            u = []
            j = 0
        if string[i] not in u:
            u.append(string[i])
        i += 1
        j += 1
    print(''.join(u))

        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
