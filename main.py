def elso():

    szamok = []

    with open('szamok.txt', 'r', encoding='utf-8') as f:
        for i in f:
            szamok.append(int(i))

    eredmeny = szamok[0]

    for x in range(1, len(szamok)):
        eredmeny += szamok[x]

    print(eredmeny)

    with open('asd.txt', 'w', encoding='utf-8') as é:
        é.write(str(eredmeny))

def masodik():

    szamok = []

    with open('szamok2.txt', 'r', encoding='utf-8') as f:
        for i in f:
            szamok.append(int(i))

    for szam in szamok:
        if szam % 2 == 0:

            with open('paros.txt', 'a', encoding='utf-8') as k:
                k.write(str(szam))
                k.write('\n')

        else:

            with open('paratlan.txt', 'a', encoding='utf-8')as a:
                a.write(str(szam))
                a.write('\n')

def harmadik():

    type_C = 0
    szavak = []
    hosszuak = []

    with open('szavak.txt', 'r', encoding='utf-8') as kurva:

        for i in kurva:

            i = i.strip()

            szavak.append(i)
            type_C += 1
            #vagy siman len(szavak), de a type_C viccesebb xdd

            if len(i) > 5:
                hosszuak.append(i)

    out = [type_C, max(szavak, key=len)]

    with open('szavak_out.txt', 'w', encoding='utf-8') as f:
        f.write(str(out))

    with open('hosszu_out.txt', 'w', encoding='utf-8') as h:
        h.write(str(hosszuak))

harmadik()



    


            