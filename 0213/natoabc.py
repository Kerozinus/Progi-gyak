#!/usr/bin/env python3
# NOTE: it is recommended to use this even if you don't understand the following code.

import sys

# uncomment the two following lines if you want to read/write from files
# sys.stdin = open('input.txt')
# sys.stdout = open('output.txt', 'w')

S = input().strip()

T = ""

asd = [ "alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliett", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "romeo", "sierra", "tango", "uniform", "victor", "whiskey", "xray", "yankee", "zulu" ]


# INSERT YOUR CODE HERE
# "alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india", "juliett", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "romeo", "sierra", "tango", "uniform", "victor", "whiskey", "xray", "yankee", "zulu"


# for i in range(len(S)):
#     # if i[0:2] == asd[i[0:2]]:
#     print(S[0:2],asd[i(2)])

szavak = []
szamlalo = 1

for i in range(len(S)):
    if S[:szamlalo] == "alpha" or "bravo" or "charlie" or "delta" or "echo" or "foxtrot" or "golf" or "hotel" or "india" or "juliett" or "kilo" or "lima" or "mike" or "november" or "oscar" or "papa" or "quebec" or "romeo" or "sierra" or "tango" or "uniform" or "victor" or "whiskey" or "xray" or "yankee" or "zulu":
        szavak.append(S[:szamlalo])
        S[szamlalo:]
        
    else:
        szamlalo += 1

for i in range(szavak):
    T+=(i[:1])
    print(T)

sys.stdout.close()
