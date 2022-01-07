from src import functions as f
import random

'''Wszystkie testy są tak przystosowane aby zwracały wynik pozytywny'''
'''Opisy wszystkich testowanych funkcji znajdują się w pliku functions'''


def test_delet_character():
    nick = "aaab"
    assert f.delet_character(nick) == "aaa"


def test_check_position():
    pole1 = 7
    pole2 = 18
    assert f.check_position(pole1)
    assert f.check_position(pole2)


def test_check_wining_conditions():
    pole_gry = [1, 2, 3, 0, 0, 0, 0,
                4, 5, 6, 0, 0, 0, 0,
                7, 8, 9, 0, 0, 0, 0]
    assert f.check_winning_conditions(pole_gry)


def test_create_set():
    lista = f.create_set()
    lista.sort()
    assert lista == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_bouble_sort():
    tabela1 = f.bubble_sort()
    random.shuffle(tabela1)
    tabela1.sort()

    tabela2 = f.bubble_sort()

    assert tabela2[0] == tabela1[0]
