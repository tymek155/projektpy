from datetime import datetime
from Klient_class import Klient
from Samochod_class import Samochod
from BazaWypozyczenia_class import BazaWypozyczenia

class WypozyczAuto:
    licznik = 10000
    
    def __init__(self):
        self.czy_operacja_udana
        self.id_wypozyczenia
        self.klient_ktory_wypozyczyl
        self.wypozyczony_samochod
        self.data_wypozyczenia
        self.data_oddania = "Brak"

    def wypozycz(self, klient :Klient, autoa : Samochod, rejestr_wypozyczen : BazaWypozyczenia):
        if autoa.czy_dostepne_do_wypozyczenia == 1:
            self.klient_ktory_wypozyczyl = klient
            self.wypozyczony_samochod = autoa
            self.id_wypozyczenia = WypozyczAuto.licznik
            WypozyczAuto.licznik += 1
            self.wypozyczony_samochod.czy_dostepne_do_wypozyczenia = 0
            self.data_wypozyczenia = datetime.today()
            self.czy_operacja_udana = 1
            print("Operacja wypozyczenia samochodu przebiegla pomyslnie.")
        else:
            print("Auto ktore chcesz wypozyczyc jest niedostepne.")

    def pokaz_informacje_wypozyczenie(self):
        print("Numer ID wypozyczenia: ", self.id_wypozyczenia)
        print("Data wypozyczenia: ", self.data_wypozyczenia)
        print("Data oddania: ", self.data_oddania)
        self.wypozyczony_samochod.podaj_info_do_dok_wypozyczenia()



