from Samochod_class import Samochod

class BazaAut:
    ilosc_aut_w_bazie = 0
    ilosc_marek = 0

    def __init__(self):
        self.dostepne_marki = set()  
        self.samochody_w_bazie = []

    def marka_in_bd(self, marka):
        return marka in self.dostepne_marki

    def znajdz_obiekt(self, autoa: Samochod):
        for i in self.samochody_w_bazie:
            if i == autoa:
                return i
        else:
            print("Nie ma auta w bazie")

    def dodaj(self, autoa: Samochod):
        self.samochody_w_bazie.append(autoa)
        BazaAut.ilosc_aut_w_bazie += 1  
        if not self.marka_in_bd(autoa.marka):
            self.dostepne_marki.add(autoa.marka)
            BazaAut.ilosc_marek += 1

    def dodaj_marke(self, marka):
        if marka not in self.dostepne_marki:
            self.dostepne_marki.add(marka)
            BazaAut.ilosc_marek += 1

    def usun_samochod(self, samochod : Samochod):
        index = 0
        for i in self.samochody_w_bazie:
            if i == samochod:
                print("Znaleziono samochod do usuniecia!")
                del self.samochody_w_bazie[index]
                BazaAut.ilosc_aut_w_bazie = BazaAut.ilosc_aut_w_bazie - 1
                break
            index = index + 1
        else:
            print("Nie znaleziono samochodu do usuniecia!")

    def wyswietl_baze_aut(self):
        for i in self.samochody_w_bazie:
            i.podaje_cale_info_samochod()
            print("\n")

    

