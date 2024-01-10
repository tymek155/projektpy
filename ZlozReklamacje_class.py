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
        przygotowana_reklamacja.poprawnosc_wypelnienia = int(input("\n\nJesli powyzsze dane sa poprawne wpisz 1, jesli nie wpisz 0: "))

        if(przygotowana_reklamacja.poprawnosc_wypelnienia == 1):
            print("\nReklamacja zostala wypelniona prawidlowo i zostaje dodana do bazy reklamacji oczekujacyh na rozpatrzenie.")
            przygotowana_reklamacja.decyzja = "Brak"
            baza_reklamacji.dodaj_reklamacje_do_bazy(przygotowana_reklamacja)
        else:
            print("Nieprawidlowo wypleniony dokument, rozpocznij proces aplikacji reklamacyjnej jeszcze raz.")

    def uzuplenij_info(self, baza_klientow: BazaKlientow, baza_wypozyczen : BazaWypozyczenia, baza_reklamacji : BazaReklamacji):
        log = input("Podaj login klienta, dla ktorego chcesz wprowadzic reklamaccje: ")
        klient_wypozyczajacy = Klient(None, None, None, None, None, None)
        klient_wypozyczajacy = baza_klientow.znajdz_klienta_w_bazie(log)
        if (klient_wypozyczajacy.login == log):
            nowa_reklamacja = Reklamacja(None, None, None, None)
            nowa_reklamacja.dane_reklamujacego = klient_wypozyczajacy
            print("Znajdz wypozyczenie, ktorego dotyczy reklamacja")
            historia_wypozyczen = baza_wypozyczen.znajdz_wypozyczenie_w_bazie(klient_wypozyczajacy.login)
            print("Historia wypozyczen klienta: ")
            for i in historia_wypozyczen:
                i.pokaz_informacje_wypozyczenie()
            spr = 0
            while(spr == 0):
                id = int(input("Podaj ID wypozyczenia, ktorego ma dotyczyc reklamacja: "))

                for i in historia_wypozyczen:
                    if i.id_wypozyczenia == id:
                        spr =1 
                        print("Podano prawidlowe ID wypozyczenia!")
                        nowa_reklamacja.wypozyczenie_reklamowane = i
                        nowa_reklamacja.dane_pojazdu = i.wypozyczony_samochod
                        break
                
                print("Podano nieprawidlowe ID wypozyczenia, podaj ID jeszcze raz.")
            
            nowa_reklamacja.powod_reklamacji = input("Podaj powod reklamacji: ")
            print("\nReklamacja zostala wypelniona, zaakceptuj wprowadzone dane.")
            self.akceptuj(nowa_reklamacja, baza_reklamacji)
        else:
            print("Brak klienta o podanym loginie!")

            


