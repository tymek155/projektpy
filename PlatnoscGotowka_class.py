from MetodyPlatnosci_class import MetodyPlatnosci
from Samochod_class import Samochod

class PlatnoscGotowka(MetodyPlatnosci):
    def __init__(self, p, metoda):
        super().__init__(p, metoda)


    def zaplac_gotowka(self,samochod : Samochod):
        print("______Paragon fiskalny______")
        samochod.podaje_cale_info_samochod()
        print("Zapłacono -> ", self.prize)