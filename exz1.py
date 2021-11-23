import pygame
import random

if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 800, 600
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color("#ffffff"))
    screen.fill(pygame.Color('red'), (100, 100, 600, 400))


    def draw(screen):
        font = pygame.font.Font(None, 50)
        text = font.render("Hello, Pygame!", True, pygame.Color("#ffcc00"))
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 2 - text.get_height() // 2
        text_w = text.get_width()
        text_h = text.get_height()
        pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10,
                                               text_w + 20, text_h + 20), 5)
        screen.blit(text, (text_x, text_y))


    def draw_pix(screen):
        for i in range(10000):
            screen.fill(pygame.Color('black'),
                        (random.random() * width,
                         random.random() * height, 2, 2))


    def draw_square(screen):
        color = pygame.Color(50, 150, 50)
        # рисуем "тень"
        pygame.draw.rect(screen, color,
                         (20, 20, 100, 100), 0)
        hsv = color.hsva
        # увеличиваем параметр Value, который влияет на яркость
        color.hsva = (hsv[0], hsv[1], hsv[2] + 30, hsv[3])
        # рисуем сам объект
        pygame.draw.rect(screen, color, (10, 10, 100, 100), 0)


    draw(screen)
    draw_square(screen)
    # draw_pix(screen)

    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()

    pygame.quit()
