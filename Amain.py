from Samochod_class import Samochod
from KupnoAuta_class import KupnoAuta
from Klient_class import Klient
from OperacjeAuto_class import OperacjeAuto
from BazaAut_class import BazaAut
from BazaKlientow_class import BazaKlientow
from BazaReklmacji_class import BazaReklamacji
from BazaWypozyczenia_class import BazaWypozyczenia

def main():
    wybor = 0
    baza_aut = BazaAut()
    baza_klientow = BazaKlientow()
    baza_reklamacji = BazaReklamacji()
    baza_wypozyczen = BazaWypozyczenia()
    while wybor != -1:
        
        print("MENY PROGRAMU")
        #print("BAZA AUT")
        print("1. Kupno samochodu - dodaj samochod do bazy")
        print("2. Wyswietl samochody znajdujace sie w bazie")
        print("3. Dodaj klienta do bazy klientow")
        print("4. Wykonaj badanie techniczne samochodu")

        wybor = int(input())
        if wybor == 1:
            zakup = KupnoAuta
            samochod = Samochod
            samochod.stworz_auto_input(samochod)
            zakup.kupno(zakup, samochod, baza_aut)
        elif wybor == 2:
            baza_aut.wyswietl_baze_aut()
        elif wybor == 3:
            klient = Klient
            klient.dodaj_klienta_input(klient)
            baza_klientow.dodaj_klienta_do_bazy(klient)
        elif wybor == 4:
            operacja_badanie = OperacjeAuto
            operacja_badanie.badanie_techniczne()
    



main()