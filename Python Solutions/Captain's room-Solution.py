"""
sample input
k = 3
entry_list = 1   2   3   1   3   4   1   4   3   4
set(entry_list) = 1, 2, 3, 4 => sum(set(entry_list)) = 10
Expected_sum if all numbers repeated k times = sum(set(entry_list))*k => 10*3 => 30
Actual sum => sum(entry_list) = 26
(k-1)x = expected - actual => 2x = 30-26 => x = 2
"""
if __name__ == '__main__':
    K, entry_list = (int(input()), list(map(int, input().split())))
    print((sum(set(entry_list)) * K - sum(entry_list))//(K-1))
