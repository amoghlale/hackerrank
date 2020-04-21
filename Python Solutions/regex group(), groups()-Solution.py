import re
S = input()
print("-1") if not re.search(r'([A-Za-z0-9])\1+', S) else print(re.search(r'([A-Za-z0-9])\1+', S).group(1))
