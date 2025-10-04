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


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 30, 60)
        self.speed_x = 7
        self.speed_y = 7
        self.jumping = False
        self.alive = True
        self.jump_timer = 12

    def update(self):
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

    def draw(self, screen):
        if self.alive is True:
            pygame.draw.rect(screen, (90, 168, 25), self.rect)


class Menu:
    def __init__(self):
        self.start_btn = pygame.rect.Rect(300, 270, 230, 50)
        self.btn_text = font.render('Начать игру', True, (255, 255, 255))
        self.difficult_btn = pygame.rect.Rect(300, 270, 230, 50)
        self.difficult_btn_text = font.render('Выбрать уровень сложности', True, (255, 255, 255))
        self.menu_text = font.render('Меню', True, (255, 255, 255))
        self.pressed = False
        self.in_menu = True

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            if 300 <= pos[0] <= 530 and 270 <= pos[1] <= 320:
                self.in_menu = False
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if 300 <= pos[0] <= 530 and 270 <= pos[1] <= 320:
                self.pressed = True
            else:
                self.pressed = False

    def draw(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.menu_text, (330, 150))
        screen.blit(self.btn_text, (300, 270))
        screen.blit(self.difficult_btn_text, (300, 240))
        if self.pressed is False:
            pygame.draw.rect(screen, (255, 0, 0), self.start_btn)
        else:
            pygame.draw.rect(screen, (0, 0, 255), self.start_btn)
        if self.pressed is False:
            pygame.draw.rect(screen, (255, 0, 0), self.difficult_btn)
        else:
            pygame.draw.rect(screen, (0, 0, 255), self.difficult_btn)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 30, 60)

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 20, 5), self.rect)


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 200, 50)

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 10, 65), self.rect)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.rect = pygame.Rect(x, y, 7, 7)
        self.speed_x = speed

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.x < 0 or self.rect.right > WIDTH:
            self.kill()

    def draw(self, screen):
        pygame.draw.rect(screen, (30, 40, 56), self.rect)


kill_count = 0
x_list = []
y_list = []
for i in range(5):
    x = random.randint(1, 800)
    y = random.randint(1, 750)
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
                    enemy_bullet_left = Bullet(enemy.rect.x, enemy.rect.y + 30, 12)
                    enemy_bullet_right = Bullet(enemy.rect.x, enemy.rect.y + 30, -12)
                    enemy_bullet_group.add(enemy_bullet_left, enemy_bullet_right)
            if event.type == SPAWN_EVENT:
                for i in enemy_group:
                    i.kill()
                    x = random.randint(1, 970)
                    y = random.randint(1, 740)
                    for i in wall_group:
                        while i.rect.x - 50 <= x <= i.rect.x + 250:
                            x = random.randint(1, 970)
                    while i.rect.y - 60 <= y <= i.rect.y + 110:
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
                    i.kill()
            if i.rect.x > WIDTH:
                i.kill()
            if pygame.sprite.collide_rect(player, i):
                player.alive = False
        for i in player_bullet_group:
            i.update()
            for n in wall_group:
                if pygame.sprite.collide_rect(i, n):
                    i.kill()
            if i.rect.x > WIDTH:
                i.kill()
            for x in enemy_group:
                if pygame.sprite.collide_rect(x, i):
                    kill_count += 1
                    x.kill()
                    i.kill()
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
