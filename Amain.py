from Samochod_class import Samochod
from KupnoAuta_class import KupnoAuta
from WypozyczAuto_class import WypozyczAuto
from Klient_class import Klient
from OperacjeAuto_class import OperacjeAuto
from ZlozReklamacje_class import ZlozReklamacje
from ZwrocAuto_class import ZwrocAuto
from BazaAut_class import BazaAut
from BazaKlientow_class import BazaKlientow
from BazaReklmacji_class import BazaReklamacji
from BazaWypozyczenia_class import BazaWypozyczenia
from MetodyPlatnosci_class import MetodyPlatnosci

def main():
    wybor = 0
    baza_aut = BazaAut()
    baza_klientow = BazaKlientow()
    baza_reklamacji = BazaReklamacji()
    baza_wypozyczen = BazaWypozyczenia()
    
    while wybor != -1:
        print("MENU PROGRAMU")
        print("1. Kupno samochodu - dodaj samochod do bazy")
        print("2. Wyswietl samochody znajdujace sie w bazie")
        print("3. Dodaj klienta do bazy klientow")
        print("4. Wyswietl klientow znajdujacych sie w bazie")
        print("5. Wykonaj badanie techniczne samochodu")
        print("6. Dokonaj naprawy samochodu.")
        print("7. Dokonaj kasacji samochodu - usun samochod z bazy")
        print("8. Sprawdz termin badania technicznego")
        print("9. Wypozycz samochod")
        print("10. Oddanie auta i zapłata")
        print("11. Zloz reklamacje dotyczaca wypozyczenia")

        print("-1. Wyjdz z programu")

        wybor = int(input())
        if wybor == 1:
            zakup = KupnoAuta()
            samochod = Samochod(None, None, None, None, None, None, None, None, None, None, None, None)
            samochod.stworz_auto_input()
            zakup.kupno(samochod, baza_aut)
        elif wybor == 2:
            baza_aut.wyswietl_baze_aut()
        elif wybor == 3:
            klient = Klient(None, None, None, None, None, None)
            klient.dodaj_klienta_input()
            baza_klientow.dodaj_klienta_do_bazy(klient)
        elif wybor == 4:
            baza_klientow.wyswietl_baze_klientow()
        elif wybor == 5:
            operacja_badanie = OperacjeAuto()
            operacja_badanie.badanie_techniczne(baza_aut.wybierz_auto(), baza_aut)
        elif wybor == 6:
            operacja_naprawa = OperacjeAuto()
            operacja_naprawa.naprawa_auta(baza_aut.wybierz_auto(), baza_aut)
        elif wybor == 7:
            operacja_kasacja = OperacjeAuto()
            operacja_kasacja.kasacja(baza_aut.wybierz_auto(), baza_aut)
        elif wybor == 8:
            operacja_sprawdz_termin_badania = OperacjeAuto()
            operacja_sprawdz_termin_badania.sprawdz_termin_badania_technicznego(baza_aut.wybierz_auto())
        elif wybor == 9:
            wypozyczenie = WypozyczAuto()
            klient = Klient(None, None, None, None, None, None)
            log = input("Podaj login dla ktorego chcesz dokonac wypozyczenia: ")
            klient = baza_klientow.znajdz_klienta_w_bazie(log)
            samochod = Samochod(None, None, None, None, None, None, None, None, None, None, None, None)
            samochod = baza_aut.wybierz_auto()
            wypozyczenie.wypozycz(klient, samochod, baza_wypozyczen)
            baza_wypozyczen.dodaj_wypozyczenie_do_bazy(wypozyczenie)
        elif wybor==10:
            log = input("Podaj login dla ktorego chcesz zwrocic auto: ")
            klient = Klient(None, None, None, None, None, None)
            klient = baza_klientow.znajdz_klienta_w_bazie(log)
            wypozyczenie = WypozyczAuto()
            wypozyczenie = baza_wypozyczen.znajdz_wypozyczenie_w_bazie(klient.log)
            wypozyczenie = baza_wypozyczen.wybierz_wypozyczenia(wypozyczenie)
            zwrot_auta = ZwrocAuto() 
            zwrot_auta.zwroc_auto(wypozyczenie.wypozyczony_samochod, klient, wypozyczenie, baza_wypozyczen)
        elif wybor == 11:
            zloz_reklmacje = ZlozReklamacje()
            zloz_reklmacje.uzuplenij_info(baza_klientow, baza_wypozyczen, baza_reklamacji)


        elif wybor == -1:
            break
            


main()
