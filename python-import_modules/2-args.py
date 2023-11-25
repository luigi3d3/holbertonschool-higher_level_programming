#!/usr/bin/python3
from sys import argv

num_args = len(argv) - 1
arg_plural = "arguments" if num_args != 1 else "argument"
end_char = ":" if num_args > 0 else "."

print(f"{num_args} {arg_plural} {end_char}")

for i, arg in enumerate(argv[1:], start=1):
    print(f"{i}: {arg}")
