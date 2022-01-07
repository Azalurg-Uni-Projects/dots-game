from src import functions as f
import pygame
import timeit


# ---------------------------------------------------------------------------------------------------------


def core_game_loop(okno_gry):  # główna pętla gry

    game_close = False  # zmienne
    game_win = False
    ciag_startowy = f.create_set()
    pole_gry = [0, 0, 0, 'x', ciag_startowy[0], ciag_startowy[1], ciag_startowy[2],
                0, 0, 0, 'x', ciag_startowy[3], ciag_startowy[4], ciag_startowy[5],
                0, 0, 0, 'x', ciag_startowy[6], ciag_startowy[7], ciag_startowy[8]]
    pobrana_wartosc = 0
    czy_pobrana_wartosc = False
    ruchy = 0
    styl_czcionki = pygame.font.SysFont("dejavusans", 25)
    nick = ""
    start = timeit.default_timer()
    kolor_tla = (205, 179, 153)

    while not game_close and not game_win:  # początek pętli

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True

            if event.type == pygame.KEYDOWN:  # reset ustawienia początkowego
                if event.key == 114:
                    ciag_startowy = f.create_set()
                    pole_gry = [0, 0, 0, 'x', ciag_startowy[0], ciag_startowy[1], ciag_startowy[2],
                                0, 0, 0, 'x', ciag_startowy[3], ciag_startowy[4], ciag_startowy[5],
                                0, 0, 0, 'x', ciag_startowy[6], ciag_startowy[7], ciag_startowy[8]]
                    ruchy = 0
                    pobrana_wartosc = 0
                    czy_pobrana_wartosc = False

            if not game_win:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_x, mouse_y = event.pos
                        pole = (((mouse_y // 75) * 7) + (mouse_x // 75))

                        if 435 <= mouse_x <= 510 and 315 <= mouse_y <= 365:  # powrót do menu
                            game_close = True

                        if f.check_position(pole):  # sprawdzenie czy zostało wybrane odpowiednie pole
                            if czy_pobrana_wartosc:  # zamiana wartości
                                pole_gry[pobrana_wartosc], pole_gry[pole - 7] = pole_gry[pole - 7], pole_gry[
                                    pobrana_wartosc]
                                czy_pobrana_wartosc = False
                                pobrana_wartosc = 0
                                ruchy += 1
                            elif not czy_pobrana_wartosc and pole_gry[pole - 7] > 0:  # pobranie wartosci
                                czy_pobrana_wartosc = True
                                pobrana_wartosc = pole - 7
                        if f.check_winning_conditions(pole_gry):
                            game_win = True
                            print("WIN!!!!")

        okno_gry.fill(kolor_tla)            # rysowanie różnych obiektów
        f.draw_playground(okno_gry)
        f.draw_fasolki(okno_gry, pole_gry)
        f.draw_arrow(okno_gry)
        f.draw_indicators(okno_gry, pole_gry)
        f.draw_moves(ruchy, okno_gry, styl_czcionki)
        pygame.display.update()

    if game_win:  # zapisywanie wyniku
        czas = timeit.default_timer() - start
        while not game_close:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_close = True

                if event.type == pygame.KEYDOWN:
                    if 48 <= event.key <= 57 or 65 <= event.key <= 90 or 97 <= event.key <= 122:
                        a = event.key
                        a = chr(a)
                        nick = nick + a
                    elif event.key == 8 and len(nick) > 0:
                        nick = f.delet_character(nick)
                    elif event.key == 13 and len(nick) > 0:
                        plik = open("../data/top_scores.txt", "a")
                        linijka = str(ruchy) + ";" + nick + '\n'
                        plik.write(linijka)
                        game_close = True
                        plik.close()
                        plik = open("../data/time.txt", "r")
                        a = plik.read()
                        plik.close()
                        plik = open("../data/time.txt", "w")
                        plik.write(str(float(a) + czas))
                        plik.close()

                    elif event.key == 27:
                        game_close = True

            pygame.display.update()         # rysowanie różnych obiektów
            okno_gry.fill(kolor_tla)
            f.draw_score(ruchy, okno_gry, styl_czcionki)
            f.draw_nick(okno_gry, styl_czcionki, nick)

# ---------------------------------------------------------------------------------------------------------


def score_loop(okno_gry):       # pętla wyświetlająca winiki gry

    game_close = False          # zmienne
    styl_czcionki = pygame.font.SysFont("dejavusans", 25)
    tabela_wynikow = f.bubble_sort()
    kolor_tla = (205, 179, 153)

    plik = open("../data/time.txt", "r")
    czas = plik.read()
    czas = int(float(czas))
    plik.close()

    while not game_close:  # początek pętli

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if 435 <= mouse_x <= 510 and 315 <= mouse_y <= 365:
                        game_close = True

        okno_gry.fill(kolor_tla)            # rysowanie różnych obiektów
        f.draw_wyniki(okno_gry, styl_czcionki, tabela_wynikow, czas)
        f.draw_arrow(okno_gry)
        pygame.display.update()

# ---------------------------------------------------------------------------------------------------------


def game_instruction(okno_gry):

    game_close = False          # zmienne
    styl_czcionki = pygame.font.SysFont("dejavusans", 80)
    kolor_tla = (205, 179, 153)
    start = timeit.default_timer()

    while not game_close:  # początek pętli

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = event.pos
                    if 435 <= mouse_x <= 510 and 315 <= mouse_y <= 365:
                        game_close = True

        okno_gry.fill(kolor_tla)        # rysowanie różnych obiektów
        f.draw_instruction(okno_gry, styl_czcionki, timeit.default_timer() - start)
        f.draw_arrow(okno_gry)
        pygame.display.update()
