from MetodyPlatnosci_class import MetodyPlatnosci
from Samochod_class import Samochod
class PlatnoscGotowka(MetodyPlatnosci):
    def _init_(self, p):
        super.__init__(p)

    def zaplac_gotowka(self,samochod : Samochod):
        print("______Paragon fiskalny______")
        samochod.podaje_cale_info_samochod()
        print("Zapłacono -> "+self.prize)