import sys

import pygame

from bullet import Bullet

from aliens.alien import Alien

from aliens.green_alien import GreenAlien

from aliens.red_alien import RedAlien

from aliens.blue_alien import BlueAlien

from explosions.explosion import Explosion


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
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(ai_settings, screen, ship, aliens, bullets):
    # screen.fill(ai_settings.bg_color)
    screen.blit(ai_settings.bg_image, [0, 0])

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(ai_settings, bullets, aliens, screen):
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            print(len(bullets))
    check_collisions(ai_settings, bullets, aliens, screen)


def check_collisions(ai_settings, bullets, aliens, screen):
    aliencollisiondict = pygame.sprite.groupcollide(bullets, aliens, True, False)
    for values in aliencollisiondict.values():
        for current_alien in values:
            ai_settings.sound_explosion.play()
            if isinstance(current_alien, BlueAlien):
                # after alien is hit, draw the explosion then remove the alien from the group
                # current_alien.image = pygame.transform.scale(pygame.image.load('images/blue_explosion.png'),
                #                                              (ai_settings.alien_width, ai_settings.alien_height))
                explosion = Explosion(ai_settings, current_alien, screen)
                aliens.add(explosion)
                aliens.remove(current_alien)
            elif isinstance(current_alien, RedAlien):
                print("Red Alien hit!")
                aliens.remove(current_alien)
            elif isinstance(current_alien, GreenAlien):
                print("Green Alien hit!")
                current_alien.image = pygame.transform.scale(pygame.image.load('images/green_explosion.png'),
                                                             (ai_settings.alien_width, ai_settings.alien_height))
                aliens.remove(current_alien)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        print("Firing new bullet")
        new_bullet = Bullet(ai_settings, screen, ship)
        new_bullet.sound_shoot.play()
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row"""
    available_space_x = ai_settings.screenwidth - 2 * alien_width
    number_aliens_x = int(available_space_x / (1.5 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screenheight - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row depending on its type"""
    if row_number == 0 or row_number == 1:
        alien_green = GreenAlien(ai_settings, screen)
        alien_width = alien_green.rect.width
        alien_green.x = (alien_width * 3) + (65 * alien_number)
        alien_green.rect.x = alien_green.x
        alien_green.rect.y = alien_green.rect.height + (60 * row_number)
        aliens.add(alien_green)

    elif row_number == 2 or row_number == 3:
        alien_red = RedAlien(ai_settings, screen)
        alien_width = alien_red.rect.width
        alien_red.x = (alien_width * 3) + (65 * alien_number)
        alien_red.rect.x = alien_red.x
        alien_red.rect.y = alien_red.rect.height + (60 * row_number)
        aliens.add(alien_red)

    elif row_number == 4:
        alien_blue = BlueAlien(ai_settings, screen)
        alien_width = alien_blue.rect.width
        alien_blue.x = (alien_width * 3) + (65 * alien_number)
        alien_blue.rect.x = alien_blue.x
        alien_blue.rect.y = alien_blue.rect.height + (60 * row_number)
        aliens.add(alien_blue)


def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens"""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    # number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(5):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drop entire fleet and change the fleet's direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, aliens):
    """Check if the fleet is at an edge,
     and then update the positions of all aliens in the fleet"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

# def reset_time():
