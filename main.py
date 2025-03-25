
import pygame


clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Way')
icon = pygame.image.load('images\\icon.png')
pygame.display.set_icon(icon)


myfont = pygame.font.Font('fonts/Bytesized-Regular.ttf',40)

backg = pygame.image.load('images/backg.jpg').convert()

cat_die = [
    pygame.image.load('images/death/death1.png').convert_alpha(),
    pygame.image.load('images/death/death2.png').convert_alpha(),
    pygame.image.load('images/death/death3.png').convert_alpha(),
    pygame.image.load('images/death/death4.png').convert_alpha(),
]
cat_die_anim_count = 0

soul = [
    pygame.image.load('images/slime/slime1.png').convert_alpha(),
    pygame.image.load('images/slime/slime2.png').convert_alpha(),
    pygame.image.load('images/slime/slime3.png').convert_alpha(),
    pygame.image.load('images/slime/slime4.png').convert_alpha(),
    pygame.image.load('images/slime/slime5.png').convert_alpha(),
    pygame.image.load('images/slime/slime6.png').convert_alpha(),
    pygame.image.load('images/slime/slime7.png').convert_alpha(),
    pygame.image.load('images/slime/slime8.png').convert_alpha(),
]

soul_list_in_game = []
player_idle_right = [
    pygame.image.load('images/idle/idle1.png').convert_alpha(),
    pygame.image.load('images/idle/idle2.png').convert_alpha(),
    pygame.image.load('images/idle/idle3.png').convert_alpha(),
    pygame.image.load('images/idle/idle4.png').convert_alpha(),
]


player_idle_anim_count = 0
walk_right =[
    pygame.image.load('images/walk/Walk1.png').convert_alpha(),
    pygame.image.load('images/walk/Walk2.png').convert_alpha(),
    pygame.image.load('images/walk/Walk3.png').convert_alpha(),
    pygame.image.load('images/walk/Walk4.png').convert_alpha(),
    pygame.image.load('images/walk/Walk5.png').convert_alpha(),
    pygame.image.load('images/walk/Walk6.png').convert_alpha(),
]
walk_left =[
    pygame.image.load('images/walk/Walk12.png').convert_alpha(),
    pygame.image.load('images/walk/Walk11.png').convert_alpha(),
    pygame.image.load('images/walk/Walk10.png').convert_alpha(),
    pygame.image.load('images/walk/Walk9.png').convert_alpha(),
    pygame.image.load('images/walk/Walk8.png').convert_alpha(),
    pygame.image.load('images/walk/Walk7.png').convert_alpha(),
]
player_anim_count = 0
backg_x = 0
soul_anim_count = 0

backg_sound = pygame.mixer.Sound('sounds/backg.mp3')
backg_sound.play()


label = pygame.font.Font('fonts/Dinner Friends.otf',70)
lose_label= label.render('The cat was lost', False, 'White')
restart_label= label.render('Return', False, (76, 173, 91))
Win_label= label.render('The cat returned home', False, 'White')
restart_label_rect = restart_label.get_rect(topleft=(230, 200))


bullets_left = 5
bullet = pygame.image.load('images/star (2).png').convert_alpha()
bullets = []
bullet_speed = 16

SOUL_TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(SOUL_TIMER, 3000)

player_speed = 5
player_x = 150
player_y = 325

soul_x = 650
soul_y = 335

is_jump = False
jump_count = 7

move_direction = walk_right
gameplay = True
running = True
is_moving = False
while running:


    screen.blit(backg, (backg_x, 0))
    screen.blit(backg,(backg_x + 600, 0))

    if gameplay:
        if player_x >= 500:
            screen.blit(Win_label, (115, 100))
        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
        if soul_list_in_game:
            for (i, el) in enumerate(soul_list_in_game):
                screen.blit(soul[soul_anim_count], el)
                el.x -= 10

                if el.x < -10:
                    soul_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    gameplay = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y, ))
        elif keys[pygame.K_RIGHT]:
            screen.blit(walk_right[player_anim_count], (player_x, player_y,))
        else:
            screen.blit(player_idle_right[player_idle_anim_count], (player_x, player_y))






        if keys[pygame.K_LEFT] and player_x > 40:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 590:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -7:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                    is_jump = False
                    jump_count = 7

        if player_anim_count == 5:
            player_anim_count = 0
        else:
            player_anim_count += 1

        if player_idle_anim_count == 3:
            player_idle_anim_count = 0
        else:
            player_idle_anim_count += 1

        if soul_anim_count == 7:
            soul_anim_count = 0
        else:
            soul_anim_count += 1
        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            backg_x -= 2

        if backg_x == -600:
           backg_x = 0

        if bullets:
            for (i, el) in enumerate (bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += bullet_speed

                if el.x > 630:
                    bullets.pop(i)


                if soul_list_in_game:
                    for (index, soul_el) in enumerate (soul_list_in_game):
                        if el.colliderect(soul_el):
                            soul_list_in_game.pop(index)
                            bullets.pop(i)


    else:
        screen.fill((46, 66, 49))
        screen.blit(lose_label, (150, 100))
        screen.blit(restart_label,restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            soul_list_in_game.clear()
            bullets.clear()
            bullets_left = 5

    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == SOUL_TIMER:
            soul_list_in_game.append(soul[soul_anim_count].get_rect(topleft =(soul_x,soul_y)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_b and bullets_left > 0:
            bullets.append(bullet.get_rect(topright=(player_x + 60, player_y + 25)))
            bullets_left -= 1

    clock.tick(10)


























































