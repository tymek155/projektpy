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
        self.sprawdz_none = "Brak"

    def stworz_auto_input(self):
        try:
            self.rocznik = int(input("Podaj rok produkcji samochodu: "))
            self.przebieg = int(input("Podaj przebieg: "))
            self.stan = int(input("Podaj 1 jesli stan jest dobry lub 0 jesli stan samochodu jest zly: "))
            self.ilosc_siedzen = int(input("Podaj ilość siedzen: "))
            self.pojemnosc_bagaznika = int(input("Podaj pojemność bagaznika: "))
            self.oplata_dzienna = int(input("Podaj oplate dzienną za wypozyczenie samochodu: "))
            
            skrzynia_biegow_input = input("Podaj czy skrzynia biegow jest automatyczna czy manualna - A lub M: ")
            if skrzynia_biegow_input.upper() in {'A', 'M'}:
                self.skrzynia_biegow = skrzynia_biegow_input.upper()
            else:
                print("Blad! Wybierz A lub M dla skrzyni biegow.")
                self.sprawdz_none = None
                return None

            data_badania_technicznego_input = input("Podaj date badania technicznego w formacie YYYY-MM-DD: ")
            self.data_badania_technicznego = datetime.strptime(data_badania_technicznego_input, "%Y-%m-%d")

            self.marka = input("Podaj marke: ")
            self.rodzaj = input("Podaj rodzaj samochodu: ")

            self.adnotacja_naprawa = ""
            self.czy_dostepne_do_wypozyczenia = 1

        except ValueError:
            print("Blad! Wprowadzono nieprawidlowa wartosc. Upewnij sie, że podajesz liczby tam, gdzie to wymagane.")
            self.sprawdz_none = None
            return None
        except Exception as e:
            print(f"Wystapil blad: {e}")
            self.sprawdz_none = None
            return None


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
        print("Przebieg: ", self.przebieg)
        print("Ilosc miejsc: ", self.ilosc_siedzen)
        print("Skryznia biegow: ", self.skrzynia_biegow)
        print("Pojemnosc bagaznika: ", self.pojemnosc_bagaznika)
        print("Oplata dzienna: ", self.oplata_dzienna)
        