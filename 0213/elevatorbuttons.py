#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

# uncomment the two following lines if you want to read/write from files
# sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w')

lo, hi, pos = map(int, input().strip().split()) # lo = Legalsó szint(nem mehet ez alá) hi = legmagasabb (nem mehet fölé) pos = jelenlegi szint

line = sys.stdin.readline().split()
if not line:
    sys.exit(0)

pressedButtons = sys.stdin.readline().strip()

ans = "" # ans = answer megoldas

error = False

# INSERT YOUR CODE HERE

for i in range(len(pressedButtons)):
    if pos > lo and pos < hi:
        if pressedButtons[i] == 'U':
            pos += 1 
        elif pressedButtons[i] == 'D':
            pos -= 1
        elif pressedButtons[i] == '0':
            pos = 0
        ans = pos
    else:
        ans = 'error'
        error = True
        break
if not error:
    ans = pos

print(ans)

sys.stdout.close()


