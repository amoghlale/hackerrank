from collections import deque
d, N = (deque(), int(input()))
for _ in range(N):
    command = input()
    if 'append' in command or 'appendleft' in command:
        operation, value = command.split()
        d.append(value) if operation == 'append' else d.appendleft(value)
    elif 'popleft' in command:
        d.popleft()
    else:
        d.pop()
print(*d)
