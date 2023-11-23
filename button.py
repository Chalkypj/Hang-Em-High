from settings import *


class Button:
    def __init__(self, text, width, height, pos, elevation, game):
        self.elevation = elevation
        self.dynamic = elevation
        self.originalY = pos[1]
        self.btnTop = pg.Rect(pos, (width, height))
        self.btnTopColor = BTNTOP
        self.btnTopText = fonts[6].render(text, True, WHITE)
        self.btnTxtRect = self.btnTopText.get_rect(center=self.btnTop.center)
        self.btnBottom = pg.Rect(pos, (width, elevation))
        self.btnBottomColor = BTNBOTTOM
        self.pressed = False
        self.game = game

    def drawBtn(self):
        self.btnTop.y = self.originalY - self.dynamic
        self.btnTxtRect.center = self.btnTop.center
        self.btnBottom.midtop = self.btnTop.midtop
        self.btnBottom.height = self.btnTop.height + self.dynamic
        pg.draw.rect(
            self.game.gameSurface, self.btnBottomColor, self.btnBottom, border_radius=18
        )
        pg.draw.rect(
            self.game.gameSurface, self.btnTopColor, self.btnTop, border_radius=18
        )
        self.game.gameSurface.blit(self.btnTopText, self.btnTxtRect)
        self.checkClick()

    def checkClick(self):
        mousePos = pg.mouse.get_pos()
        if self.btnTop.collidepoint(mousePos):
            self.btnTopColor = BTNHLGHT
            if pg.mouse.get_pressed()[0]:
                self.dynamic = 0
                self.pressed = True
            else:
                self.dynamic = self.elevation
                if self.pressed == True:
                    self.pressed = False
        else:
            self.dynamic = self.elevation
            self.btnTopColor = BTNTOP
