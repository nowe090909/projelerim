import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aksiyon Oyunu")

player_img = pygame.image.load("player.png")
player_img = pygame.transform.scale(player_img, (50, 50))
bullet_img = pygame.image.load("bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (10, 10))
enemy_img = pygame.image.load("enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (50, 50))

player_x, player_y = WIDTH // 2, HEIGHT - 100
player_vel = 5
bullets = []

enemies = []
enemy_vel = 3
enemy_spawn_rate = 30
enemy_spawn_counter = 0

score = 0
font = pygame.font.Font(None, 36)

def draw_window():
    win.fill((0, 0, 0))
    win.blit(player_img, (player_x, player_y))
    for bullet in bullets:
        win.blit(bullet_img, (bullet[0], bullet[1]))
    for enemy in enemies:
        win.blit(enemy_img, (enemy[0], enemy[1]))
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    win.blit(text, (10, 10))
    pygame.display.update()

def move_player():
    global player_x, player_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_vel
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_img.get_width():
        player_x += player_vel

def move_bullets():
    global bullets
    bullets = [(bullet[0], bullet[1] - 5) for bullet in bullets if bullet[1] > 0]

def spawn_enemies():
    global enemies, enemy_spawn_counter
    if enemy_spawn_counter == 0:
        enemy_x = random.randint(0, WIDTH - enemy_img.get_width())
        enemy_y = -enemy_img.get_height()
        enemies.append((enemy_x, enemy_y))
        enemy_spawn_counter = enemy_spawn_rate
    else:
        enemy_spawn_counter -= 1

def move_enemies():
    global enemies, score
    enemies = [(enemy[0], enemy[1] + enemy_vel) for enemy in enemies]
    enemies = [enemy for enemy in enemies if enemy[1] < HEIGHT]
    for enemy in enemies:
        if pygame.Rect(player_x, player_y, player_img.get_width(), player_img.get_height()).colliderect(pygame.Rect(enemy[0], enemy[1], enemy_img.get_width(), enemy_img.get_height())):
            game_over()
        for bullet in bullets:
            if pygame.Rect(bullet[0], bullet[1], bullet_img.get_width(), bullet_img.get_height()).colliderect(pygame.Rect(enemy[0], enemy[1], enemy_img.get_width(), enemy_img.get_height())):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1

def game_over():
    pygame.quit()
    sys.exit()

clock = pygame.time.Clock()
run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullets.append((player_x + player_img.get_width() // 2, player_y))

    move_player()
    move_bullets()
    spawn_enemies()
    move_enemies()
    draw_window()

pygame.quit()
sys.exit()