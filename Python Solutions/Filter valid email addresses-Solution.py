import re
def fun(s):
    input_components = re.split("[@.]", s)
    if len(input_components) < 3 or len(input_components) > 3:
        return None
    else:
        username_check = True if re.fullmatch("[A-Za-z0-9^-]+|[A-Za-z0-9^_]+", input_components[0]) else False
        password_check = True if re.fullmatch("[A-Za-z0-9]+", input_components[1]) else False
        extension_check = True if len(input_components[2]) <= 3 else False
        return True if (username_check and password_check and extension_check) else False


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
