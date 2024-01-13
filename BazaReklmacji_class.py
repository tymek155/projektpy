from Reklamacja_class import Reklamacja
from Klient_class import Klient

class BazaReklamacji:
    stan_ilosciowy_reklamacji_w_bazie = 0

    def __init__(self):
        self.reklamacje_w_bazie = []

    def dodaj_reklamacje_do_bazy(self, nowa_reklamacja : Reklamacja):
        self.reklamacje_w_bazie.append(nowa_reklamacja)
        BazaReklamacji.stan_ilosciowy_reklamacji_w_bazie += 1

    def znajdz_reklamacje_w_bazie(self, reklamujacy_klient : Klient):
        znalezione_reklamacje = []
        for i in self.reklamacje_w_bazie:
            if self.reklamacje_w_bazie.dane_reklamujacego.login == reklamujacy_klient.login:
                znalezione_reklamacje.append(i)
        return znalezione_reklamacje