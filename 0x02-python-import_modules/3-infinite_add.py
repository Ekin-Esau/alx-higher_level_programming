#!/usr/bin/python3
import sys
total = 0

for i in range(len(sys.argv) - 1):
    total += int(sys.argv[i + 1])
print(total)
