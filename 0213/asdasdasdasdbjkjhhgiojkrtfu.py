S = input().strip()

nato = {
    "alpha": "a", "bravo": "b", "charlie": "c", "delta": "d",
    "echo": "e", "foxtrot": "f", "golf": "g", "hotel": "h",
    "india": "i", "juliett": "j", "kilo": "k", "lima": "l",
    "mike": "m", "november": "n", "oscar": "o", "papa": "p",
    "quebec": "q", "romeo": "r", "sierra": "s", "tango": "t",
    "uniform": "u", "victor": "v", "whiskey": "w", "xray": "x",
    "yankee": "y", "zulu": "z"
}

T = ""

while S:
    for word in nato:
        if S.startswith(word):
            T += nato[word]
            S = S[len(word):]
            break

print(T)
