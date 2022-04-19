import sys
from funkcje.accountant import odczyt_pliku
from funkcje.accountant import history
from funkcje.accountant import fd
from funkcje.accountant import plik_do_zapisu

dane = odczyt_pliku(fd)
historia = history(dane)

lsp = int(sys.argv[1])
psp = int(sys.argv[2])+1

with open(plik_do_zapisu, "w") as zapis:
    for idx in range(lsp, psp):
        b = historia[idx]
        for i in range(len(b)):
            zapis.write(str(b[i]) + '\n')
    zapis.write("stop")