import pygame
import random


# ---------------------------------------------------------------------------------------------------------
# zmienne
kolory = {
    "red": (255, 0, 0), "orange": (255, 125, 0), "yellow": (255, 255, 0),
    "green": (0, 255, 0), "cyan": (0, 255, 255), "blue": (0, 0, 255),
    "violet": (125, 0, 255), "magenta": (255, 0, 255), "white": (255, 255, 255),
    "black": (0, 0, 0)
}

WARUNKI_WYGRANEJ = [(1, 2, 3, 4, 5, 6, 7, 8, 9), (1, 4, 7, 2, 5, 8, 3, 6, 9),
                    (3, 2, 1, 6, 5, 4, 9, 8, 7), (3, 6, 9, 2, 5, 8, 1, 4, 7),
                    (7, 4, 1, 8, 5, 2, 9, 6, 3), (7, 8, 9, 4, 5, 6, 1, 2, 3),
                    (9, 8, 7, 6, 5, 4, 3, 2, 1), (9, 6, 3, 8, 5, 2, 7, 4, 1)]

lista_kolorow = ["red", "orange", "yellow", "green", "cyan", "blue", "violet", "magenta", "white"]
random.shuffle(lista_kolorow)

relacje = [[1, 2], [2, 3], [4, 5], [5, 6], [7, 8], [8, 9], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 9]]


# ---------------------------------------------------------------------------------------------------------

# tworzenie losowego ciągu startowego
def create_set():
    y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(y)
    return y


# rysowanie "szachownicy"
def draw_playground(okno_gry):
    for x in range(1, 4):
        for y in range(0, 3):
            pygame.draw.rect(okno_gry, (255, 255, 255), ((y * 75, x * 75), (75, 75)), 1)

    for x in range(1, 4):
        for y in range(4, 7):
            pygame.draw.rect(okno_gry, (255, 255, 255), ((y * 75, x * 75), (75, 75)), 1)


# rysowanie fasolek
def draw_fasolki(okno_gry, pole_gry):
    for i in range(1, 4):
        for j in range(0, 7):
            x = j * 75 + 75 / 2
            y = i * 75 + 75 / 2
            pole = i * 7 + j - 7
            if pole_gry[pole] == 1:
                pygame.draw.circle(okno_gry, kolory[lista_kolorow[0]], (x, y), 15)
            elif pole_gry[pole] == 2:
                pygame.draw.circle(okno_gry, kolory[lista_kolorow[1]], (x, y), 15)
            elif pole_gry[pole] == 3:
                pygame.draw.circle(okno_gry, kolory[lista_kolorow[2]], (x, y), 15)
            elif pole_gry[pole] == 4:
                pygame.draw.circle(okno_gry, kolory[lista_kolorow[3]], (x, y), 15)
            elif pole_gry[pole] == 5:
                pygame.draw.circle(okno_gry, kolory[lista_kolorow[4]], (x, y), 15)
            elif pole_gry[pole] == 6:
                pygame.draw.circle(okno_gry, kolory[lista_kolorow[5]], (x, y), 15)
            elif pole_gry[pole] == 7:
                pygame.draw.circle(okno_gry, kolory[lista_kolorow[6]], (x, y), 15)
            elif pole_gry[pole] == 8:
                pygame.draw.circle(okno_gry, kolory[lista_kolorow[7]], (x, y), 15)
            elif pole_gry[pole] == 9:
                pygame.draw.circle(okno_gry, kolory[lista_kolorow[8]], (x, y), 15)


# sprawdzanie czy gra została wygrana
def check_winning_conditions(pole_gry):
    rezultat = (pole_gry[0], pole_gry[1], pole_gry[2],
                pole_gry[7], pole_gry[8], pole_gry[9],
                pole_gry[14], pole_gry[15], pole_gry[16])
    if rezultat in WARUNKI_WYGRANEJ:
        return True
    else:
        return False


# sprawdza pozycję kursora na ekranie
def check_position(pole):
    if pole in [7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 25, 26, 27]:
        return True
    else:
        return False


