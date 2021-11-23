import pygame

if __name__ == '__main__':
    pygame.init()
    print('Укажите размер поля w и количество клеток n(w кратно n)')
    try:
        w, n = map(int, input().split())
    except TypeError:
        print('Неверный формат')
    # except ValueError:
    #     print('Неверно указанные значения')
    else:
        size = w, w
        screen = pygame.display.set_mode(size)
        screen.fill(pygame.Color("#ffcc00"))
        pygame.display.set_caption('Шахматы')
        black_color = True  # черный цвет клетки
        for i in range(n):
            if (n - i) % 2 == 1:
                black_color = True
            for j in range(n):
                if black_color:
                    color = pygame.Color(0, 0, 0)
                else:
                    color = pygame.Color(255, 255, 255)
                pygame.draw.rect(screen, color,
                                 (w // n * i, w // n * j, w // n, w // n))
                black_color = not black_color
        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.flip()
        # завершение работы:
        pygame.quit()
