from settings import *


class Button:
    def __init__(self, text, width, height, pos, elevation, game):
        self.elevation = elevation
        self.dynamic = elevation
        self.original_y = pos[1]
        self.button_top = pg.Rect(pos, (width, height))
        self.button_top_colour = BTNTOP
        self.button_top_text = fonts[6].render(text, True, WHITE)
        self.button_text_rect = self.button_top_text.get_rect(
            center=self.button_top.center
        )
        self.button_bottom = pg.Rect(pos, (width, elevation))
        self.button_bottom_colour = BTNBOTTOM
        self.pressed = False
        self.game = game

    def draw_button(self):
        self.button_top.y = self.original_y - self.dynamic
        self.button_text_rect.center = self.button_top.center
        self.button_bottom.midtop = self.button_top.midtop
        self.button_bottom.height = self.button_top.height + self.dynamic
        pg.draw.rect(
            self.game.canvas,
            self.button_bottom_colour,
            self.button_bottom,
            border_radius=18,
        )
        pg.draw.rect(
            self.game.canvas, self.button_top_colour, self.button_top, border_radius=18
        )
        self.game.canvas.blit(self.button_top_text, self.button_text_rect)
        self.check_click()

    def check_click(self):
        mousePos = pg.mouse.get_pos()
        if self.button_top.collidepoint(mousePos):
            self.button_top_colour = BTNHLGHT
            if pg.mouse.get_pressed()[0]:
                self.dynamic = 0
                self.pressed = True
            else:
                self.dynamic = self.elevation
                if self.pressed == True:
                    self.pressed = False
        else:
            self.dynamic = self.elevation
            self.button_top_colour = BTNTOP
