import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Наша первая игра')

start_position = None
end_position = None
drawing = False
running = True
speed_x = 5
rect = pygame.Rect(10, 500, 100, 100)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                rect.x += speed_x
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_d]:
            rect.x += speed_x
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (107, 142, 35), rect)
        clock.tick(60)
        pygame.display.flip()
pygame.quit()
