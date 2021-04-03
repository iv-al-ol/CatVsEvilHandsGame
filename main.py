#====================================================================
# Импорт необходимых модулей
#--------------------------------------------------------------------
import pygame as pg
import random as rnd
import os

#====================================================================
# Параметры окна
#--------------------------------------------------------------------
WIDTH = 1600
HEIGHT = 900
FPS = 60

pg.display.set_caption("Cat vs Evil Hands")
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

#====================================================================
# Работа с файловой системой
#--------------------------------------------------------------------
py_folder = os.path.dirname(__file__)   # Папка файла питона
img_folder = os.path.join(py_folder, 'img') # Папка с изображениями в папке питона
bullets_folder = os.path.join(img_folder, 'bullets')
cat_move_folder = os.path.join(img_folder, 'cat_move')
#--------------------------------------------------------------------
cat_player_img = pg.image.load(os.path.join(cat_move_folder,
    'cat_looks_right.png')).convert_alpha()
#--------------------------------------------------------------------
evil_hand_img = pg.image.load(os.path.join(img_folder,
    'evil_hand.png')).convert_alpha()
#--------------------------------------------------------------------
background_img = pg.image.load(os.path.join(img_folder,
    'darkPurple.png')).convert_alpha()
#--------------------------------------------------------------------
bullets_img = []
bullets_list = ['bullet_1.png', 'bullet_2.png','bullet_3.png',
                 'bullet_4.png', 'bullet_5.png']
for img in bullets_list:
    bullets_img.append(pg.image.load(os.path.join(bullets_folder,
                                                  img)).convert_alpha())
#--------------------------------------------------------------------

#====================================================================
# Задание цветов
#--------------------------------------------------------------------
WHITE         = (255, 255, 255)
BLACK         = (  0,   0,   0)
RED           = (255,   0,   0)
GREEN         = (  0, 255,   0)
BLUE          = (  0,   0, 255)
YELLOW        = (255, 255,   0)
JADE          = (  0, 168, 107)
DARK_BROWN    = (101,  67,  33)

#####################################################################
# Функции
#####################################################################
def draw_ground():
    """
    Закрашивает фон экрана рисунком
    """
    background_rect = background_img.get_rect()
    
    ground_limit_x = WIDTH // background_rect.width + 1
    ground_limit_y = HEIGHT // background_rect.height + 1
    
    for line_y in range (ground_limit_y):
        for line_x in range(ground_limit_x):
            screen.blit(background_img, (0 + line_x*(background_rect.height),
                                         0 + line_y*(background_rect.height)))

def debug_hits(self):
    """
    Рисование круга для проверки столкновений
    """
    self.rect = self.image.get_rect()
    self.radius = self.image.get_height() // 2 - int(self.image.get_height() * 0.1)
    pg.draw.circle(self.image, RED, self.rect.center, self.radius)

