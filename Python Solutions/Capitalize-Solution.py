#!/bin/python3 # code provided by hackerrank
import math # code provided by hackerrank
import os # code provided by hackerrank
import random # code provided by hackerrank
import re # code provided by hackerrank
import sys # code provided by hackerrank


def solve(s):
    character_list = [i for i in s]
    i = j = 0
    output_string = ''
    while j < len(character_list):
        if character_list[j] != ' ':
            j += 1
        else:
            output_string += ''.join(character_list[i: j]).capitalize() + ' '
            j += 1
            i = j
    output_string += ''.join(character_list[i: j]).capitalize()
    return output_string

# code provided by hackerrank
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
