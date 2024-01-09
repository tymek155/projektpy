from Samochod_class import Samochod
from Klient_class import Klient
from BazaWypozyczenia_class import BazaWypozyczenia

class Zaplata:
    def __init__(self, wypozyczony_samochod : Samochod, uczestnik_transakcji : Klient, baza_wypozyczen: BazaWypozyczenia, ilosc_dni):
        self.kwota = wypozyczony_samochod.oplata_dzienna * ilosc_dni
        self.metoda_platnosci = "Brak"
        print("Sprawdzam czy klient posiada status stalego klienta.")

    def wybierz_metode_platnosci(self):
        print("Wybierz metode platnosci za wypozcyzenie: ")
        print("1. Gotowka")
        print("2. Karta platnicza")
        print("3. BLIK")
        print("4. Zlecenie przelewu.")
        wybor = int(input("Podaj numer wybranej metody: "))
        if (wybor != 1 and wybor != 2 and wybor != 3 and wybor != 4):
             print("Metoda platnosci podana w sposob nieprawidlowy, wybierz jeszcze raz")
             self.wybierz_metode_platnosci()
        return wybor



        
	

