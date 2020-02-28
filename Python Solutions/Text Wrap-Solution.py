import textwrap

def wrap(string, max_width):
    wrapped_text_by_width = textwrap.wrap(string, max_width) if max_width < len(string) else None
    return "\n".join(i for i in wrapped_text_by_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
