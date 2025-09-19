import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 50)

SPAWN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_EVENT, 3000)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Наша первая игра')
bg_image = pygame.image.load('background.png')
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))


class Menu:
    def __init__(self):
        self.start_btn = pygame.rect.Rect(300, 270, 230, 50)
        self.btn_text = font.render('Начать игру', True, (255, 255, 255))
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
        if self.pressed is False:
            pygame.draw.rect(screen, (255, 0, 0), self.start_btn)
        else:
            pygame.draw.rect(screen, (0, 0, 255), self.start_btn)
        screen.blit(self.btn_text, (300, 270))


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


class Game:
    def __init__(self):
        self.player = Player(50, 448)
        self.menu = Menu()
        self.enemy_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.current_enemies = 3
        self.kill_count = 0

    def update(self, event):
        if self.menu.in_menu is True:
            self.menu.update(event)
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.alive is True:
                        bullet = Bullet(self.player.rect.x, self.player.rect.y + 30)
                        self.bullet_group.add(bullet)
                    if event.key == pygame.K_w:
                        self.player.jumping = True
            if event.type == SPAWN_EVENT:
                for i in range(self.current_enemies):
                    enemy = Enemy(x=random.randint(680, 750), y=450)
                    self.enemy_group.add(enemy)
                self.current_enemies += 3
            for i in self.bullet_group:
                i.update()
                if i.rect.x > 800:
                    i.kill()
                for x in self.enemy_group:
                    if pygame.sprite.collide_rect(x, i):
                        self.kill_count += 1
                        x.kill()
                        i.kill()
            for i in self.enemy_group:
                i.update()
                if pygame.sprite.collide_rect(i, self.player):
                    self.player.alive = False
                if i.rect.x < 0:
                    i.kill()
            self.player.update()
            self.player.jump()

    def draw(self, screen):
        if self.menu.in_menu is True:
            self.menu.draw(screen)
        else:
            text = f'Вы убили {self.kill_count} врагов'
            rendered = font.render(text, True, (255, 0, 0))
            screen.blit(bg_image, (0, 0))
            screen.blit(rendered, (WIDTH - rendered.get_width(), 0))
            for i in self.bullet_group:
                i.draw(screen)
            for i in self.enemy_group:
                i.draw(screen)
            self.player.draw(screen)


game = Game()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        game.update(event)
    game.draw(screen)
    clock.tick(60)
    pygame.display.flip()
