from WypozyczAuto_class import WypozyczAuto

class BazaWypozyczenia:
    stan_ilosciowy_historii = 0
    
    def __init__(self):
        self.historia_wypozyczen_w_bazie = []

    def dodaj_wypozyczenie_do_bazy(self, wypozyczenie : WypozyczAuto):
        self.historia_wypozyczen_w_bazie.append(wypozyczenie)
        BazaWypozyczenia.stan_ilosciowy_historii += 1

    def znajdz_wypozyczenie_w_bazie(self, log):#
        wynik = []
        for i in self.historia_wypozyczen_w_bazie:
            if i.klient_ktory_wypozyczyl.login == log:
                wynik.append(i)
        if not wynik:
            print("Nie znaleziono wypozyczen dla danego klienta!")
            return None
        return wynik
    
    def wypozyczenie_aktualizacja(self, wypozyczenie : WypozyczAuto):
        for i in self.historia_wypozyczen_w_bazie:
            if i.id_wypozyczenia == wypozyczenie.id_wypozyczenia:
                i = wypozyczenie
                print("Informacje o wypozyczeniu zostaly zaktualizowane. ")
                break

    def wybierz_wypozyczenia(self, lista_wypozyczen):#
        print("Wybierz wypożyczenie, na którym chcesz podjąć operację: ")
        iterator = 0

        for i in lista_wypozyczen:
            print("Wypożyczenie nr: ", iterator + 1)
            i.pokaz_informacje_wypozyczenie()
            iterator += 1

        try:
            wybor_nr = int(input("\n\nPodaj numer wypożyczenia: "))
            wybor_nr = wybor_nr - 1

            if 0 <= wybor_nr < len(lista_wypozyczen):
                return lista_wypozyczen[wybor_nr]
            else:
                raise IndexError("Podano numer spoza zakresu dostępnych wypożyczeń.")
        except ValueError:
            print("Blad! Podano nieprawidlowa wartosc. Wprowadz numer wypozyczenia jako liczbe calkowita.")
            return None
        except IndexError as a:
            print(f"Blad! {a}")
            return None
