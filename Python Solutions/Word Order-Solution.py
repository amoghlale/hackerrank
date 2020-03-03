from collections import OrderedDict
n = int(input())
output_dict = OrderedDict()
for _ in range(n):
    word = input()
    output_dict[word] = output_dict[word] + 1 if word in output_dict else 1
print(len(output_dict))
print(*[value for value in output_dict.values()])
