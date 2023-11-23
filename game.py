from math import sqrt
from random import choice
from button import Button
from settings import *


class Game:
    def __init__(self):
        self.canvas = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(TITLE)
        pg.display.set_icon(ICON)
        self.words = self.get_words()
        self.game_start()

    def game_start(self):
        self.word = choice(self.words)
        self.words.remove(self.word)
        print(self.word)
        self.status = 0
        self.guess = []

    def run(self):
        self.clock.tick()
        self.get_event()
        self.update()
        self.draw()

    def update(self):
        pass

    def draw(self):
        self.canvas.fill(BG)
        txt = fonts[0].render("Hang Em High", True, RED)
        draw_word = self.get_draw_word()
        self.canvas.blit(txt, (SCREEN_WIDTH / 2 - txt.get_width() / 2, 20))
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
