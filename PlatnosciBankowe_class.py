from Samochod_class import Samochod
from MetodyPlatnosci_class import MetodyPlatnosci
import time

class PlatnosciBankowe(MetodyPlatnosci):
    def _init_(self, p, metoda):
        super.__init__(p,metoda)

    def Bankowosc(self, samochod : Samochod):
        if self.metoda_platnosci=="Karta Platnicza":
            print("______Paragon fiskalny______")
            samochod.podaje_cale_info_samochod()
            print("Zapłacono -> "+self.prize)
        elif self.metoda_platnosci=="BLIK":
            print("Wybrano Płatność BLIK-iem     Podaj kod: ")
            int(input())
            print("Zatwierdź transakcje w aplikacji bankowej")
            time.sleep(5)
            print("Dziękujemy za dokonanie transakcji i opłacenie wypożyczenia samochodu:\n")
            samochod.podaje_cale_info_samochod()
        elif self.metoda_platnosci=="Przelew":
            print("Wybrano Tradycyjny Przelew\n Przelej "+self.prize+" na numer konta 0000000000, załączając w opisie dane samochodu\n")
            samochod.podaje_cale_info_samochod()
            time.sleep(5)
            print("Dziękujemy za dokonanie transakcji i opłacenie wypożyczenia\n")
            
