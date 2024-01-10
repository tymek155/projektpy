from datetime import datetime
from Samochod_class import Samochod
from BazaAut_class import BazaAut

class OperacjeAuto:
    def __init__(self):
        self.czy_naprawa_udana = None
        self.czy_kasacja_wykonana = None

    def kasacja(self, samochod : Samochod, baza_aut : BazaAut):
        if self.czy_kasacja_wykonana == 1:
            print("Usuwam samochod z bazy samochodow")
            baza_aut.usun_samochod(samochod)

    def naprawa_auta(self, samochod : Samochod, baza_aut : BazaAut):
        decyzja_naprawy = int(input("Czy naprawa samochodu jest mozliwa? Podaj 1 jesli TAK, 0 jesli NIE" ))
        while (decyzja_naprawy == 0):
            decyzja_ostateczna = int(input("Czy chcesz usunac auto z bazy i przekazac jes do kasacji? Podaj 1 jesli TAK, 0 jesli NIE "))
            if decyzja_ostateczna == 1:
                print("Auto zostaje przekazane do kasacji i trwale usuniete z bazy")
                self.czy_kasacja_wykonana = 1
                self.kasacja(samochod, baza_aut)
                break
            else:
                print("Powrot do procesu naprawy auta")
                decyzja_naprawy = int(input("Czy naprawa samochodu jest mozliwa? Podaj 1 jesli TAK, 0 jesli NIE"))
        if decyzja_naprawy == 1:
            notatka = input("Opisz naprawe, wymienione czesci oraz koszt naprawy samochodu: ")
            samochod.adnotacja_naprawa = samochod.adnotacja_naprawa + notatka
            self.czy_naprawa_udana = 1
            podaj_date = input("Podaj datę nastepnego badania technicznego w formacie YYYY-MM-DD: ")
            try:
                samochod.data_badania_technicznego = datetime.strptime(podaj_date, "%Y-%m-%d")
                print("Data nastepnego badania technicznego:", samochod.data_badania_technicznego)    
            except ValueError:
                print("Blad! Nieprawidlowy format daty.")

    def badanie_techniczne(self, samochod: Samochod, baza_aut : BazaAut):
        sprawdzam_stan_samochodu = []

        print("PODAJ 1 JESLI DOBRY, PODAJ 0 JESLI ZLY")
        sprawdzam_stan_samochodu.append(int(input("Czy stan oswietelenia jest dobry?  ")))
        sprawdzam_stan_samochodu.append(int(input("Czy stan hamulcow jest dobry?  ")))
        sprawdzam_stan_samochodu.append(int(input("Czy stan zawieszenia jest dobry?  ")))
        sprawdzam_stan_samochodu.append(int(input("Czy stan silnika jest dobry?  ")))
        sprawdzam_stan_samochodu.append(int(input("Czy stan ukladu kierwoniczego jest dobry?  ")))
        sprawdzam_stan_samochodu.append(int(input("Czy stan karoserii jest dobry?  ")))
        sprawdzam_stan_samochodu.append(int(input("Czy stan podwozia jest dobry?  ")))

        for i in sprawdzam_stan_samochodu:
            if i == 0:
                print("Samochod wymaga naprawy, przejscie do procesu naprawy samochodu.")
                self.naprawa_auta(samochod, baza_aut)
                break
        print("Pozytywny wynik badania technicznego!")
        podaj_date = input("Podaj datę nastepnego badania technicznego w formacie YYYY-MM-DD: ")
        try:
            samochod.data_badania_technicznego = datetime.strptime(podaj_date, "%Y-%m-%d")
            print("Data nastepnego badania technicznego: ", samochod.data_badania_technicznego)    
        except ValueError:
            print("Blad! Nieprawidlowy format daty.")

    def sprawdz_termin_badania_technicznego(self, samochod: Samochod):
        print("Termin badania technicznego dla danego auta to: ", samochod.data_badania_technicznego)
        
