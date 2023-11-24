#!/usr/bin/python3
def uppercase(s):
    for char in s:
        if 'a' <= char <= 'z':
            print("{}".format(chr(ord(char) - ord('a') + ord('A'))), end="")
        else:
            print(char, end="")

uppercase("Best School, 98 Battery street")
