# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import os

py_folder = os.path.dirname(__file__)   # Папка файла питона
img_folder = os.path.join(py_folder, 'img') # Папка с изображениями в папке питона

player_img = pygame.image.load(os.path.join(img_folder, 'cat.png')) # Добавление изображения
evil_hand_img = pygame.image.load(os.path.join(img_folder, 'evil_hand.png'))

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

        self.speed_x = 0
        self.speed_y = 0
        
        self.x_touch = 0    # Касание по х
        self.y_touch = 0    # Касание по y
        
    def update(self):
        # Движение по координате "х"
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speed_x = -8
        if keystate[pygame.K_d]:
            self.speed_x = 8
        self.rect.x += self.speed_x

        # Ограничение по "х"
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
        # Движение по координате "y"
        self.speed_y = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_w]:
            self.speed_y = -8
        if keystate[pygame.K_s]:
            self.speed_y = 8          
        self.rect.y += self.speed_y   
        
        # Ограничение по "y"
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0       

class Evil_Hand(pygame.sprite.Sprite):  # Спрайт злой руки
    
    def evil_hand_pos(self):
        
        self_rect_x = random.randrange(3*(-self.rect.width), WIDTH + 3*(self.rect.width))
        if self_rect_x > WIDTH // 2:
            self.rect.x = random.randrange(WIDTH + self.rect.width, WIDTH + 3*(self.rect.width))
        else:
            self.rect.x = random.randrange(3*(-self.rect.width), (-self.rect.width))

        self.rect.y = random.randrange(3*(-self.rect.height), HEIGHT + 3*(self.rect.height))
        
        self_speed_x = random.randrange(-8, 8)
        if self_speed_x > -1:
            self.speed_x = random.randrange(1, 8)
        if self_speed_x < 1:
            self.speed_x = random.randrange(-8, -1)

        self_speed_y = random.randrange(-8, 8)
        if self_speed_y > -1:
            self.speed_y = random.randrange(1, 8)
        if self_speed_y < 1:
            self.speed_y = random.randrange(-8, -1)
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = evil_hand_img
        self.rect = self.image.get_rect()
        Evil_Hand.evil_hand_pos(self)
        
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.rect.left > WIDTH + 3*self.rect.width:
            Evil_Hand.evil_hand_pos(self)
            
        if self.rect.right < 0 - 3*self.rect.width:
            Evil_Hand.evil_hand_pos(self)
            
        if self.rect.top > HEIGHT + 3*self.rect.height:
            Evil_Hand.evil_hand_pos(self)

        if self.rect.bottom < 0 - 3*self.rect.height:
            Evil_Hand.evil_hand_pos(self)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Отображение на экране
all_sprites = pygame.sprite.Group() # Создаем в группу all_sprites
mobs = pygame.sprite.Group()

player = Player()
all_sprites.add(player)     # Добавляем спрайт в группу all_sprites

for i in range(random.randrange(10, 20)):
    evil_h = Evil_Hand()
    all_sprites.add(evil_h) # Добавляем спрайт в группу all_sprites
    mobs.add(evil_h)    # Добавляем спрайт в группу mobs

# Цикл игры
running = True
while running:
    clock.tick(FPS) # Держим цикл на правильной скорости
    
    # Ввод процесса (события)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()    # Обновление
    
    screen.fill(BLACK)
    all_sprites.draw(screen)    # Отрисовка всех спрайтов
    
    pygame.display.flip()   # После отрисовки всего, переворачиваем экран

pygame.quit()
