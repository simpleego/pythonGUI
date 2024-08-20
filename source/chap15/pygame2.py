import pygame
import sys
import random

# 게임 화면 크기
screen_width = 800
screen_height = 600

# 색상 정의
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# 플레이어 클래스
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #self.image = pygame.Surface((50, 50))
        #self.image.fill(green)
        self.image = pygame.image.load("spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 10
        self.speed_x = 0

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width

# 스프라이트 그룹 생성
all_sprites = pygame.sprite.Group()
# 플레이어 생성
player = Player()
all_sprites.add(player)

# 게임 화면 생성
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Invader")
# 게임 루프
clock = pygame.time.Clock()

# 게임 루프
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.speed_x = -5
            elif event.key == pygame.K_RIGHT:
                player.speed_x = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.speed_x = 0
    # 화면 업데이트
    all_sprites.update()
    screen.fill(black)
    # 스프라이트 그룹을 화면에 그리기
    all_sprites.draw(screen)
    # 화면 업데이트
    pygame.display.flip()
    # FPS 설정 (60FPS)
    clock.tick(60)
pygame.quit()