# rysowanie wskaźnika pomocniczego
def draw_one_indicators(okno_gry, pole_gry, pole0, pole1=-1, pole2=-1, pole3=-1,
                        pole4=-1):
    poprawny = True
    if pole_gry[pole0] > 0 and pole_gry[pole1] > 0 and pole1 >= 0:
        if [pole_gry[pole0], pole_gry[pole1]] in relacje or [pole_gry[pole1], pole_gry[pole0]] in relacje:
            poprawny = poprawny
        else:
            poprawny = False

    if pole_gry[pole0] > 0 and pole_gry[pole2] > 0 and pole2 >= 0:
        if [pole_gry[pole0], pole_gry[pole2]] in relacje or [pole_gry[pole2], pole_gry[pole0]] in relacje:
            poprawny = poprawny
        else:
            poprawny = False

    if pole_gry[pole0] > 0 and pole_gry[pole3] > 0 and pole3 >= 0:
        if [pole_gry[pole0], pole_gry[pole3]] in relacje or [pole_gry[pole3], pole_gry[pole0]] in relacje:
            poprawny = poprawny
        else:
            poprawny = False

    if pole_gry[pole0] > 0 and pole_gry[pole4] > 0 and pole4 >= 0:
        if [pole_gry[pole0], pole_gry[pole4]] in relacje or [pole_gry[pole4], pole_gry[pole0]] in relacje:
            poprawny = poprawny
        else:
            poprawny = False

    if poprawny and pole_gry[pole0] > 0:
        for i in range(1, 4):
            for j in range(0, 7):
                x = j * 75 + 75 / 2 + 30
                y = i * 75 + 75 / 2 - 30
                if pole0 == i * 7 + j - 7:
                    pygame.draw.circle(okno_gry, kolory["green"], (x, y), 5)
    elif not poprawny and pole_gry[pole0] > 0:
        for i in range(1, 4):
            for j in range(0, 7):
                x = j * 75 + 75 / 2 + 30
                y = i * 75 + 75 / 2 - 30
                if pole0 == i * 7 + j - 7:
                    pygame.draw.circle(okno_gry, kolory["red"], (x, y), 5)


# rysowanie wszystkich wskaźników pomocniczych
def draw_indicators(okno_gry, pole_gry):
    draw_one_indicators(okno_gry, pole_gry, 0, 1, 7)
    draw_one_indicators(okno_gry, pole_gry, 1, 2, 0, 8)
    draw_one_indicators(okno_gry, pole_gry, 7, 0, 8, 14)
    draw_one_indicators(okno_gry, pole_gry, 8, 9, 7, 1, 15)
    draw_one_indicators(okno_gry, pole_gry, 9, 16, 2, 8)
    draw_one_indicators(okno_gry, pole_gry, 14, 15, 7)
    draw_one_indicators(okno_gry, pole_gry, 15, 14, 8, 16)
    draw_one_indicators(okno_gry, pole_gry, 16, 9, 15)
    draw_one_indicators(okno_gry, pole_gry, 2, 9, 1)


# wyświetlanie napisów podczas gry
def draw_moves(ruchy, okno_gry, styl_czcionki):
    wiadomosc = styl_czcionki.render("Ilość ruchów: {}".format(ruchy), True, (0, 0, 0))
    wiadomosc2 = styl_czcionki.render("R - Naciśni by zacząć od początku", True, (0, 0, 0))
    okno_gry.blit(wiadomosc, [10, 10])
    okno_gry.blit(wiadomosc2, [10, 330])


# wyświetlanie napisów końcowych
def draw_score(ruchy, okno_gry, styl_czcionki):
    wiadomosc1 = styl_czcionki.render("Gratulacje!!!", True, (0, 0, 0))
    wiadomosc2 = styl_czcionki.render("Twój wynik to: {}".format(ruchy), True, (0, 0, 0))
    wiadomosc3 = styl_czcionki.render("ESC - Wyjście bez zapisywania wyniku", True, (0, 0, 0))
    wiadomosc4 = styl_czcionki.render("ENTER - Zapisz wynik", True, (0, 0, 0))

    okno_gry.blit(wiadomosc1, [210, 50])
    okno_gry.blit(wiadomosc2, [195, 100])
    okno_gry.blit(wiadomosc3, [100, 250])
    okno_gry.blit(wiadomosc4, [175, 275])


# wyświetlanie nicku na ekranie
def draw_nick(okno_gry, styl_czcionki, nick):
    dlugosc = len(nick)
    for i in range(0, 5 - dlugosc):
        nick = nick + "_"
    wiadomosc = styl_czcionki.render(
        "Podaj swój nick: {} {} {} {} {} ".format(nick[0], nick[1], nick[2], nick[3], nick[4]), True, (0, 0, 0))
    okno_gry.blit(wiadomosc, [150, 150])


# usuwanie znaku z nicku
def delet_character(nick):
    lista = list(nick)
    lista[len(lista) - 1] = ""
    napis = ""
    for litera in lista:
        napis += litera

    return napis


