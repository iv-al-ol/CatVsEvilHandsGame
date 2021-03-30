# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import os

py_folder = os.path.dirname(__file__)   # Папка файла питона
img_folder = os.path.join(py_folder, 'img') # Папка с изображениями в папке питона

player_img = pygame.image.load(os.path.join(img_folder, 'cat.png')) # Добавление изображения

WIDTH = 600
HEIGHT = 900
FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):         # Спрайт игрока
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

        self.speedx = 0
        self.speedy = 0
        
        self.x_reflection = 0
        self.y_reflection = 0
        
    def update(self):
        # Движение по координате "х"
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx

        # Ограничение по "х"
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
        # Движение по координате "y"
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8          
        self.rect.y += self.speedy   
        
        # Ограничение по "y"
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0       

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Отображение на экране
all_sprites = pygame.sprite.Group()     # Каждый созданный спрайт должен быть в группе all_sprites
player = Player()
all_sprites.add(player)     # Спрайт игрока добавляется в группу all_sprites

# Цикл игры
running = True
while running:
    
    clock.tick(FPS) # Держим цикл на правильной скорости
    
    # Ввод процесса (события)
    for event in pygame.event.get():
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
