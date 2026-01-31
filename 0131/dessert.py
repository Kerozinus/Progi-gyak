N, P = map(int, input().strip().split()) # N = Desszertek száma P = Kedvenc gyümölcs

S = list(map(int, input().strip().split())) # Édességi szintek

F = list(map(int, input().strip().split())) # Gyümölcsök

Q = int(input().strip()) # Preferenciák száma

szamlalo = 0

l = [0 for i in range(Q)] # Min. édesség
r = [0 for i in range(Q)] # Max. édesség
k = [0 for i in range(Q)] # Gyümi db

for i in range(Q):
    l[i], r[i], k[i] = map(int, input().strip().split())

# for i in range(N):
#     if S[i] >= l[0] and S[i] <= r[0]:
#         if F[i] == P:
#             szamlalo += 1
#             if szamlalo == k:
#                 print('YES')
#         else:
#             print('NO')
#     else:
#         print('NO')

for i in range(Q):
    szamlalo = 0
    for x in range(N):
        if S[x] >= l[i] and S[x] <= r[i] and F[x] == P:
            szamlalo = szamlalo + 1

    if szamlalo >= k[i]:
            print('YES')
    else:
        print("NO")
                        
