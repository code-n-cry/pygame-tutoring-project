import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Наша первая игра')

start_position = None
end_position = None
#drawing = False  # Идет ли процесс выбора прямоугольника
count = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            count += 1
            if count % 2 == 1:
                start_position = event.pos
            else:
                end_position = event.pos
                left = min(start_position[0], end_position[0])
                top = min(start_position[1], end_position[1])
                width = abs(end_position[0] - start_position[0])
                height = abs(end_position[1] - start_position[1])
                rectangle = pygame.Rect(left, top, width, height)
                pygame.draw.rect(screen, (107, 142, 35), rectangle)
                pygame.display.update()

pygame.quit()
