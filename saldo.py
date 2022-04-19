import sys
from funkcje.accountant import odczyt_pliku
from funkcje.accountant import zapis_historii
from funkcje.accountant import history
from funkcje.accountant import fd
from funkcje.accountant import plik_do_zapisu

dane = odczyt_pliku(fd)
historia = history(dane)
x = sys.argv[1]
y = sys.argv[2]
saldo = ("saldo", int(x), y)
historia.append(saldo)
zapis_historii(historia, plik_do_zapisu)