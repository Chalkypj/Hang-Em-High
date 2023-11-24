from math import sqrt
from random import choice
from button import Button
from settings import *


class Game:
    def __init__(self):
        self.canvas = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        self.games_won = 0
        self.games_lost = 0
        self.play_button = Button(
            "Play Again", 140, 40, (SCREEN_WIDTH / 4, SCREEN_HEIGHT - 90), 6, self
        )
        self.quit_button = Button(
            "Quit", 140, 40, (SCREEN_WIDTH / 4 + 350, SCREEN_HEIGHT - 90), 6, self
        )
        self.running = True
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(TITLE)
        pg.display.set_icon(ICON)
        self.words = self.get_words()
        self.game_start()

    def game_start(self):
        self.word = choice(self.words)
        self.words.remove(self.word)
        self.status = 0
        self.win = "None"
        self.game_over = False
        self.guess = []
        self.sound_play = False
        for letter in letters:
            letter[3] = True

    def run(self):
        self.clock.tick()
        self.get_event()
        if self.game_over:
            self.game_finished()
        else:
            self.draw()
            self.update()

    def update(self):
        pass

    def draw(self):
        if self.win != "None":
            self.game_over = True
            if self.win == "Won":
                self.games_won += 1
            else:
                self.games_lost += 1
        else:
            self.draw_title()
            self.draw_score()
            draw_word = self.get_draw_word()
            self.canvas.blit(draw_word, (225, 260))
            self.canvas.blit(images[self.status], (20, 160))
            for letter in letters:
                x, y, ltr, vis = letter
                if vis:
                    pg.draw.circle(self.canvas, BLACK, (x, y), RADIUS, 3)
                    txt = fonts[1].render(ltr, True, BLACK)
                    self.canvas.blit(
                        txt, (x - txt.get_width() / 2, y - txt.get_height() / 2)
                    )
            self.screen.blit(self.canvas, (0, 0))
        pg.display.flip()
        self.check_win()
        if self.game_over:
            self.game_finished()

    def draw_title(self):
        self.canvas.fill(BG)
        txt = fonts[0].render("Hang Em High", True, RED)
        self.canvas.blit(txt, (SCREEN_WIDTH / 2 - txt.get_width() / 2, 20))

    def draw_score(self):
        score = f"Games Won = {self.games_won} Games lost = {self.games_lost}"
        txt = fonts[2].render(score, True, RED)
        self.canvas.blit(txt, (SCREEN_WIDTH / 2 - txt.get_width() / 2, 90))

    def get_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
            if pg.mouse.get_pressed()[0]:
                mousex, mousey = pg.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, vis = letter
                    if vis:
                        dis = sqrt((x - mousex) ** 2 + (y - mousey) ** 2)
                        if dis < RADIUS:
                            letter[3] = False
                            self.guess.append(ltr)
                            if ltr not in self.word:
                                self.status += 1

    def get_words(self):
        words = []
        wordFile = open("words.txt", "r").readlines()
        for line in wordFile:
            words.append(line.strip())
        return words

    def get_draw_word(self):
        txt = ""
        for letter in self.word:
            if letter in self.guess:
                txt += letter + " "
            else:
                txt += "_ "
        draw_word = fonts[2].render(txt, True, BLACK)
        return draw_word

    def check_win(self):
        self.win = "Won"
        for letter in self.word:
            if letter not in self.guess:
                self.win = "None"
            if self.status == 6:
                self.win = "Lost"

    def game_finished(self):
        self.draw_title()
        self.draw_score()
        self.canvas.blit(images[self.status], (100, 160))
        txt = fonts[5].render(self.word, True, BLACK)
        self.canvas.blit(txt, (320, 260))
        txt = fonts[4].render(f"You {self.win}!", True, BLACK)
        self.canvas.blit(txt, (SCREEN_WIDTH / 2 - txt.get_width() / 2, 380))
        self.play_button.draw_button()
        self.quit_button.draw_button()
        if self.win == "Won" and not self.sound_play:
            WINSND.play()
            self.sound_play = True
        elif self.win == "Lost" and not self.sound_play:
            LOSESND.play()
            self.sound_play = True
        self.screen.blit(self.canvas, (0, 0))
        pg.display.flip()
        if self.play_button.pressed:
            self.play_button.pressed = False
            self.game_start()
        if self.quit_button.pressed:
            self.quit_button.pressed = False
            self.running = False
