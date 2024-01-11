from datetime import datetime
from Samochod_class import Samochod
from Klient_class import Klient
from WypozyczAuto_class import WypozyczAuto
from BazaWypozyczenia_class import BazaWypozyczenia
from Zaplata_class import Zaplata


class ZwrocAuto:
    def __init__(self):
        self.czy_operacja_udana = None

    def zwroc_auto(self, samochod : Samochod, klient : Klient, wypozyczenie : WypozyczAuto, baza_wypozyczen: BazaWypozyczenia):
        if (samochod.czy_dostepne_do_wypozyczenia == 0):
            podaj_date = input("Podaj date w formacie YYYY-MM-DD: ")
            try:
                wprowadzona_data = datetime.strptime(podaj_date, "%Y-%m-%d")
                print("Wprowadzona data: ", wprowadzona_data)
                wypozyczenie.data_oddania = wprowadzona_data
                baza_wypozyczen.wypozyczenie_aktualizacja(wypozyczenie)
                ilosc_dni = (wypozyczenie.data_oddania - wypozyczenie.data_wypozyczenia).days
                print("Operacja zwrotu samochodu przebiegla pomyslnie, przejscie do procedury zaplaty.")
                self.czy_operacja_udana = 1
                oplac_wypozyczenie = Zaplata(samochod, klient, baza_wypozyczen, ilosc_dni)
                oplac_wypozyczenie.wybierz_metode_platnosci(samochod)
                samochod.czy_dostepne_do_wypozyczenia = 1
            except:
                print("Blad! Nieprawidlowy format daty.")