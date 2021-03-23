# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import os

py_folder = os.path.dirname(__file__)   # Папка файла питона
img_folder = os.path.join(py_folder, 'img') # Папка с изображениями в папке питона

player_img = pygame.image.load(os.path.join(img_folder, 'cat.png')) # Добавление изображения

WIDTH = 1600 // 2
HEIGHT = 900 // 2
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.x_reflection = 0
        self.y_reflection = 0
        
    def update(self):
        if self.x_reflection == 0:
            self.rect.x += 3
        if self.x_reflection == 1:
            self.rect.x -= 3
        if self.rect.right > WIDTH:
            self.x_reflection = 1
        if self.rect.left < 0:
            self.x_reflection = 0

        if self.y_reflection == 0:
            self.rect.y += 3
        if self.y_reflection == 1:
            self.rect.y -= 3
        if self.rect.bottom > HEIGHT:
            self.y_reflection = 1
        if self.rect.top < 0:
            self.y_reflection = 0


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()
    
    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
