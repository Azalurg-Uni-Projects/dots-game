import pygame
from src import functions as f, loops

# ---------------------------------------------------------------------------------------------------------

pygame.init()

# ---------------------------------------------------------------------------------------------------------
# ustawienia ekranu

okno_gry = pygame.display.set_mode((525, 375))
pygame.display.set_caption("ZAGADKOWE FASOLKI")

# ---------------------------------------------------------------------------------------------------------
# zmienne

game_close = False
styl_czcionki_menu = pygame.font.SysFont("comicsansms", 30)
kolor_tla = (205, 179, 153)

# ---------------------------------------------------------------------------------------------------------
# menu gry wywołujące odpowiednie pętle

while not game_close:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_close = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseX, mouseY = event.pos
                if 33 <= mouseX <= 230 and 66 <= mouseY <= 141:
                    loops.core_game_loop(okno_gry)
                elif 33 <= mouseX <= 230 and 233 <= mouseY <= 308:
                    loops.game_instruction(okno_gry)
                elif 295 <= mouseX <= 490 and 66 <= mouseY <= 141:
                    loops.score_loop(okno_gry)
                elif 295 <= mouseX <= 490 and 233 <= mouseY <= 308:
                    game_close = True

    okno_gry.fill(kolor_tla)
    f.draw_menu(okno_gry, styl_czcionki_menu)
    pygame.display.update()

# ---------------------------------------------------------------------------------------------------------
# zakończenie działani programu

pygame.quit()
quit()
