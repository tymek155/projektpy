from Osoba_class import Osoba
from Samochod_class import Samochod
#from BazaWypozyczenia_class import BazaWypozyczenia

class Klient(Osoba):
    def __init__(self, im, nazw, pes, pl, log, status):
        super().__init__(im, nazw, pes, pl)
        self.login = log
        self.status_stalego_klienta = status

    def jakie_auto(autoa : Samochod):
        print("Podaj dane auta: ")
        m = input("Podaj marke: ")
        rok = int(input("Podaj rok: "))
        przeb = int(input("Podaj przebieg: "))
        il_s = int(input("Podaj ilosc siedzen: "))
        rskrz = input("Podaj rodzaj skryzni biegow: ")

        return Samochod(m, rok, przeb, True, il_s, rskrz, 10, "coupe, 0")
    
    def wyswietl_informacje_o_kliencie(self):
        print("Imie: ", self.imie)
        print("Nazwisko: ", self.nazwisko)
        print("PESEL: ", self.pesel)
        print("Plec: ", self.plec)
        print("Login: ", self.login)


  #  def sprawdz_status_stalego_klienta(self, baza_wypozyczen : BazaWypozyczenia):
  #      policz_ile_transakcji = 0
  #      for i in baza_wypozyczen.historia_wypozyczen_w_bazie:
  #          if i.klient_ktory_wypozyczyl.login == self.login:
  #              policz_ile_transakcji += 1

   #     if policz_ile_transakcji >= 10:
  #          print("Klient posiada status stalego klienta - posiada dodatkowa znizke na wypozyczenie")
   #         self.status_stalego_klienta = 1
   #    else:
    #        print("Za malo transakcji do statusu stalego klienta!")
     #       print("Brakujaca ilosc transakcji to: ", 10-policz_ile_transakcji)