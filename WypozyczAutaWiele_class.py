from Klient_class import Klient
from WypozyczAuto_class import WypozyczAuto
from BazaAut_class import BazaAut
from BazaWypozyczenia_class import BazaWypozyczenia

class WypozyczAutaWiele:
    def __init__(self):
        None
    
    def wypozycz_wiele_samochodow(klient : Klient, baza_aut : BazaAut, rejestr_wypozyczen : BazaWypozyczenia):
        ilosc_samochodow = int(input("Podaj ilosc samochodow, ktore chcesz wypozyczyc: "))
        dostepne_samochody = 0
        for i in baza_aut.samochody_w_bazie:
            if i.czy_dostepne_do_wypozyczenia == 1:
                dostepne_samochody += 1

        if ilosc_samochodow > dostepne_samochody:
            print("Podana ilosc samochodow jest wieksza niz ilosc samochodow dostepnych do wypozcyzenia.")
            print("Dostepna ilosc to: ", dostepne_samochody)
            ilosc_samochodow = int(input("Podaj liczbe samochodow do wypozyczenia lub wpisz 0 jesli chcesz anulowac operację: "))
            if ilosc_samochodow <= 0 or ilosc_samochodow > dostepne_samochody:
                return None
            
        print("Wybierz samochody, ktore chcesz wypozyczyc: ")
        baza_aut.wyswietl_baze_aut()
        print("Podaj kojeno numery samochdow do wypozyczenia: ")
        iter = 0
        lista_samochodow = []
        while iter < ilosc_samochodow:
            wybrany_numer_samochodu = int(input())
            lista_samochodow.append(baza_aut.samochody_w_bazie[wybrany_numer_samochodu])
            iter += 1
        
        for i in lista_samochodow:
            wypozyczenie = WypozyczAuto()
            wypozyczenie.wypozycz(klient, i, rejestr_wypozyczen)
            rejestr_wypozyczen.dodaj_wypozyczenie_do_bazy(wypozyczenie)

    

