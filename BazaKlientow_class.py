from Klient_class import Klient

class BazaKlientow:
    ilosc_klientow_w_bazie = 0

    def __init__(self):
        self.klienci_w_bazie = set()

    def dodaj_klienta_do_bazy(self, klient : Klient):
        self.klienci_w_bazie.add(klient)
        BazaKlientow.ilosc_klientow_w_bazie += 1

    def znajdz_klienta_w_bazie(self, log):
        for i in self.klienci_w_bazie:
            if i.login == log:
                return i
        return None
    
    def wyswietl_baze_klientow(self):
        for i in self.klienci_w_bazie:
            i.wyswietl_informacje_o_kliencie()
