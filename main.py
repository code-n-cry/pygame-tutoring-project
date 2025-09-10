import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Наша первая игра')

start_position = None
end_position = None
drawing = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not drawing:
            start_position = event.pos
            drawing = True
        if event.type == pygame.MOUSEBUTTONUP and drawing:
            end_position = event.pos
            drawing = False
            left = min(start_position[0], end_position[0])
            top = min(start_position[1], end_position[1])
            width = abs(end_position[0] - start_position[0])
            height = abs(end_position[1] - start_position[1])

            rectangle = pygame.Rect(left, top, width, height)
            pygame.draw.rect(screen, (107, 142, 35), rectangle)
            pygame.display.update()

pygame.quit()
