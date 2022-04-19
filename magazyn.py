from funkcje.accountant import odczyt_pliku
from funkcje.accountant import zapis_magazyn
from funkcje.accountant import history
from funkcje.accountant import fd
from funkcje.accountant import plik_do_zapisu
from funkcje.accountant import stan_magazynu

dane = odczyt_pliku(fd)
historia = history(dane)
magazyn = dict()
magazyn=stan_magazynu(magazyn)
zapis_magazyn(plik_do_zapisu, magazyn)