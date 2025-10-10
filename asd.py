for i in range(wall_count):
    x = random.randint(100, 800)
    y = random.randint(100, 750)
    overlap = True
    wall = Wall(x, y)
    while overlap:
        overlap = False
        for i in wall_group:
            x = random.randint(100, 800)
            y = random.randint(100, 750)
            wall = Wall(x, y)
            if pygame.sprite.collide_rect(wall, i):
                overlap = True
        coords.append([x, y])
    wall_group.add(wall)