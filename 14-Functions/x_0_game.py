from random import choice

def bosh_doska_hosil_qil():
    doska = []
    raqam = 1
    for i in range(3):
        qator = []
        for j in range(3):
            qator.append(str(raqam))
            raqam += 1
        doska.append(qator)
    return doska

def doskani_korsat(doska):
    print("+-------+-------+-------+")
    for i in range(3):
        print("|       |       |       |")
        print(f"|   {doska[i][0]}   |   {doska[i][1]}   |   {doska[i][2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def bosh_maydonlar(doska):
    boshlar = []
    for i in range(3):
        for j in range(3):
            if doska[i][j].isdigit():
                boshlar.append((i, j))
    return boshlar

def golib_bormi(doska, belgi):
    for i in range(3):  
        if doska[i][0] == belgi and doska[i][1] == belgi and doska[i][2] == belgi:
            return True
        if doska[0][i] == belgi and doska[1][i] == belgi and doska[2][i] == belgi:
            return True
    if doska[0][0] == belgi and doska[1][1] == belgi and doska[2][2] == belgi:
        return True
    if doska[0][2] == belgi and doska[1][1] == belgi and doska[2][0] == belgi:
        return True
    return False

def foydalanuvchi_tanlasin(doska):
    while True:
        tanlov = input("Sizning galingiz: ")
        for i in range(3):
            for j in range(3):
                if doska[i][j] == tanlov:
                    doska[i][j] = "O"
                    return
        print("Xato! Boshqa raqam kiriting.")

def strategik_yurish(doska, belgi):
    for i in range(3):
        for j in range(3):
            if doska[i][j].isdigit():
                doska[i][j] = belgi
                if golib_bormi(doska, belgi):
                    return (i, j)
                doska[i][j] = str(i * 3 + j + 1)
    return None

def kompyuter_tanlasin(doska):
    yurish = strategik_yurish(doska, "X")  
    if not yurish:
        yurish = strategik_yurish(doska, "O")  
    if not yurish and doska[1][1] == "5":  
        yurish = (1, 1)
    if not yurish:
        burchaklar = []
        for i, j in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            if doska[i][j].isdigit():
                burchaklar.append((i, j))
        if burchaklar:
            yurish = choice(burchaklar)
    if not yurish:
        boshlar = bosh_maydonlar(doska)
        yurish = choice(boshlar)
    doska[yurish[0]][yurish[1]] = "X"

while True:
    doska = bosh_doska_hosil_qil()
    doskani_korsat(doska)
    while True:
        foydalanuvchi_tanlasin(doska)
        doskani_korsat(doska)
        if golib_bormi(doska, "O"):
            print("Siz yutdingiz!")
            break
        if not bosh_maydonlar(doska):
            print("Durrang!")
            break
        kompyuter_tanlasin(doska)
        doskani_korsat(doska)
        if golib_bormi(doska, "X"):
            print("Kompyuter yutdi!")
            break
        if not bosh_maydonlar(doska):
            print("Durrang!")
            break
    yana = input("Yana o'ynaysizmi? (ha/yo'q): ").lower()
    if yana != "ha":
        break
