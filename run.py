import copy
######################Pobranie_danych_z_pliku
fileName = "test.txt"
v = []
with open(fileName, 'r') as file:
    for line in file:
        if line.split():
            line = [float(x) for x in line.split()]
            v.append(line)
file.close()

y = 0.5
########################Rozbicie_danych_na_dwie_tablice
Typetab = []
RTab = []
potTab = []

Typetab.append([0, 0, 0, 0, 0, 0])
Typetab.append(v[1])
Typetab[1].insert(0, 0)
Typetab[1].insert(5, 0)
Typetab.append(v[2])
Typetab[2].insert(0, 0)
Typetab[2].insert(5, 0)
Typetab.append(v[3])
Typetab[3].insert(0, 0)
Typetab[3].insert(5, 0)
Typetab.append([0, 0, 0, 0, 0, 0])


RTab.append([0, 0, 0, 0, 0, 0])
RTab.append(v[4])
RTab[1].insert(0, 0)
RTab[1].insert(5, 0)
RTab.append(v[5])
RTab[2].insert(0, 0)
RTab[2].insert(5, 0)
RTab.append(v[6])
RTab[3].insert(0, 0)
RTab[3].insert(5, 0)
RTab.append([0, 0, 0, 0, 0, 0])


rozTab = []
potTab = [[0] * 4 for i in range(int(v[0][1]))]


################Obliczenia
V = copy.deepcopy(RTab)
i = 0
while i < 100:
    Vstare = copy.deepcopy(V)
    for wiersz in range(1, int(v[0][1]) + 1):# 3
        for z in range(1, int(v[0][0]) + 1):# 4

            if Typetab[wiersz][z] == 1:
                listVmax = []

            #ruch_Do_Góry
                polaprawdgora = [0, 0, 0, 0] # na lewo, do przodu, na prawo, swoje miejsce
                if Typetab[wiersz - 1][z] == 0 or (wiersz - 1 < 0):    #przód
                    polaprawdgora[3] += 0.8#Swoje Pole
                else:
                    polaprawdgora[1] += 0.8# ruch do przodu
                if Typetab[wiersz][z - 1] == 0 or (z - 1 < 0):     #lewo
                    polaprawdgora[3] += 0.1#swoje pole
                else:
                    polaprawdgora[0] += 0.1# ruch na lewo
                if Typetab[wiersz][z + 1] == 0 or (z + 1 > int(v[0][0])):     #prawo
                    polaprawdgora[3] += 0.1#swoje_pole
                else:
                    polaprawdgora[2] += 0.1# na prawo
                listVmax.append((polaprawdgora[0] * V[wiersz][z - 1]) + (polaprawdgora[1] * V[wiersz - 1][z]) +
                                (polaprawdgora[2] * V[wiersz][z + 1]) + (polaprawdgora[3] * V[wiersz][z]))

            # ruch_w_prawo
                polaprawdpraw = [0, 0, 0, 0]  # na lewo, do przodu, na prawo, swoje miejsce
                if Typetab[wiersz][z + 1] == 0 or (z + 1 > int(v[0][0])):  # przód
                    polaprawdpraw[3] += 0.8  # Swoje Pole
                else:
                    polaprawdpraw[1] += 0.8  # ruch do przodu
                if Typetab[wiersz - 1][z] == 0 or (wiersz - 1 < 0):  # lewo
                    polaprawdpraw[3] += 0.1  # swoje pole
                else:
                    polaprawdpraw[0] += 0.1  # ruch na lewo
                if Typetab[wiersz + 1][z] == 0 or (wiersz + 1 > int(v[0][1])):  # prawo
                    polaprawdpraw[3] += 0.1  # swoje_pole
                else:
                    polaprawdpraw[2] += 0.1  # na prawo

                listVmax.append((polaprawdpraw[0] * V[wiersz - 1][z]) + (polaprawdpraw[1] * V[wiersz][z + 1]) +
                                (polaprawdpraw[2] * V[wiersz + 1][z]) + (polaprawdpraw[3] * V[wiersz][z]))

        #ruch_w_dół
                polaprawddol = [0, 0, 0, 0]  # na lewo, do przodu, na prawo, swoje miejsce
                if Typetab[wiersz + 1][z] == 0 or (wiersz + 1 > int(v[0][1])):  # przód
                    polaprawddol[3] += 0.8  # Swoje Pole
                else:
                    polaprawddol[1] += 0.8  # ruch do przodu
                if Typetab[wiersz][z + 1] == 0 or (z + 1 > v[0][0]):  # lewo
                    polaprawddol[3] += 0.1  # swoje pole
                else:
                    polaprawddol[0] += 0.1  # ruch na lewo
                if Typetab[wiersz][z - 1] == 0 or (z - 1 < 0):  # prawo
                    polaprawddol[3] += 0.1  # swoje_pole
                else:
                    polaprawddol[2] += 0.1  # na prawo
                listVmax.append((polaprawddol[0] * V[wiersz][z + 1]) + (polaprawddol[1] * V[wiersz + 1][z]) +
                                (polaprawddol[2] * V[wiersz][z - 1]) + (polaprawddol[3] * V[wiersz][z]))

        # ruch_w_lewo
                polaprawdlewa = [0, 0, 0, 0]  # na lewo, do przodu, na prawo, swoje miejsce
                if Typetab[wiersz][z - 1] == 0 or (wiersz - 1 < 0):  # przód
                    polaprawdlewa[3] += 0.8  # Swoje Pole
                else:
                    polaprawdlewa[1] += 0.8  # ruch do przodu
                if Typetab[wiersz + 1][z] == 0 or (wiersz + 1 > int(v[0][1])):  # lewo
                    polaprawdlewa[3] += 0.1  # swoje pole
                else:
                    polaprawdlewa[0] += 0.1  # ruch na lewo
                if Typetab[wiersz - 1][z] == 0 or (wiersz - 1 < 0):  # prawo
                    polaprawdlewa[3] += 0.1  # swoje_pole
                else:
                    polaprawdlewa[2] += 0.1  # na prawo
                listVmax.append((polaprawdlewa[0] * V[wiersz + 1][z]) + (polaprawdlewa[1] * V[wiersz][z - 1]) +
                                (polaprawdlewa[2] * V[wiersz - 1][z]) + (polaprawdlewa[3] * V[wiersz][z]))

                Vwynik = RTab[wiersz][z] + y * max(listVmax)
                Vstare[wiersz][z] = copy.deepcopy(Vwynik)
                index = listVmax.index(max(listVmax))
                potTab[wiersz - 1][z - 1] = index + 1



    for xz in range(len(V)):
        for xy in range(len(V[xz])):
            rozTab.append(abs(Vstare[xz][xy] - V[xz][xy])) #Sprawdzić czy od razu odejmą się dwie tablice
    if max(rozTab) < 10**(-4):
        break
    rozTab.clear()

    V = copy.deepcopy(Vstare)
    i += 1



print("Ilość iteracji: ", i)
#dalej
for i in range(len(V)):
    for z in range(len(V[0])):
        x = V[i][z]
        V[i][z] = round(x, 4)

for i in V:
    print(i)
print("\n")
for i in potTab:
    print(i)