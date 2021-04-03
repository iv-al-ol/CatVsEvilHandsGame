"""
Soundtrack - Fato Shadow
"""

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

pg.mixer.init()
pg.mixer.music.set_volume(0.1)
pg.display.set_caption("Cat vs Evil Hands")
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

#====================================================================
# Работа с файловой системой
#--------------------------------------------------------------------
folder_py       = os.path.dirname(__file__)   # Директория .py файла

folder_img          = 'img'         # Главная папка с изображениями
folder_cat_move     = 'cat_move'    # Подпапка с изображениями кота
folder_bullets      = 'bullets'     # Подпапка с изображениями снарядов

folder_snd          = 'snd'         # Главная папка со звуками

#====================================================================
# Добавление файлов игры
#--------------------------------------------------------------------
# Добавление рисунков
#--------------------------------------------------------------------
def add_image(add_image_list, folder_img, subfolder_img=None):
    """Добавляет изображения в игру.
    
    add_image_list -> tuple: Имена рисунков с расширениями файлов
        (например: ['pic_1.png', 'pic_2.png']);
    folder_img -> str: Имя папки с изображениями;
    subfolder_img -> str: Имя подпапки с изображениями;
    
    Возвращает сконвертированные изображения в составе списка.
    
    """
    folder_img = os.path.join(folder_py, str(folder_img))   # Определение папки с изображениями
    added_img_list = []
    if (subfolder_img != None):
        subfolder_img = os.path.join(folder_img, str(subfolder_img))    # Определение подпапки с изображениями
        for img in add_image_list:
            added_img_list.append(pg.image.load(os.path.join(subfolder_img, img)).convert_alpha())
    else:
        for img in add_image_list:    
            added_img_list.append(pg.image.load(os.path.join(folder_img, img)).convert_alpha())
    return added_img_list

img_cat_player = add_image(['cat_looks_right.png'], folder_img, folder_cat_move)
img_cat_player = img_cat_player[0]

img_bullets = add_image(['bullet_1.png', 'bullet_2.png',
                'bullet_3.png', 'bullet_4.png', 'bullet_5.png'], folder_img, folder_bullets)

img_evil_hand = add_image(['evil_hand.png'], folder_img)
img_evil_hand = img_evil_hand[0]

img_background = add_image(['darkPurple.png'], folder_img)
img_background = img_background[0]

#--------------------------------------------------------------------
# Добавление звуков
#--------------------------------------------------------------------
def add_sound(add_sound_list, folder_snd, subfolder_snd=None):
    """Добавляет звуки в игру.
    
    add_sound_list -> tuple: Имена звуков с расширениями файлов
        (например: ['sound_1.mp3', 'sound_2.wav']);
    folder_snd -> str: Имя папки со звуками;
    subfolder_snd -> str: Имя подпапки со звуками;
    
    Возвращает добавленные звуки в составе списка.
    
    """
    folder_snd = os.path.join(folder_py, str(folder_snd))   # Определение папки со звуками
    added_sound_list = []
    if (subfolder_snd != None):
        subfolder_snd = os.path.join(folder_snd, str(subfolder_snd))    # Определение подпапки со звуками
        for snd in add_sound_list:
            added_sound_list.append(pg.mixer.Sound(os.path.join(subfolder_snd, snd)))
    else:
        for snd in add_sound_list:    
            added_sound_list.append(pg.mixer.Sound(os.path.join(folder_snd, snd)))
    return added_sound_list

def add_music(add_music_list, folder_snd, subfolder_snd=None):
    """Добавляет музыку в игру.
    
    add_music_list -> tuple: Имена музыки с расширениями файлов
        (например: ['music_1.mp3', 'music_2.wav']);
    folder_snd -> str: Имя папки c музыкой;
    subfolder_snd -> str: Имя подпапки с музыкой;
    
    Возвращает добавленную музыку в составе списка.
    
    """
    folder_snd = os.path.join(folder_py, str(folder_snd))   # Определение папки с музыкой
    added_music_list = []
    if (subfolder_snd != None):
        subfolder_snd = os.path.join(folder_snd, str(subfolder_snd))    # Определение подпапки с музыкой
        for mus in add_music_list:
            added_music_list.append(pg.mixer.music.load(os.path.join(subfolder_snd, mus)))
    else:
        for mus in add_music_list:    
            added_music_list.append(pg.mixer.music.load(os.path.join(folder_snd, mus)))
    return added_music_list

