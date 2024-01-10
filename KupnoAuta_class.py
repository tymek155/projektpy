from Samochod_class import Samochod
from BazaAut_class import BazaAut

class KupnoAuta:
    def __init__(self):
        self.czy_operacja_udana = None

    def kupno(self, samochod : Samochod, baza_aut : BazaAut):
        baza_aut.dodaj(samochod)
        if (baza_aut.samochody_w_bazie[-1] == samochod):
            print("Dodano zakupiony samochod do bazy pomyslnie.")
            self.czy_operacja_udana = 1
        else:
            print("Nastapil blad przy dodawaniu do bazy")
            self.czy_operacja_udana = 0