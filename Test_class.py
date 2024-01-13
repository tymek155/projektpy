import unittest
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import MagicMock
from BazaAut_class import BazaAut
from BazaKlientow_class import BazaKlientow
from BazaWypozyczenia_class import BazaWypozyczenia
from WypozyczAuto_class import WypozyczAuto
from Klient_class import Klient
from OperacjeAuto_class import OperacjeAuto
from Samochod_class import Samochod
from Zaplata_class import Zaplata

class TestBazaAut(unittest.TestCase):
    def test_usun_samochod(self):
        baza_aut = BazaAut()
        samochod1 = Samochod("marka1", 2000, 1000, 1, 5, "A", 1200, "rodzaj1", "2024-12-10", "Brak", 1, 200)
        samochod2 = Samochod("marka2", 2005, 2000, 1, 4, "A", 1400, "rodzaj2", "2024-12-20", "Brak", 1, 220)

        baza_aut.dodaj(samochod1)
        baza_aut.dodaj(samochod2)

        self.assertEqual(BazaAut.ilosc_aut_w_bazie, 2)

        baza_aut.usun_samochod(samochod1)

        self.assertEqual(BazaAut.ilosc_aut_w_bazie, 1)
        self.assertNotIn(samochod1, baza_aut.samochody_w_bazie)
        self.assertIn(samochod2, baza_aut.samochody_w_bazie)

class TestBazaKlientow(unittest.TestCase):
    def test_znajdz_klienta_w_bazie(self):
        klient1 = Mock(imie = "imie 1", nazwisko = "Nazwisko1", pesel = 00000000, plec = "M", login = "login1", status_stalego_klienta = 1)
        klient2 = Mock(imie = "imie 2", nazwisko = "Nazwisko2", pesel = 00000000, plec = "K", login = "login2", status_stalego_klienta = 1)
        klient3 = Mock(imie = "imie 3", nazwisko = "Nazwisko3", pesel = 00000000, plec = "M", login = "login3", status_stalego_klienta = 1)

        baza_klientow = BazaKlientow()
        baza_klientow.dodaj_klienta_do_bazy(klient1)
        baza_klientow.dodaj_klienta_do_bazy(klient2)
        baza_klientow.dodaj_klienta_do_bazy(klient3)

        znaleziony_klient = baza_klientow.znajdz_klienta_w_bazie("login2")
        none_klient = baza_klientow.znajdz_klienta_w_bazie("none login")
        self.assertEqual(znaleziony_klient,klient2)
        self.assertIsNone(none_klient)

class TestBazaWypozyczen(unittest.TestCase):
    def test_znajdz_wypozyczenie_w_bazie(self):
        baza_wypozyczen = BazaWypozyczenia()
        login1 = "login1"
        login2 = "login2"

        klient1 = Klient("imie1", "nazwisko2", 0000000, "m", login1, 0)
        klient2 = Klient("imie1", "nazwisko2", 0000000, "m", login2, 0)

        samochod1 = Samochod("marka1", 2000, 1000, 1, 5, "A", 1200, "rodzaj1", "2024-12-10", "Brak", 1, 200)
        samochod2 = Samochod("marka2", 2005, 2000, 1, 4, "A", 1400, "rodzaj2", "2024-12-20", "Brak", 1, 220)

        wypozyczenie1 = WypozyczAuto()
        wypozyczenie2 = WypozyczAuto()

        wypozyczenie1.wypozycz(klient1, samochod1, baza_wypozyczen)
        baza_wypozyczen.dodaj_wypozyczenie_do_bazy(wypozyczenie1)
        wypozyczenie2.wypozycz(klient2, samochod2, baza_wypozyczen)
        baza_wypozyczen.dodaj_wypozyczenie_do_bazy(wypozyczenie2)

        wynik1 = baza_wypozyczen.znajdz_wypozyczenie_w_bazie(login1)
        wynik2 = baza_wypozyczen.znajdz_wypozyczenie_w_bazie(login2)

        self.assertIsNotNone(wynik1)
        self.assertEqual(len(wynik1), 1)
        self.assertEqual(wynik1[0], wypozyczenie1)

        self.assertIsNotNone(wynik2)
        self.assertEqual(len(wynik2), 1)
        self.assertEqual(wynik2[0], wypozyczenie2)

class TestBazaKlientow(unittest.TestCase):
    def test_znajdz_klienta_w_bazie_none(self):
        login_klienta = "test_login"
        baza_wypozyczen = BazaWypozyczenia()

        wynik_none = baza_wypozyczen.znajdz_wypozyczenie_w_bazie(login_klienta)

        self.assertIsNone(wynik_none)
        
