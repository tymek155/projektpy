import unittest
from unittest.mock import Mock
from BazaKlientow_class import BazaKlientow
from Klient_class import Klient

class TestFunkcji(unittest.TestCase):
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

        

