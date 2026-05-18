merkozesek = []
sorok = 0
with open("0518\merkozesek.txt","r",encoding="utf-8")as b:
    for i in b:
        sorok += 1
        merkozesek.append(i.strip().split(";"))
print(f"A héten játszott csapatok száma: {sorok*2}")
print(f"C betűvel kezdődő csapatok: ")
for c in range(0,sorok):
    if merkozesek[c][0].startswith("C") or merkozesek[c][0].startswith("c"):
        print(merkozesek[c][0])
    if merkozesek[c][1].startswith("C") or merkozesek[c][1].startswith("c"):
        print(merkozesek[c][0])
dontetlenek = 0
for x in range(0,sorok):
    if merkozesek[x][4] == "x" or merkozesek[x][4] == "X":
        dontetlenek += 1
print(f"{dontetlenek} mérkőzés végződött döntetlenre.")
with open("0518\goltalanok.txt","w",encoding="utf-8")as g:
    g.write("Gólt nem szerző csapatok:")
    g.write("\n")
    for n in range(0,sorok):
        if merkozesek[n][2] == "0":
            g.write(merkozesek[n][0])
            g.write("\n")
        if merkozesek[n][3] == "0":
            g.write(merkozesek[n][1])
            g.write("\n")