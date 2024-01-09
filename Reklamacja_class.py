from Klient_class import Klient
from Samochod_class import Samochod
from WypozyczAuto_class import WypozyczAuto

class Reklamacja:
    def __init__(self, klient : Klient, samochod : Samochod, wypozyczenie : WypozyczAuto, powod):
        self.dane_reklamujacego = klient
        self.dane_pojazdu = samochod
        self.powod_reklamacji = powod
        self.decyzja = "Brak"
        self.poprawnosc_wypelnienia = 0
        self.wypozyczenie_reklamowane = wypozyczenie

    def sprawdz_stan_rozpatrzenia(self):
        if self.decyzja != "Brak":
            print("Reklamacja zostala rozpatrzona, decyzja to: ", self.powod_reklamacji)
        else:
            print("Reklamacja nie zostala rozpatrzona")