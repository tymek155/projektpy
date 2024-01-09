from Samochod_class import Samochod
from BazaAut_class import BazaAut
from BazaKlientow_class import BazaKlientow
from BazaReklmacji_class import BazaReklamacji
from BazaWypozyczenia_class import BazaWypozyczenia

def main():
    baza_aut = BazaAut()
    baza_klientow = BazaKlientow()
    baza_reklamacji = BazaReklamacji()
    baza_wypozyczen = BazaWypozyczenia()
    print("MENY PROGRAMU")
    print("BAZA AUT")
    print("1. Dodaj samochod do bazy\n")



    wybor = int(input())
    if wybor == 1:
        samochod = Samochod
        samochod.stworz_auto_input(samochod)
        baza_aut.dodaj(samochod)



main()