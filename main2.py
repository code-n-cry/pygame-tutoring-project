import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 50)

SPAWN_EVENT = pygame.USEREVENT + 1
kill_count = 0
pygame.time.set_timer(SPAWN_EVENT, 3000)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Наша первая игра')
bg_image = pygame.image.load('background.png')
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
in_menu = True
pressed = False

start_btn = pygame.rect.Rect(300, 270, 230, 50)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 30, 60)
        self.speed_x = random.randint(5, 10)

    def update(self):
        self.rect.x -= self.speed_x

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 20, 5), self.rect)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 7, 7)
        self.speed_x = 12

    def update(self):
        self.rect.x += self.speed_x

    def draw(self, screen):
        pygame.draw.rect(screen, (30, 40, 56), self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 30, 60)
        self.speed_x = 7
        self.speed_y = 2
        self.jumping = False
        self.alive = True
        self.jump_timer = 12

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_d] and self.rect.x + 30 < WIDTH:
            self.rect.x += self.speed_x
        if pressed_keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= self.speed_x

    def jump(self):
        if self.jumping:
            if self.jump_timer >= -12:
                neg = 1
                if self.jump_timer < 0:
                    neg = -1
                self.rect.y -= (self.jump_timer ** 2) // 10 * neg
                self.jump_timer -= 1
            else:
                self.jumping = False
                self.jump_timer = 12

    def draw(self, screen):
        if self.alive is True:
            pygame.draw.rect(screen, (90, 168, 25), self.rect)


player = Player(50, 448)
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemy_count = 5
btn_text = font.render('Начать игру', True, (255, 255, 255))
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
        if in_menu is True and event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if  300 <= pos[0] <= 530 and 270 <= pos[1] <= 320:
                pressed = True
            else:
                pressed = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if in_menu is False:
                    if player.alive is True:
                        bullet = Bullet(player.rect.x, player.rect.y + 30)
                        bullet_group.add(bullet)
                    if event.key == pygame.K_w:
                        player.jumping = True
        if event.type == SPAWN_EVENT:
            if in_menu is False:
                for i in range(enemy_count):
                    enemy = Enemy(x=random.randint(680, 750), y=450)
                    enemy_group.add(enemy)
                enemy_count += 3
    if in_menu is False:
        for i in bullet_group:
            i.update()
            if i.rect.x > 800:
                i.kill()
            for x in enemy_group:
                if pygame.sprite.collide_rect(x, i):
                    kill_count += 1
                    x.kill()
                    i.kill()
        for i in enemy_group:
            i.update()
            if pygame.sprite.collide_rect(i, player):
                player.alive = False
            if i.rect.x < 0:
                i.kill()
        player.update()
        player.jump()
        text = f'Вы убили {kill_count} врагов'
        rendered = font.render(text, True, (255, 0, 0))
        screen.blit(bg_image, (0, 0))
        screen.blit(rendered, (WIDTH - rendered.get_width(), 0))
        for i in bullet_group:
            i.draw(screen)
        for i in enemy_group:
            i.draw(screen)
        player.draw(screen)
    else:
        screen.fill((0, 0, 0))
        if pressed is False:
            pygame.draw.rect(screen, (255, 0, 0), start_btn)
            screen.blit(btn_text, (300, 270))
        else:
            pygame.draw.rect(screen, (0, 0, 255), start_btn)
            screen.blit(btn_text, (300, 270))
    clock.tick(60)
    pygame.display.flip()