# wyświetlanie menu gry
def draw_menu(okno_gry, styl_czcionki):
    pygame.draw.rect(okno_gry, kolory["white"], ((62.5 / 2, 107.5 / 2 + 10), (200, 80)), 3)
    pygame.draw.rect(okno_gry, kolory["white"], ((62.5 / 2 + 262.5, 107.5 / 2 + 10), (200, 80)), 3)
    pygame.draw.rect(okno_gry, kolory["white"], ((62.5 / 2, 107.5 / 2 + 177.5), (200, 80)), 3)
    pygame.draw.rect(okno_gry, kolory["white"], ((62.5 / 2 + 262.5, 107.5 / 2 + 177.5), (200, 80)), 3)

    wiadomosc1 = styl_czcionki.render("START", True, kolory["red"])
    wiadomosc2 = styl_czcionki.render("WYNIKI", True, kolory["black"])
    wiadomosc3 = styl_czcionki.render("INSTRUKCJA", True, kolory["black"])
    wiadomosc4 = styl_czcionki.render("WYJŚCIE", True, kolory["black"])

    okno_gry.blit(wiadomosc1, (62.5 / 2 + 45, 107.5 / 2 + 10 + 17.5))
    okno_gry.blit(wiadomosc2, (62.5 / 2 + 35 + 262.5, 107.5 / 2 + 30))
    okno_gry.blit(wiadomosc3, (62.5 / 2, 107.5 / 2 + 10 + 10 + 177.5))
    okno_gry.blit(wiadomosc4, (62.5 / 2 + 25 + 262.5, 107.5 / 2 + 10 + 10 + 177.5))


# wyświetlanie strzałki do cofania
def draw_arrow(okno_gry):
    styl_czcionki = pygame.font.SysFont("comicsansms", 50)
    obrazek = styl_czcionki.render("<-", True, kolory["black"])
    okno_gry.blit(obrazek, (450, 300))
    pygame.draw.rect(okno_gry, kolory["white"], ((435, 315), (75, 50)), 3)


# twożelinie listy z wynikami
def create_score_table():
    lista = []
    tabela = [[], []]
    plik = open("../data/top_scores.txt", "r")
    for linia in plik:
        lista.append(linia)
    plik.close()

    for wynik in lista:
        a = 0
        liczba = ""
        napis = ""
        while wynik[a] != ";":
            a += 1
        for i in range(0, a):
            liczba += str(wynik[i])
        tabela[0].append(liczba)
        a += 1
        while wynik[a] != "\n":
            napis += wynik[a]
            a += 1
        tabela[1].append(napis)

    return tabela


# sortowanie bombelkowe wyników
def bubble_sort():
    tabela = create_score_table()
    for i in range(len(tabela[0]) - 1, 0, -1):
        for j in range(i):
            if int(tabela[0][j]) > int(tabela[0][j + 1]):
                tabela[0][j], tabela[0][j + 1] = tabela[0][j + 1], tabela[0][j]
                tabela[1][j], tabela[1][j + 1] = tabela[1][j + 1], tabela[1][j]
    return tabela


# wyświetlanie wyników gry
def draw_wyniki(okno_gry, styl_czcionki, tabela_wynikow, czas):
    ruchy = 0

    for liczba in tabela_wynikow[0]:
        ruchy += int(liczba)
    rozegane_gry = len(tabela_wynikow[0])
    s = czas % 60
    m = czas // 60 % 60
    h = czas // 60 // 60

    wiadomosc1 = styl_czcionki.render("Łączna ilość ruchów: {}".format(ruchy), True, kolory["black"])
    wiadomosc2 = styl_czcionki.render("Ilość rozegranych gier: {}".format(rozegane_gry), True, kolory["black"])
    wiadomosc3 = styl_czcionki.render("Czas spędzony w grze: {}:{}:{}".format(h, m, s), True, kolory["black"])

    okno_gry.blit(wiadomosc1, [10, 100])
    okno_gry.blit(wiadomosc2, [10, 150])
    okno_gry.blit(wiadomosc3, [10, 200])

    wiadomosc1 = styl_czcionki.render("Tabela wyników: ", True, kolory["cyan"])
    okno_gry.blit(wiadomosc1, [300, 25])

    for i in range(0, 5):
        wiadomosc1 = styl_czcionki.render("{}. {} : {}".format(i + 1, tabela_wynikow[0][i], tabela_wynikow[1][i]), True,
                                          kolory["black"])
        okno_gry.blit(wiadomosc1, [325, 75 + 50 * i])


