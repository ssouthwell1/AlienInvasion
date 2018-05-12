import sys

import pygame

from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

            # NEED TO REFACTOR THIS METHOD WITH FLAGGED EVENTS FOR THE KEY PRESSES

        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        # elif event.key == pygame.K_UP:
        #     ship.rect.bottom -= 1
        # elif event.key == pygame.K_DOWN:
        #     # Update this to check and make sure the ship is not already at the bottom of the screen
        #     ship.rect.bottom += 1


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to key presses"""
    if event.key == pygame.K_RIGHT:
        print("Value before right key down: " + str(ship.moving_right))
        ship.moving_right = True
        print("Value after right key down: " + str(ship.moving_right))
    if event.key == pygame.K_LEFT:
        print("Value before left key down: " + str(ship.moving_left))
        ship.moving_left = True
        print("Value after left key down: " + str(ship.moving_left))
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullets_allowed:
            print("Firing new bullet")
            new_bullet = Bullet(ai_settings, screen, ship)
            new_bullet.sound_shoot.play()
            bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Respond to key releases"""
    if event.key == pygame.K_RIGHT:
        print("Value before right key up: " + str(ship.moving_right))
        ship.moving_right = False
        print("Value after right key up: " + str(ship.moving_right))
    if event.key == pygame.K_LEFT:
        print("Value before left key up: " + str(ship.moving_left))
        ship.moving_left = False
        print("Value after left key up: " + str(ship.moving_left))


def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    pygame.display.flip()


def update_bullets(bullets):
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            print(len(bullets))
