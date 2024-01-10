from Samochod_class import Samochod



class MetodyPlatnosci:
    def __init__(self,p,metoda):
        self.prize=p
        self.metoda_platnosci=metoda
    def zaplac(self, samochod : Samochod):
        if self.prize > 0:
            if self.metoda_platnosci=="Gotowka":
                print("Wybrano Płatność gotówką\n")
                from PlatnoscGotowka_class import PlatnoscGotowka
                platnosc=PlatnoscGotowka(self.prize, self.metoda_platnosci)
                platnosc.zaplac_gotowka(samochod)
            else:
                print("Wybrano Płatności bankowe\n-----Przekierowuję na stronę banku------\n")
                from PlatnosciBankowe_class import PlatnosciBankowe
                platnosc=PlatnosciBankowe(self.prize, self.metoda_platnosci)
                platnosc.Bankowosc(samochod)


    