class TestKlient(unittest.TestCase):
    @patch('builtins.input', side_effect=["Jan", "Kowalski", "00000000000", "M", "login"])
    def test_dodaj_klienta_input(self, mock_input):
        klient = Klient(None, None, None, None, None, None)

        klient.dodaj_klienta_input()

        self.assertEqual(klient.imie, "Jan")
        self.assertEqual(klient.nazwisko, "Kowalski")
        self.assertEqual(klient.pesel,00000000000)
        self.assertEqual(klient.plec, "M")
        self.assertEqual(klient.login, "login")

    @patch('builtins.input', side_effect=["Jan", "Kowalski", "tekst_zamiast_pesel", "M", "login"])
    def test_dodaj_klienta_input_none(self, mock_input):
        klient = Klient(None, None, None, None, None, None)

        klient.dodaj_klienta_input()

        self.assertIsNone(klient.pesel)

class MockMetodyPlatnosci:
        def __init__(self, kwota, metoda_platnosci):
            self.kwota = kwota
            self.metoda_platnosci = metoda_platnosci
            self.zaplac = MagicMock()

class TestZaplata(unittest.TestCase):

    def test_obnizka_dla_stalego_klienta(self):
        samochod = Samochod("marka1", 2000, 1000, 1, 5, "A", 1200, "rodzaj1", "2024-12-10", "Brak", 1, 200)
        klient = Klient("Jan", "Kowalski", "00000000000", "M", "login",11)
        baza_wypozyczen = BazaWypozyczenia()
        wypozyczenie = WypozyczAuto()
        wypozyczenie.wypozycz(klient, samochod, baza_wypozyczen)
        baza_wypozyczen.dodaj_wypozyczenie_do_bazy(wypozyczenie)

        ilosc_dni = 5
        zaplata = Zaplata(samochod, klient, baza_wypozyczen, ilosc_dni)
        self.assertEqual(zaplata.kwota*0.9, samochod.oplata_dzienna * ilosc_dni * 0.9)

    def test_wybor_metody_platnosci(self):
        samochod = Samochod("marka1", 2000, 1000, 1, 5, "A", 1200, "rodzaj1", "2024-12-10", "Brak", 1, 200)
        klient = Klient("Jan", "Kowalski", "00000000000", "M", "login",11)
        baza_wypozyczen = BazaWypozyczenia()
        wypozyczenie = WypozyczAuto()
        wypozyczenie.wypozycz(klient, samochod, baza_wypozyczen)
        baza_wypozyczen.dodaj_wypozyczenie_do_bazy(wypozyczenie)

        ilosc_dni = 3
        zaplata = Zaplata(samochod, klient, baza_wypozyczen, ilosc_dni)
        zaplata.wybierz_metode_platnosci(samochod)
        self.assertIn(zaplata.metoda_platnosci, ["Gotowka", "Karta Platnicza", "BLIK", "Przelew"])

    def test_rekurencyjny_wybor_metody_platnosci(self):
        samochod = Samochod("marka1", 2000, 1000, 1, 5, "A", 1200, "rodzaj1", "2024-12-10", "Brak", 1, 200)
        klient = Klient("Jan", "Kowalski", "00000000000", "M", "login",10)
        baza_wypozyczen = BazaWypozyczenia()
        wypozyczenie = WypozyczAuto()
        wypozyczenie.wypozycz(klient, samochod, baza_wypozyczen)
        baza_wypozyczen.dodaj_wypozyczenie_do_bazy(wypozyczenie)

        ilosc_dni = 2
        zaplata = Zaplata(samochod, klient, baza_wypozyczen, ilosc_dni)
        zaplata.wybierz_metode_platnosci(samochod)
        self.assertIn(zaplata.metoda_platnosci, ["Gotowka", "Karta Platnicza", "BLIK", "Przelew"])

    def test_zaplac(self):
        samochod = Samochod("marka1", 2000, 1000, 1, 5, "A", 1200, "rodzaj1", "2024-12-10", "Brak", 1, 200)
        klient = Klient("Jan", "Kowalski", "00000000000", "M", "login",9)
        baza_wypozyczen = BazaWypozyczenia()
        wypozyczenie = WypozyczAuto()
        wypozyczenie.wypozycz(klient, samochod, baza_wypozyczen)
        baza_wypozyczen.dodaj_wypozyczenie_do_bazy(wypozyczenie)

        ilosc_dni = 4
        zaplata = Zaplata(samochod, klient, baza_wypozyczen, ilosc_dni)
        mock_metoda_platnosci = MockMetodyPlatnosci(zaplata,1)
        mock_metoda_platnosci.zaplac(samochod)
        mock_metoda_platnosci.zaplac.assert_called_with(samochod)
            
    


