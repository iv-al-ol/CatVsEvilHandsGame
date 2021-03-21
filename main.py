import pygame
import os
import random

# Основные параметры
WIDTH = 1600 // 2 # Ширина игрового окна
HEIGHT = 900 // 2 # Высота игрового окна
FPS = 30 # Частота кадров в секунду

# Цвета (R, G, B)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()   # Запускает pygame
pygame.mixer.init()  # Для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT))   # Окно программы
pygame.display.set_caption("Первая тестовая игра")  # Отображение названия в окне
clock = pygame.time.Clock()     # Убедиться в частоте кадров

# Цикл игры
running = True

while running:
    clock.tick(FPS) # Контроль "тиков" (ФПС)
    # Ввод процесса (события)
    
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
    
    # Обновление
    
    # Визуализация (сборка)
    # Рендеринг
    screen.fill(BLACK)  # Залить окно чёрным
    pygame.display.flip()   # "Повернуть" экран для отображения отрисовок
    
pygame.quit # Завершение программы
