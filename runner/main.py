import pygame as pg
pg.init()  # starting point of pygame, thats why it should be at the start

width = 800
height = 400
running = True

pg.display.set_caption("Runner")
clock = pg.time.Clock()
sky = pg.image.load('assets/graphics/Sky.png')
ground = pg.image.load('assets/graphics/ground.png')
text = pg.font.Font('assets/font/Pixeltype.ttf', 50)
text_surf = text.render('Runner',False, 'Purple')

snail = pg.image.load('assets/graphics/snail/snail1.png')
snail_x_pos = 730

#player stand
player = pg.image.load('assets/graphics/Player/player_stand.png')
player_rect = player.get_rect(midbottom = (80,200))

screen = pg.display.set_mode((width, height))

while running:
    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    #draw
    screen.blit(sky, (0,0))
    screen.blit(ground, (0,300))
    screen.blit(text_surf, (350,50))

    snail_x_pos -= 4
    if snail_x_pos < -100:
        snail_x_pos = 800
    screen.blit(snail, (snail_x_pos, 265))

    screen.blit(player, player_rect)

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