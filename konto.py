
from funkcje.accountant import odczyt_pliku
from funkcje.accountant import history
from funkcje.accountant import fd
from funkcje.accountant import plik_do_zapisu
from funkcje.accountant import stan_konta


dane = odczyt_pliku(fd)
historia = history(dane)
konto = str(stan_konta())
with open(plik_do_zapisu, 'w') as zapis:  # magazyn
        zapis.write(konto)