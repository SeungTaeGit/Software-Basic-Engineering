import sys
import pygame
from pygame.locals import QUIT, Rect
import time
import os

pygame.init()
surface = pygame.display.set_mode((420, 430))
fpsclock = pygame.time.Clock()
pygame.display.set_caption('Find shortest instance')

player_rect = Rect(200, 400, 30, 30)
player_speed = 5

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "image")

walls = [
    Rect(0, 0, 220, 30),
    Rect(250, 0, 160, 30),
    Rect(0, 0, 30, 380),
    Rect(390, 0, 30, 380),
    Rect(0, 380, 200, 30),
    Rect(230, 380, 190, 30),
    Rect(170, 400, 30, 30),
    Rect(230, 400, 30, 30),
    Rect(90, 60, 130, 60),
    Rect(250, 60, 100, 60),
    Rect(280, 100, 10, 100),
    Rect(30, 60, 30, 140),
    Rect(90, 150, 160, 50),
    Rect(60, 300, 110, 50),
    Rect(200, 300, 80, 50),
    Rect(310, 300, 50, 50),
    Rect(60, 230, 200, 40),
    Rect(290, 60, 70, 210),
]
# 폰트 지정
font = pygame.font.Font(pygame.font.match_font('Arial'), 20)

# 벽과 충돌하는지 확인
def check(player_rect, walls):
    for wall in walls:
        if player_rect.colliderect(wall):
            return True
    return False

def show_shortest_path():
    # 새로운 창 생성
    new_window = pygame.display.set_mode((480, 480))
    new_window.fill((255, 255, 255))

    # 로딩 이미지 표시 및 축소
    loading_image = pygame.image.load(os.path.join(image_path, "maze.jpg"))
    loading_image = pygame.transform.scale(loading_image, (430, 430))  # 원하는 크기로 조절
    loading_rect = loading_image.get_rect(center=(240, 240))
    new_window.blit(loading_image, loading_rect)

    # 텍스트 표시
    font = pygame.font.Font(pygame.font.match_font('Arial'), 20)
    text = font.render("here is the shortest path  [1-4-3-1-3-5-7 SUM = 24] ", True, (0, 0, 0))
    text_rect = text.get_rect(center=(230, 10))
    new_window.blit(text, text_rect)

    pygame.display.flip()  # 변경 사항을 적용
    time.sleep(5)  # 이미지를 보여주기 위해 잠시 대기

def main():
    game_over_flag = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # 플레이어 이탈방지 함수
        if not game_over_flag:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_rect.left > 0:
                player_rect.x -= player_speed
                if check(player_rect, walls):
                    player_rect.x += player_speed
            if keys[pygame.K_RIGHT] and player_rect.right < 430:
                player_rect.x += player_speed
                if check(player_rect, walls):
                    player_rect.x -= player_speed
            if keys[pygame.K_UP] and player_rect.top > 0:
                player_rect.y -= player_speed
                if check(player_rect, walls):
                    player_rect.y += player_speed
            if keys[pygame.K_DOWN] and player_rect.bottom < 430:
                player_rect.y += player_speed
                if check(player_rect, walls):
                    player_rect.y -= player_speed

            # 플레이어가 게임 오버 지점에 도달하면 게임 오버 상태로 전환
            if player_rect.x == 220 and player_rect.y == 0:
                game_over_flag = True

        surface.fill((255, 255, 255))

        # 숫자 표시 (최하단좌측부터(0))
        number = font.render("1", True, (0, 0, 0))
        number_rect = number.get_rect(center=(195, 365))
        surface.blit(number, number_rect)
        
        number = font.render("2", True, (0, 0, 0))
        number_rect = number.get_rect(center=(230, 365))
        surface.blit(number, number_rect)

        # 숫자 표시 (최하단좌측부터(1))
        number = font.render("5", True, (0, 0, 0))
        number_rect = number.get_rect(center=(45, 325))
        surface.blit(number, number_rect)

        number = font.render("4", True, (0, 0, 0))
        number_rect = number.get_rect(center=(185, 325))
        surface.blit(number, number_rect)
        
        number = font.render("8", True, (0, 0, 0))
        number_rect = number.get_rect(center=(295, 325))
        surface.blit(number, number_rect)
        
        number = font.render("3", True, (0, 0, 0))
        number_rect = number.get_rect(center=(375, 325))
        surface.blit(number, number_rect)

        # 숫자 표시 (최하단좌측부터(2))
        number = font.render("3", True, (0, 0, 0))
        number_rect = number.get_rect(center=(120, 285))
        surface.blit(number, number_rect)

        number = font.render("7", True, (0, 0, 0))
        number_rect = number.get_rect(center=(235, 285))
        surface.blit(number, number_rect)
        
        number = font.render("10", True, (0, 0, 0))
        number_rect = number.get_rect(center=(335, 285))
        surface.blit(number, number_rect)

        # 숫자 표시 (최하단좌측부터(3))
        number = font.render("1", True, (0, 0, 0))
        number_rect = number.get_rect(center=(45, 250))
        surface.blit(number, number_rect)

        number = font.render("2", True, (0, 0, 0))
        number_rect = number.get_rect(center=(275, 250))
        surface.blit(number, number_rect)        
        
        number = font.render("20", True, (0, 0, 0))
        number_rect = number.get_rect(center=(375, 250))
        surface.blit(number, number_rect)    

        # 숫자 표시 (최하단좌측부터(4))
        number = font.render("3", True, (0, 0, 0))
        number_rect = number.get_rect(center=(155, 215))
        surface.blit(number, number_rect)

        # 숫자 표시 (최하단좌측부터(5))
        number = font.render("8", True, (0, 0, 0))
        number_rect = number.get_rect(center=(75, 170))
        surface.blit(number, number_rect)

        number = font.render("5", True, (0, 0, 0))
        number_rect = number.get_rect(center=(265, 170))
        surface.blit(number, number_rect)        
        
        # 숫자 표시 (최하단좌측부터(6))
        number = font.render("4", True, (0, 0, 0))
        number_rect = number.get_rect(center=(155, 135))
        surface.blit(number, number_rect)

        # 숫자 표시 (최하단좌측부터(7))
        number = font.render("1", True, (0, 0, 0))
        number_rect = number.get_rect(center=(75, 90))
        surface.blit(number, number_rect)

        number = font.render("7", True, (0, 0, 0))
        number_rect = number.get_rect(center=(235, 90))
        surface.blit(number, number_rect)        
        
        # 숫자 표시 (최하단좌측부터(8))
        number = font.render("10", True, (0, 0, 0))
        number_rect = number.get_rect(center=(155, 45))
        surface.blit(number, number_rect)

        # 빨간색 사각형들 (벽)
        for wall in walls:
            pygame.draw.rect(surface, (255, 0, 0), wall)

        # 파란색 사각형 (플레이어)
        pygame.draw.rect(surface, (0, 0, 255), player_rect)

        if game_over_flag:
            show_shortest_path()  # 최단 경로 표시
            pygame.display.update() # 새로운 화면 갱신
            pygame.time.delay(5000)  # 대기시간
            sys.exit() # 종료

        pygame.display.update()
        fpsclock.tick(60)


if __name__ == "__main__":
    main()