# wyświetlanie instrukcji
def draw_instruction(okno_gry, styl_czcionki, czas):
    def kwadrat():
        for a in range(1, 4):
            for b in range(2, 5):
                pygame.draw.rect(okno_gry, kolory["white"], ((b * 75, a * 75), (75, 75)), 1)

    czas = int(czas)

    if czas % 30 < 5:
        for i in range(1, 2):
            for j in range(2, 4):
                x = j * 75 + 75 / 2
                y = i * 75 + 75 / 2

                pygame.draw.circle(okno_gry, kolory[lista_kolorow[2]], (x, y), 15)
                pygame.draw.circle(okno_gry, kolory["green"], (x+30, y-30), 5)
                if j == 3:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[3]], (x, y), 15)
        kwadrat()

    elif czas % 30 < 10:
        for i in range(1, 2):
            for j in range(2, 5):
                x = j * 75 + 75 / 2
                y = i * 75 + 75 / 2

                if j == 2:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[2]], (x, y), 15)
                    pygame.draw.circle(okno_gry, kolory["green"], (x + 30, y - 30), 5)
                if j == 4:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[4]], (x, y), 15)
                    pygame.draw.circle(okno_gry, kolory["red"], (x + 30, y - 30), 5)
                if j == 3:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[3]], (x, y), 15)
                    pygame.draw.circle(okno_gry, kolory["red"], (x + 30, y - 30), 5)
        kwadrat()

    elif czas % 30 < 15:
        for i in range(1, 3):
            for j in range(2, 4):
                x = j * 75 + 75 / 2
                y = i * 75 + 75 / 2

                if j == 2 and i == 1:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[2]], (x, y), 15)
                    pygame.draw.circle(okno_gry, kolory["green"], (x + 30, y - 30), 5)
                if j == 3 and i == 1:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[3]], (x, y), 15)
                    pygame.draw.circle(okno_gry, kolory["green"], (x + 30, y - 30), 5)
                if j == 2 and i == 2:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[4]], (x, y), 15)
                    pygame.draw.circle(okno_gry, kolory["green"], (x + 30, y - 30), 5)
        kwadrat()

    elif czas % 30 < 20:

        for i in range(1, 4):
            for j in range(2, 5):
                x = j * 75 + 75 / 2
                y = i * 75 + 75 / 2

                if j == 2 and i == 1:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[2]], (x, y), 15)
                    pygame.draw.circle(okno_gry, kolory["green"], (x + 30, y - 30), 5)
                if j == 3 and i == 1:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[3]], (x, y), 15)
                    pygame.draw.circle(okno_gry, kolory["green"], (x + 30, y - 30), 5)
                if j == 3 and i == 2:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[4]], (x, y), 15)
                    pygame.draw.circle(okno_gry, kolory["red"], (x + 30, y - 30), 5)
                if j == 3 and i == 3:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[5]], (x, y), 15)
                    pygame.draw.circle(okno_gry, kolory["red"], (x + 30, y - 30), 5)
                if j == 4 and i == 3:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[6]], (x, y), 15)
                    pygame.draw.circle(okno_gry, kolory["green"], (x + 30, y - 30), 5)
        kwadrat()

    elif czas % 30 < 25:
        for i in range(1, 4):
            for j in range(2, 5):
                x = j * 75 + 75 / 2
                y = i * 75 + 75 / 2

                if j == 2 and i == 1:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[2]], (x, y), 15)
                if j == 3 and i == 1:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[1]], (x, y), 15)
                if j == 4 and i == 1:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[0]], (x, y), 15)
                if j == 2 and i == 2:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[3]], (x, y), 15)
                if j == 3 and i == 2:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[4]], (x, y), 15)
                if j == 4 and i == 2:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[7]], (x, y), 15)
                if j == 2 and i == 3:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[8]], (x, y), 15)
                if j == 3 and i == 3:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[5]], (x, y), 15)
                if j == 4 and i == 3:
                    pygame.draw.circle(okno_gry, kolory[lista_kolorow[6]], (x, y), 15)

                pygame.draw.circle(okno_gry, kolory["green"], (x + 30, y - 30), 5)
        kwadrat()

    elif czas % 30 < 30:
        wiadomosc1 = styl_czcionki.render("! WIN !", True, kolory["red"])

        okno_gry.blit(wiadomosc1, [165, 150])
