import pygame


class NonMultiple(Exception):
    pass


if __name__ == '__main__':
    try:
        d, n = map(int, input().split())
    except ValueError:
        print('Неверные значения')
    except TypeError:
        print('Неверные значения')
    except NonMultiple:
        pass
    else:
        pygame.init()
        size = width, height = 300, 300
        screen = pygame.display.set_mode(size)
        screen.fill((0, 0, 0))
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
        for i in range(n):
            color = colors[i % 3]
            pygame.draw.circle(screen, color, (width // 2, height // 2), width // 2 - d * i)
        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.flip()
        # завершение работы:
        pygame.quit()
