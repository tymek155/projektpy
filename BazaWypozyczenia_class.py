from WypozyczAuto_class import WypozyczAuto

class BazaWypozyczenia:
    stan_ilosciowy_historii = 0
    
    def __init__(self):
        self.historia_wypozyczen_w_bazie = []

    def dodaj_wypozyczenie_do_bazy(self, wypozyczenie : WypozyczAuto):
        self.historia_wypozyczen_w_bazie.append(wypozyczenie)
        BazaWypozyczenia.stan_ilosciowy_historii += 1

    def znajdz_wypozyczenie_w_bazie(self, log):
        wynik = []
        for i in self.historia_wypozyczen_w_bazie:
            if i.klient_ktory_wypozyczyl.login == log:
                wynik.append(i)
        return wynik
    
    def wypozyczenie_aktualizacja(self, wypozyczenie : WypozyczAuto):
        for i in self.historia_wypozyczen_w_bazie:
            if i.id_wypozyczenia == wypozyczenie.id_wypozyczenia:
                i = wypozyczenie
                print("Informacje o wypozyczeniu zostaly zaktualizowane. ")
                break