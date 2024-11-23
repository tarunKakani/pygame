import pygame as pg
#.convert_alpha() not working
pg.init()  # starting point of pygame, thats why it should be at the start

width = 800
height = 400
running = True

pg.display.set_caption("Runner")
clock = pg.time.Clock()
sky = pg.image.load('runner/assets/graphics/Sky.png')
ground = pg.image.load('runner/assets/graphics/ground.png')
text = pg.font.Font('runner/assets/font/Pixeltype.ttf', 50)
text_surf = text.render('Runner',False, 'Purple')

#snail 
snail = pg.image.load('runner/assets/graphics/snail/snail1.png')
snail_rect = snail.get_rect(midbottom = (730,300))

#player stand
player = pg.image.load('runner/assets/graphics/Player/player_walk_1.png')
player_rect = player.get_rect(midbottom = (80,300)) #same position as ground

screen = pg.display.set_mode((width, height))

while running:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    #draw
    screen.blit(sky, (0,0))
    screen.blit(ground, (0,300))
    screen.blit(text_surf, (350,50))

    # my way
    # snail_rect[0] -= 4
    # if snail_rect[0] < -100:
    #     snail_rect[0] = 800
    
    # more control on points
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800

    screen.blit(snail, snail_rect)
    screen.blit(player, player_rect)

    # collision
    # if player_rect.colliderect(snail_rect):
    #     print("Collision")


    

    # keys = pg.key.get_pressed()
    # if keys[pg.k_w]:
    #     pass
    # if keys[pg.k_s]:
    #     pass
    # if keys[pg.k_d]:
    #     pass
    # if keys[pg.k_a]:
    #     pass


    #update
    pg.display.update()

    clock.tick(60)
    # dt = clock.tick(60)/1000 # 60 frames per second

pg.quit()