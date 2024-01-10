from datetime import datetime

class Samochod:
    def __init__(self, marka, rocz, przeb, st, ils, skrz, pojemn, rodz, data, adn, czyd, opltd):
        self.rocznik = rocz
        self.marka =marka
        self.przebieg = przeb
        self.stan = st
        self.ilosc_siedzen = ils
        self.skrzynia_biegow = skrz
        self.pojemnosc_bagaznika = pojemn
        self.rodzaj = rodz
        self.data_badania_technicznego = data
        self.adnotacja_naprawa = adn
        self.czy_dostepne_do_wypozyczenia = czyd
        self.oplata_dzienna = opltd

    def stworz_auto_input(self):
        self.rocznik = int(input("Podaj rok produkcji samochodu: "))
        self.marka = input("Podaj marke: ")
        self.przbieg = int(input("Podaj przebieg: "))
        self.stan = int(input("Podaj 1 jesli stan jest dobyr lub 0 jesli stan samochodu jest zly: "))
        self.ilosc_siedzen = int(input("Podaj ilosc siedzen: "))
        self.skrzynia_biegow = input("Podaj czy skrzynia biegow jest automatyczna czy manualna - A lub M: ")
        self.pojemnosc_bagaznika = int(input("Podaj pojemnosc bagaznika: "))
        self.rodzaj = input("Podaj rodzaj samochodu: ")
        self.adnotacja_naprawa = ""
        self.czy_dostepne_do_wypozyczenia = 1
        self.oplata_dzienna = int(input("Podaj oplate dzienna za wypozyczenie samochodu: "))
        data_podaj = input("Podaj date badania technicznego w formacie YYYY-MM-DD: ")
        try:
            self.data_badania_technicznego = datetime.strptime(data_podaj, "%Y-%m-%d")
        except ValueError:
            print("Błąd! Nieprawidłowy format daty.")


    def podaj_info_do_dok_wypozyczenia(self):
        print("Informacje o samochodzie: ")
        print("Marka: ", self.marka)
        print("Rodzaj samochodu: ", self.rodzaj)
        print("Rocznik produkcji: ", self.rocznik)
        print("Oplata dzienna: ", self.oplata_dzienna)

    def podaje_cale_info_samochod(self):
        print("SAMOCHOD")
        print("Marka: ", self.marka)
        print("Rodzaj samochodu: ", self.rodzaj)
        print("Rocznik produkcji: ", self.rocznik)
        print("Przebieg: ", self.przbieg)
        print("Ilosc miejsc: ", self.ilosc_siedzen)
        print("Skryznia biegow: ", self.skrzynia_biegow)
        print("Pojemnosc bagaznika: ", self.pojemnosc_bagaznika)
        print("Oplata dzienna: ", self.oplata_dzienna)
        