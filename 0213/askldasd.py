#!/usr/bin/env python3
import sys

line = sys.stdin.readline().split()
if not line:
    sys.exit(0)
    
lo, hi, pos = map(int, line) 
pressedButtons = sys.stdin.readline().strip()

ans = "" 
error = False

for char in pressedButtons:
    next_pos = pos
    
    if char == 'U':
        next_pos += 1 
    elif char == 'D':
        next_pos -= 1
    elif char == '0':
        next_pos = 0
    
    if next_pos < lo or next_pos > hi:
        ans = "error"
        error = True
        break
    else:
        pos = next_pos
if not error:
    ans = pos

print(ans)