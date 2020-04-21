import re
S = input()
pattern = re.compile(input())
match_obj = pattern.search(S)
if match_obj is None:
    print("(-1, -1)")
while match_obj:
    print("({}, {})".format(match_obj.start(), match_obj.end()-1))
    match_obj = pattern.search(S, match_obj.start()+1)
