import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketched_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False

        self.editable = (value == 0)

        # the fonts
        self.value_font = pygame.font.SysFont("arial", 36)
        self.sketch_font = pygame.font.SysFont("arial", 20)

    def set_cell_value(self, value):
        if self.editable:
            self.value = value

    def set_sketched_value(self, value):
        if self.editable:
            self.sketched_value = value

    def draw(self, cell_size):
        x = self.col * cell_size
        y = self.row * cell_size

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0),
                             (x, y, cell_size, cell_size), 3)

        if self.value != 0:
            text = self.value_font.render(str(self.value), True, (0, 0, 0))
            rect = text.get_rect(center=(x + cell_size/2, y + cell_size/2))
            self.screen.blit(text, rect)

        elif self.sketched_value != 0:
            text = self.sketch_font.render(str(self.sketched_value),
                                           True, (110, 110, 110))

            self.screen.blit(text, (x + 4, y + 2))