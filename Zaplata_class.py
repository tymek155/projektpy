from Samochod_class import Samochod
from Klient_class import Klient
from BazaWypozyczenia_class import BazaWypozyczenia
from MetodyPlatnosci_class import MetodyPlatnosci

class Zaplata:
    def __init__(self, wypozyczony_samochod : Samochod, uczestnik_transakcji : Klient, baza_wypozyczen: BazaWypozyczenia, ilosc_dni):
        self.kwota = wypozyczony_samochod.oplata_dzienna * ilosc_dni
        self.metoda_platnosci = "Brak"
        print("Sprawdzam czy klient posiada status stalego klienta.")
        uczestnik_transakcji.sprawdz_status_stalego_klienta(baza_wypozyczen)
        if uczestnik_transakcji.status_stalego_klienta == 1:
            print("Transakcja zostanie zrealizowana z obnizka dla stalego klienta")
            self.kwota = 0.9*self.kwota

    def wybierz_metode_platnosci(self,samochod:Samochod):
        print("Wybierz metode platnosci za wypozcyzenie: ")
        print("1. Gotowka")
        print("2. Karta platnicza")
        print("3. BLIK")
        print("4. Zlecenie przelewu.")
        wybor = int(input("Podaj numer wybranej metody: "))
        if (wybor != 1 and wybor != 2 and wybor != 3 and wybor != 4):
             print("Metoda platnosci podana w sposob nieprawidlowy, wybierz jeszcze raz")
             self.wybierz_metode_platnosci()
        else:
            if wybor==1:
                self.metoda_platnosci="Gotowka"
            elif wybor==2:
                self.metoda_platnosci="Karta Platnicza"
            elif wybor==3:
                self.metoda_platnosci="BLIK"
            else:
                self.metoda_platnosci="Przelew"
        platnosc=MetodyPlatnosci(self.kwota, self.metoda_platnosci)
        platnosc.zaplac(samochod)



        
	

