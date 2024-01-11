from Osoba_class import Osoba
from Samochod_class import Samochod
#from BazaWypozyczenia_class import BazaWypozyczenia

class Klient(Osoba):
    def __init__(self, im, nazw, pes, pl, log, status):
        super().__init__(im, nazw, pes, pl)
        self.login = log
        self.status_stalego_klienta = status
        self.sprawdz_czy_none = "Brak"

    def jakie_auto(autoa : Samochod):
        print("Podaj dane auta: ")
        m = input("Podaj marke: ")
        rok = int(input("Podaj rok: "))
        przeb = int(input("Podaj przebieg: "))
        il_s = int(input("Podaj ilosc siedzen: "))
        rskrz = input("Podaj rodzaj skryzni biegow: ")

        return Samochod(m, rok, przeb, True, il_s, rskrz, 10, "coupe, 0")
    
    def wyswietl_informacje_o_kliencie(self):
        print("Imie: ", self.imie)
        print("Nazwisko: ", self.nazwisko)
        print("PESEL: ", self.pesel)
        print("Plec: ", self.plec)
        print("Login: ", self.login)
        print("\n")

    def dodaj_klienta_input(self):
        try:
            self.imie = input("Podaj imię: ")
            self.nazwisko = input("Podaj nazwisko: ")
            self.pesel = int(input("Podaj PESEL: "))
            self.plec = input("Podaj płeć: ")
            self.login = input("Podaj indywidualny login: ")
        except ValueError:
            print("Blad! Wprowadzono nieprawidlową wartosc. Upewnij sie, że podajesz liczby tam, gdzie to wymagane.")
            self.sprawdz_czy_none = None
            return None

    def sprawdz_status_stalego_klienta(self, baza_wypozyczen):
        policz_ile_transakcji = 0
        for i in baza_wypozyczen.historia_wypozyczen_w_bazie:
            if i.klient_ktory_wypozyczyl.login == self.login:
                  policz_ile_transakcji += 1

        if policz_ile_transakcji >= 10:
            print("Klient posiada status stalego klienta - posiada dodatkowa znizke na wypozyczenie")
            self.status_stalego_klienta = 1
        else:
            print("Za malo transakcji do statusu stalego klienta!")
            print("Brakujaca ilosc transakcji to: ", 10-policz_ile_transakcji)