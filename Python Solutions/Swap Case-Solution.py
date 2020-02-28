def swap_case(s):
    output_string = ""
    for string_character in s:
        if 97 <= ord(string_character) <= 122:
            output_string += chr(ord(string_character) - 32)
        elif 65 <= ord(string_character) <= 90:
            output_string += chr(ord(string_character) + 32)
        else:
            output_string += string_character
    return output_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