soundtrack_1 = add_music(['soundtrack_1.mp3'], folder_snd)
soundtrack_1 = soundtrack_1[0]

snd_shoot = add_sound(['shoot_1.wav', 'shoot_2.wav', 'shoot_3.wav'], folder_snd)

snd_explosion = add_sound(['explosion_1.wav', 'explosion_2.wav', 'explosion_3.wav'], folder_snd)
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
    """Закрашивает фон экрана рисунком"""
    background_rect = img_background.get_rect()
    
    ground_limit_x = WIDTH // background_rect.width + 1
    ground_limit_y = HEIGHT // background_rect.height + 1
    
    for line_y in range (ground_limit_y):
        for line_x in range(ground_limit_x):
            screen.blit(img_background, (0 + line_x*(background_rect.height),
                                         0 + line_y*(background_rect.height)))

def debug_hits(self):
    """Рисует круг для проверки столкновений"""
    self.rect = self.image.get_rect()
    self.radius = self.image.get_height() // 2 - int(self.image.get_height() * 0.1)
    pg.draw.circle(self.image, RED, self.rect.center, self.radius)

def draw_text(surf, text, size, x, y):
    """Выводит текст на поверхности с заданными параметрами.
    
    surf: Поверхность отображения текста;
    text: Отображаемый текст;
    size: Размер шрифта;
    x: Координата середины блока текста по x 
    y: Координата верха блока текста по y
    
    """
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

#####################################################################
# ОБЪЕКТЫ
#####################################################################
#====================================================================
# Объект игрока
#--------------------------------------------------------------------
class Cat(pg.sprite.Sprite):
    """Объект игрока. Выводит спрайт кота."""
    
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(img_cat_player,
                                        (img_cat_player.get_width()*2,
                                         img_cat_player.get_height()*2))       
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2

        self.speed_x = 0
        self.speed_y = 0
        
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
        
    def shoot(self, shot_direction):
        """Выводит спрайт снаряда.
        
        shot_direction: направление полета снаряда.
        Принимает значения типа str(): 'up', 'down', 'left', 'right'.
        
        """
        bullet = Bullet(self.rect.right + 10, self.rect.centery - 10, shot_direction)
        all_sprites.add(bullet)
        bullets.add(bullet)
        rnd.choice(snd_shoot).play()
        
        
#====================================================================
# Объект противника
#--------------------------------------------------------------------
class EvilHand(pg.sprite.Sprite):
    """Объект противника. Выводит спрайт злых рук."""
    
    def evil_hand_pos(self):
        """Определяет начальную позицию и скорость злых рук."""
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
        self.image_orig = img_evil_hand
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
    """Объект снарядов. Выводит спрайт снарядов."""
    
    def __init__(self, x, y, shot_direction):
        pg.sprite.Sprite.__init__(self)
        self.image = rnd.choice(img_bullets)
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
# Создаем окно игры
#--------------------------------------------------------------------
pg.init()
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
# Подсчет очков
#--------------------------------------------------------------------
score = 0

#====================================================================
# Цикл игры
#--------------------------------------------------------------------
pg.mixer.music.play(loops=-1)   # Запуск музыки

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
                cat_player.shoot(shot_direction)
            elif (event.key == pg.K_DOWN):
                shot_direction = 'down'
                cat_player.shoot(shot_direction)
            elif (event.key == pg.K_LEFT):
                shot_direction = 'left'
                cat_player.shoot(shot_direction)
            elif (event.key == pg.K_RIGHT):
                shot_direction = 'right'
                cat_player.shoot(shot_direction)
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
        score += 1
        rnd.choice(snd_explosion).play()
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
    draw_text(screen, str('Уничтожено рук: %s' % score), 20, WIDTH // 2, 10)
#-------------------------------------------------------------------- 
    pg.display.flip()   # После отрисовки всего, переворачиваем экран
#--------------------------------------------------------------------

pg.quit()
