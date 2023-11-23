import pygame as pg
from time import time
from sys import exit

pg.init()
pg.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "Hang Em High"
FPS = 60
RADIUS = 20  # Button radius
GAP = 15  # Gap between buttons

# Colours
WHITE = "#FFFFFF"
BLACK = "#000000"
RED = "#FF3250"
BTNTOP = "#475F77"
BTNBOTTOM = "#354B5E"
BTNHLGHT = "#D74B4B"
BG = "#17EAD9"


# Fonts
fonts = []
fonts.append(pg.font.Font("assets/fnt/FasterOne-Regular.ttf", 68))  # TITLEFONT
fonts.append(pg.font.Font("assets/fnt/OtomanopeeOne-Regular.ttf", 24))  # FONT
fonts.append(pg.font.Font("assets/fnt/OtomanopeeOne-Regular.ttf", 40))  # WORDFONT
fonts.append(pg.font.Font("assets/fnt/OtomanopeeOne-Regular.ttf", 60))  # MESSAGEFONT
fonts.append(pg.font.Font("assets/fnt/OtomanopeeOne-Regular.ttf", 48))  # MENUTITLEFONT
fonts.append(pg.font.Font("assets/fnt/OtomanopeeOne-Regular.ttf", 40))  # MENUFONT
fonts.append(pg.font.Font(None, 30))  # BTNFONT

# Images
images = []
for i in range(7):
    image = pg.image.load("assets/img/hangman" + str(i) + ".png")
    images.append(image)
ICON = pg.image.load("assets/img/icon.png")
# Letters
letters = []
A = 65
startX = round((SCREEN_WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
startY = 400
for i in range(26):
    x = startX + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = startY + ((i // 13) * (RADIUS * 2 + GAP))
    letters.append([x, y, chr(A + i), True])

# Sounds
WINSND = pg.mixer.Sound("assets/snd/mixkit-small-win-2020.wav")
LOSESND = pg.mixer.Sound("assets/snd/fail-trombone-01.wav")
