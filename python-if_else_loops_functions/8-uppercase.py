#!/usr/bin/python3
def uppercase(s):
    output = ""
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            output += "{}".format(chr(ord(char) - ord('a') + ord('A')))
        else:
            output += char
    print(output)
