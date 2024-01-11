from BazaKlientow_class import BazaKlientow
from BazaWypozyczenia_class import BazaWypozyczenia
from BazaReklmacji_class import BazaReklamacji
from Klient_class import Klient
from Reklamacja_class import Reklamacja

class ZlozReklamacje:
    def __init__(self):
        self.czy_operacja_udana = None

    def akceptuj(self, przygotowana_reklamacja : Reklamacja, baza_reklamacji: BazaReklamacji):
        print("Informacje o skladajacym reklamacje: ")
        przygotowana_reklamacja.dane_reklamujacego.wyswietl_informacje_o_kliencie()
        przygotowana_reklamacja.dane_pojazdu.podaj_info_do_dok_wypozyczenia()
        print("Powod zlozenia reklamacji: ", przygotowana_reklamacja.powod_reklamacji)
        try:
            przygotowana_reklamacja.poprawnosc_wypelnienia = int(input("\n\nJesli powyzsze dane sa poprawne wpisz 1, jesli nie wpisz 0: "))
            if(przygotowana_reklamacja.poprawnosc_wypelnienia == 1):
                print("\nReklamacja zostala wypelniona prawidlowo i zostaje dodana do bazy reklamacji oczekujacyh na rozpatrzenie.")
                przygotowana_reklamacja.decyzja = "Brak"
                baza_reklamacji.dodaj_reklamacje_do_bazy(przygotowana_reklamacja)
            else:
                print("Nieprawidlowo wypleniony dokument, rozpocznij proces aplikacji reklamacyjnej jeszcze raz.")
        except ValueError:
            print("Blad, wprowadzono nieprawidlowa wartosc!")

    def uzuplenij_info(self, baza_klientow: BazaKlientow, baza_wypozyczen: BazaWypozyczenia, baza_reklamacji: BazaReklamacji):
        log = input("Podaj login klienta, dla ktorego chcesz wprowadzic reklamacje: ")
        klient_wypozyczajacy = baza_klientow.znajdz_klienta_w_bazie(log)

        if klient_wypozyczajacy is None:
            print("Nie znaleziono klienta o podanym loginie.")
            return None

        nowa_reklamacja = Reklamacja(None, None, None, None)
        nowa_reklamacja.dane_reklamujacego = klient_wypozyczajacy

        print("Znajdz wypozyczenie, ktorego dotyczy reklamacja")
        historia_wypozyczen = baza_wypozyczen.znajdz_wypozyczenie_w_bazie(klient_wypozyczajacy.login)

        if not historia_wypozyczen:
            print("Brak wypozyczen dla tego klienta.")
            return

        print("\nHistoria wypozyczen klienta: ")
        for i in historia_wypozyczen:
            sprawdz_czy_zostalo_wyswietlone = 0
            if i.data_oddania != "Brak":
                i.pokaz_informacje_wypozyczenie()
                print("\n")
                sprawdz_czy_zostalo_wyswietlone = 1

        if sprawdz_czy_zostalo_wyswietlone == 0:
            print("Brak wypozyczen do zareklamowania.")
            return None

        while True:
            try:
                id_wypozyczenia = int(input("Podaj ID wypozyczenia, ktorej ma dotyczyc reklamacja: "))
                wypozyczenie = None
                for i in historia_wypozyczen:
                    if i.id_wypozyczenia == id_wypozyczenia:
                        wypozyczenie = i
                
                if wypozyczenie == None:
                    print("Brak wypozyczenia o podanym ID!")
                    return None

                if wypozyczenie.data_oddania == "Brak":
                    print("Wybrano wypozyczenie, ktore nie zostalo jeszcze zrealizowane.")
                    print("Blad operacji!")   
                    return None

                if wypozyczenie:
                    nowa_reklamacja.wypozyczenie_reklamowane = wypozyczenie
                    nowa_reklamacja.dane_pojazdu = wypozyczenie.wypozyczony_samochod
                    break
                else:
                    print("Podano nieprawidlowe ID wypozyczenia, podaj ID jeszcze raz.")
            except ValueError:
                print("Blad! Podano nieprawidlowa wartosc. Wprowadz numer ID jako liczbe całkowita.")

        nowa_reklamacja.powod_reklamacji = input("Podaj powod reklamacji: ")
        print("\nReklamacja zostala wypelniona, zaakceptuj wprowadzone dane.")
        self.akceptuj(nowa_reklamacja, baza_reklamacji)
