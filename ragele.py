import pygame
import sys
import random

# Ekran boyutları
WIDTH, HEIGHT = 800, 600

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Oyuncu sınıfı
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT-50))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        self.rect.x = max(0, min(WIDTH - 50, self.rect.x))

# Düşman sınıfı
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(center=(random.randint(0, WIDTH), 0))
        self.speed = random.randint(1, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.y = 0
            self.rect.x = random.randint(0, WIDTH)

# Oyun başlatma fonksiyonu
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player = Player()
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    enemy_frequency = 0
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        enemy_frequency += 1
        if enemy_frequency > 30:
            enemy_frequency = 0
            enemy = Enemy()
            enemies.add(enemy)
            all_sprites.add(enemy)

        all_sprites.update()

        # Çarpışmaları kontrol et
        hits = pygame.sprite.spritecollide(player, enemies, True)
        for hit in hits:
            score += 1
            print("Score:", score)

        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()

