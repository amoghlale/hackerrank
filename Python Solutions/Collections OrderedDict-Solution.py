from collections import OrderedDict
output_ordered_dictionary = OrderedDict()
for _ in range(int(input())):
    row = input().split()
    name, cost = (' '.join(row[:-1]), int(row[-1]))
    output_ordered_dictionary[name] = output_ordered_dictionary[name] + cost if name in output_ordered_dictionary else cost
[print(key, value) for key, value in output_ordered_dictionary.items()]