#####################################################################
# ОБЪЕКТЫ
#####################################################################
#====================================================================
# Объект игрока
#--------------------------------------------------------------------
class Cat(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(cat_player_img,
                                        (cat_player_img.get_width()*2,
                                         cat_player_img.get_height()*2))       
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2

        self.speed_x = 0
        self.speed_y = 0
        
        self.x_touch = 0    # Касание по х
        self.y_touch = 0    # Касание по y
        
    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        keystate = pg.key.get_pressed()
        
        # Движение по координате "х"
        if keystate[pg.K_a]:
            self.speed_x = -8
        if keystate[pg.K_d]:
            self.speed_x = 8
        self.rect.x += self.speed_x
        
        # Движение по координате "y"
        if keystate[pg.K_w]:
            self.speed_y = -8
        if keystate[pg.K_s]:
            self.speed_y = 8          
        self.rect.y += self.speed_y
        
        # Ограничение по "х"
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
                
        # Ограничение по "y"
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        
    def shot(self, shot_direction):
        bullet = Bullet(self.rect.right + 10, self.rect.centery - 10, shot_direction)
        all_sprites.add(bullet)
        bullets.add(bullet)
        
#====================================================================
# Объект противника
#--------------------------------------------------------------------
class EvilHand(pg.sprite.Sprite):
    def evil_hand_pos(self):
        """
        Определяет начальную позицию и скорость
        """
        self_rect_x = rnd.randrange(3*(-self.rect.width),
                                    WIDTH + 3*(self.rect.width))
        if self_rect_x > WIDTH // 2:
            self.rect.x = rnd.randrange(WIDTH + self.rect.width,
                                        WIDTH + 3*(self.rect.width))
        else:
            self.rect.x = rnd.randrange(3*(-self.rect.width),
                                        (-self.rect.width))
        self.rect.y = rnd.randrange(3*(-self.rect.height),
                                    HEIGHT + 3*(self.rect.height))
        
        self_speed_x = rnd.randrange(-8, 8)
        if self_speed_x > -1:
            self.speed_x = rnd.randrange(1, 8)
        if self_speed_x < 1:
            self.speed_x = rnd.randrange(-8, -1)

        self_speed_y = rnd.randrange(-8, 8)
        if self_speed_y > -1:
            self.speed_y = rnd.randrange(1, 8)
        if self_speed_y < 1:
            self.speed_y = rnd.randrange(-8, -1)
    
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image_orig = evil_hand_img
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        EvilHand.evil_hand_pos(self)
        
        self.rot = 0
        self.rot_speed = rnd.randrange(-10, 10)
        self.last_update = pg.time.get_ticks()
    
    def rotate(self):
        """
        Задает вращение
        """
        now = pg.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now  
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pg.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
        
    def update(self):
        self.rotate()
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.rect.left > WIDTH + 3*self.rect.width:
            EvilHand.evil_hand_pos(self)
            
        if self.rect.right < 0 - 3*self.rect.width:
            EvilHand.evil_hand_pos(self)
            
        if self.rect.top > HEIGHT + 3*self.rect.height:
            EvilHand.evil_hand_pos(self)

        if self.rect.bottom < 0 - 3*self.rect.height:
            EvilHand.evil_hand_pos(self)
        
#====================================================================
# Объект выстрелов
#--------------------------------------------------------------------
class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, shot_direction):
        pg.sprite.Sprite.__init__(self)
        self.image = rnd.choice(bullets_img)
        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.centery = y
        
        self.speed_x = 0
        self.speed_y = 0
        self.radius = self.image.get_height() // 2 - int(self.image.get_height() * 0.05)

    def update(self):
        if (shot_direction == 'up'):
            self.speed_y = -10
        elif (shot_direction == 'down'):
            self.speed_y = 10
        elif (shot_direction == 'left'):
            self.speed_x = -10
        elif (shot_direction == 'right'):
            self.speed_x = 10
            
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
                
        # Удалить спрайт, если вышел за границу окна
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.top > HEIGHT:
            self.kill()
        if self.rect.right < 0:
            self.kill()
        if self.rect.left > WIDTH:
            self.kill()

#====================================================================
# Создаем игру и окно
#--------------------------------------------------------------------
pg.init()
pg.mixer.init()
#--------------------------------------------------------------------

#====================================================================
# Создание групп спрайтов
#--------------------------------------------------------------------
all_sprites = pg.sprite.Group()
mobs        = pg.sprite.Group()
bullets     = pg.sprite.Group()
#--------------------------------------------------------------------

#====================================================================
# Добавление спрайтов в группы спрайтов
#--------------------------------------------------------------------
cat_player = Cat()
all_sprites.add(cat_player) # Добавляем спрайт в группу all_sprites

for i in range(rnd.randrange(15, 30)):
    evil_h = EvilHand()
    all_sprites.add(evil_h) # Добавляем спрайт в группу all_sprites
    mobs.add(evil_h)    # Добавляем спрайт в группу mobs
#--------------------------------------------------------------------

#====================================================================
# Цикл игры
#--------------------------------------------------------------------
running = True
while running:
    clock.tick(FPS) # Держим цикл на правильной скорости

    #----------------------------------------------------------------
    # Проверка событий
    #----------------------------------------------------------------
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if (event.key == pg.K_UP):
                shot_direction = 'up'
                cat_player.shot(shot_direction)
            elif (event.key == pg.K_DOWN):
                shot_direction = 'down'
                cat_player.shot(shot_direction)
            elif (event.key == pg.K_LEFT):
                shot_direction = 'left'
                cat_player.shot(shot_direction)
            elif (event.key == pg.K_RIGHT):
                shot_direction = 'right'
                cat_player.shot(shot_direction)
            else:
                shot_direction = None
    #----------------------------------------------------------------

    all_sprites.update()    # Обновление всех спрайтов
    
    #----------------------------------------------------------------
    # Проверка касания групп спрайтов
    #----------------------------------------------------------------
    hits = pg.sprite.groupcollide(bullets, mobs, True, True,
                                  pg.sprite.collide_rect_ratio(0.95))
    for hit in hits:
        eh = EvilHand()
        all_sprites.add(eh)
        mobs.add(eh)

    #----------------------------------------------------------------
    # Проверка касания спрайта с группой спрайтов
    #----------------------------------------------------------------
    hits = pg.sprite.spritecollide(cat_player, mobs, False,
                                   pg.sprite.collide_rect_ratio(0.95))
    if hits:
        running = False
    
    #----------------------------------------------------------------
    draw_ground()   # Закрасить фон
    
    all_sprites.draw(screen)    # Отрисовка всех спрайтов
    pg.display.flip()   # После отрисовки всего, переворачиваем экран
#--------------------------------------------------------------------

pg.quit()
