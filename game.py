import pygame
import random

pygame.init()

WIDTH, HEIGHT = 1000, 800
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()
SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 3000)
TIME_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(TIME_EVENT, 1500)
clock = pygame.time.Clock()

font = pygame.font.SysFont('Bitcount Grid Double Ink', 50)

enemy_bullet_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
difficult = "easy"


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.speed_x = 7
        self.speed_y = 7
        self.jumping = False
        self.player_life = 3
        self.alive = True
        self.jump_timer = 12
        self.image = pygame.image.load("images/player.png")
        self.image = pygame.transform.scale(self.image,(30, 60))
        self.rect = self.image.get_rect()

    def update(self):
        global wall_group
        overlap = False
        old_x = self.rect.x
        old_y = self.rect.y
        if self.alive:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_d] and self.rect.x + 30 < WIDTH:
                self.rect.x += self.speed_x
            if pressed_keys[pygame.K_a] and self.rect.x > 10:
                self.rect.x -= self.speed_x
            if pressed_keys[pygame.K_s] and self.rect.y + 60 < HEIGHT:
                self.rect.y += self.speed_y
            if pressed_keys[pygame.K_w] and self.rect.y > 0:
                self.rect.y -= self.speed_y
            for wall in wall_group:
                if pygame.sprite.collide_rect(self, wall):
                    self.rect.x = old_x
                    self.rect.y = old_y

    def draw(self, screen):
        if self.alive is True:
            screen.blit(self.image, self.rect)


