class Samochod:
    def __init__(self, marka, rocz, przeb, st, ils, skrz, pojemn, rodz, data, adn, czyd, opltd):
        self.rocznik = rocz
        self.marka =marka
        self.przbieg = przeb
        self.stan = st
        self.ilosc_siedzen = ils
        self.skrzynia_biegow = skrz
        self.pojemnosc_bagaznika = pojemn
        self.rodzaj = rodz
        self.data_badania_technicznego = data
        self.adnotacja_naprawa = adn
        self.czy_dostepne_do_wypozyczenia = czyd
        self.oplata_dzienna = opltd

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
        