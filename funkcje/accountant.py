fd = "in.txt"
plik_do_zapisu = "plik_do_zapisu.txt"
lista = ["saldo", "sprzedaz", "zakup","stop"]
akcje = ["saldo", "sprzedaz", "zakup", "konto", "magazyn", "przeglad" ]

stan_salda = 0
magazyn = dict()


def stan_magazynu(magazyn):

    for i in range(len(historia)):  # magazyn
        b = historia[i]
        if b[0] == akcje[2]:
            if b[1] in magazyn:
                magazyn[b[1]] += b[3]
            else:
                magazyn = {b[1]: b[3]}
        if b[0] == akcje[1]:
            if b[1] in magazyn:
                magazyn[b[1]] -= b[3]
    return (magazyn)


def stan_konta():

    stan_salda=0
    for i in range(len(historia)):  # stan salda
        b = historia[i]
        if b[0] == akcje[0]:
            stan_salda += b[1]
        if b[0] == akcje[1]:
            stan_salda += b[2] * b[3]
        if b[0] == akcje[2]:
            stan_salda -= b[2] * b[3]
    return stan_salda


def zapis_magazyn(plik_do_zapisu, magazyn):
    with open(plik_do_zapisu,'w') as zapis:# magazyn
        for k, v in magazyn.items():
            zapis.write("{}: {}".format(k, v))


def odczyt_pliku(fd):
    with open(fd,'r') as plik:
        dane_z_pliku = plik.read()
        dane = dane_z_pliku.split('\n')
        return dane

def zapis_historii(historia,plik_do_zapisu):
    with open(plik_do_zapisu, "w") as zapis:
        for idx in range(len(historia)):
            b = historia[idx]
            for i in range(len(b)):
                zapis.write(str(b[i])+'\n')
        zapis.write("stop")


def history(dane):
    historia = []
    for idx in range(len(dane)):
        if dane[idx] == lista[0]:
            if dane[idx + 3] not in lista:
                print('Błędna akcja, program przerywa pracę!')
                break
            saldo = (dane[idx], int(dane[idx + 1]), (dane[idx + 2]))
            historia.append(saldo)
        elif dane[idx] == lista[1]:
            if dane[idx + 4] not in lista:
                print('Błędna akcja, program przerywa pracę!')
                break
            sprzedaz = (dane[idx], (dane[idx + 1]), int(dane[idx + 2]),
                        int(dane[idx + 3]))
            historia.append(sprzedaz)
        elif dane[idx] == lista[2]:
            if dane[idx + 4] not in lista:
                print('Błędna akcja, program przerywa pracę!')
                break
            zakup = (dane[idx], dane[idx + 1], int(dane[idx + 2]),
                     int(dane[idx + 3]))
            historia.append(zakup)
    return historia


dane = odczyt_pliku(fd)
historia = history(dane)