class Menu:
    def __init__(self):
        self.start_btn = pygame.rect.Rect(300, 270, 230, 50)
        self.btn_text = font.render('Начать игру', True, (255, 255, 255))
        self.easy_btn = pygame.rect.Rect(300, 170, 230, 50)
        self.btn_easy_text = font.render('Легкий', True, (255, 255, 255))
        self.normal_btn = pygame.rect.Rect(300, 270, 230, 50)
        self.btn_normal_text = font.render('Нормальный', True, (255, 255, 255))
        self.hard_btn = pygame.rect.Rect(300, 370, 230, 50)
        self.btn_hard_text = font.render('Сложный', True, (255, 255, 255))
        self.difficult_btn = pygame.rect.Rect(300, 370, 500, 50)
        self.difficult_btn_text = font.render('Выбрать уровень сложности', True, (255, 255, 255))
        self.menu_text = font.render('Меню', True, (255, 255, 255))
        self.difficult_pressed = False
        self.choice = False
        self.start_pressed = False
        self.in_menu = True

    def update(self, event):
        global difficult, enemy_count, player
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if self.choice == False:
                if 300 <= pos[0] <= 530 and 270 <= pos[1] <= 320:
                    self.in_menu = False
                    x_list = []
                    y_list = []
                    wall_count = 0
                    if difficult == "easy":
                        wall_count = 5
                        enemy_count = 1
                        player.player_life = 3
                    if difficult == "normal":
                        wall_count = 7
                        enemy_count = 2
                        player.player_life = 2
                    if difficult == "hard":
                        wall_count = 9
                        enemy_count = random.randint(3, 4)
                        player.player_life = 1
                    for i in range(wall_count):
                        x = random.randint(50, 800)
                        y = random.randint(50, 750)
                        if not x_list and not y_list:
                            x_list.append(x)
                            y_list.append(y)
                        else:
                            for i in range(len(x_list)):
                                while x_list[i] - 70 <= x <= x_list[i] + 270:
                                    x = random.randint(1, 800)
                                while y_list[i] - 70 <= y <= y_list[i] + 270:
                                    y = random.randint(1, 750)
                            x_list.append(x)
                            y_list.append(y)
                        wall = Wall(x, y)
                        wall_group.add(wall)
                if 300 <= pos[0] <= 800 and 370 <= pos[1] <= 420:
                    self.choice = True
            else:
                if 300 <= pos[0] <= 500 and 170 <= pos[1] <= 320:
                    difficult = "easy"
                if 300 <= pos[0] <= 500 and 270 <= pos[1] <= 420:
                    difficult = "normal"
                if 300 <= pos[0] <= 500 and 370 <= pos[1] <= 520:
                    difficult = "hard"
                self.choice = False

        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if 300 <= pos[0] <= 530 and 270 <= pos[1] <= 320:
                self.start_pressed = True
            else:
                self.start_pressed = False
            if 300 <= pos[0] <= 800 and 370 <= pos[1] <= 420:
                self.difficult_pressed = True
            else:
                self.difficult_pressed = False

    def draw(self, screen):
        screen.fill((0, 0, 0))
        if self.choice == False:
            if self.start_pressed is False:
                pygame.draw.rect(screen, (255, 0, 0), self.start_btn)
            else:
                pygame.draw.rect(screen, (0, 0, 255), self.start_btn)
            if self.difficult_pressed is False:
                pygame.draw.rect(screen, (255, 0, 0), self.difficult_btn)
            else:
                pygame.draw.rect(screen, (0, 0, 255), self.difficult_btn)
            screen.blit(self.menu_text, (370, 170))
            screen.blit(self.btn_text, (300, 270))
            screen.blit(self.difficult_btn_text, (300, 370))
        else:
            pygame.draw.rect(screen, (255, 0, 0), self.easy_btn)
            pygame.draw.rect(screen, (255, 0, 0), self.normal_btn)
            pygame.draw.rect(screen, (255, 0, 0), self.hard_btn)
            screen.blit(self.btn_easy_text, (370, 170))
            screen.blit(self.btn_normal_text, (300, 270))
            screen.blit(self.btn_hard_text, (300, 370))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("images/enemy.png")
        self.image = pygame.transform.scale(self.image, (30, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 200, 50)

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 10, 65), self.rect)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.image.load("images/bullet.png")
        self.image = pygame.transform.scale(self.image, (7, 7))
        self.explosion_1 = pygame.image.load("images/explosion/1.png")
        self.explosion_1 = pygame.transform.scale(self.explosion_1, (50, 50))
        self.explosion_2 = pygame.image.load("images/explosion/2.png")
        self.explosion_2 = pygame.transform.scale(self.explosion_2, (50, 50))
        self.explosion_3 = pygame.image.load("images/explosion/3.png")
        self.explosion_3 = pygame.transform.scale(self.explosion_3, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed
        self.explosion_images = [self.explosion_1,
                                 self.explosion_2, self.explosion_2, self.explosion_3,
                                 self.explosion_3, self.explosion_3]
        self.current_explosion = 0
        self.explosion = False

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.x < 30 or self.rect.right > WIDTH - 50:
            self.explosion = True
        if self.explosion:
            self.speed_x = 0
            if self.current_explosion < len(self.explosion_images):
                self.image = self.explosion_images[self.current_explosion]
                self.current_explosion += 1
            elif self.current_explosion >= len(self.explosion_images) - 1:
                self.kill()

    def draw(self, screen):
        pygame.draw.rect(screen, (30, 40, 56), self.rect)
        screen.blit(self.image, self.rect)


kill_count = 0
enemy_count = 1
player = Player(50, 250)
menu = Menu()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if menu.in_menu is True:
            menu.update(event)
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player.alive:
                        bullet = Bullet(player.rect.x, player.rect.y + 30, 12)
                        player_bullet_group.add(bullet)
            if event.type == TIME_EVENT:
                for i in enemy_group:
                    enemy_bullet_left = Bullet(i.rect.x, i.rect.y + 30, 12)
                    enemy_bullet_right = Bullet(i.rect.x, i.rect.y + 30, -12)
                    enemy_bullet_group.add(enemy_bullet_left, enemy_bullet_right)
            if event.type == SPAWN_EVENT:
                for c in range(enemy_count):
                    x = random.randint(51, 970)
                    y = random.randint(51, 740)
                    for i in enemy_group:
                        while len(enemy_group) >= enemy_count:
                            i.kill()
                        for i in wall_group:
                            while i.rect.x - 250 <= x <= i.rect.x + 350:
                                x = random.randint(1, 970)
                            while i.rect.y - 120 <= y <= i.rect.y + 120:
                                y = random.randint(1, 740)
                    enemy = Enemy(x, y)
                    enemy_group.add(enemy)
                    if pygame.sprite.collide_rect(i, player):
                        player.alive = False
                    if i.rect.x < 0:
                        i.kill()
    if not menu.in_menu:
        for i in enemy_group:
            i.update()
        player.update()
        text = f'Вы убили {kill_count} врагов'
        rendered = font.render(text, True, (255, 0, 0))
        for i in enemy_bullet_group:
            i.update()
            for g in wall_group:
                if pygame.sprite.collide_rect(i, g):
                    i.explosion = True
            if pygame.sprite.collide_rect(player, i):
                i.explosion = True
                if player.player_life <= 0:
                    player.alive = False
                else:
                    player.player_life -= 1
        for i in player_bullet_group:
            i.update()
            for n in wall_group:
                if pygame.sprite.collide_rect(i, n):
                    i.explosion = True
            for enemy in enemy_group:
                if pygame.sprite.collide_rect(enemy, i):
                    kill_count += 1
                    enemy.kill()
                    i.explosion = True
    if menu.in_menu is True:
        menu.draw(screen)
    else:
        screen.fill((0, 0, 0))
        screen.blit(rendered, (WIDTH - rendered.get_width(), 0))
        for i in enemy_group:
            i.draw(screen)
        for i in enemy_bullet_group:
            i.draw(screen)
        for i in player_bullet_group:
            i.draw(screen)
        for i in wall_group:
            i.draw(screen)
        player.draw(screen)
    clock.tick(60)
    pygame.display.flip()
