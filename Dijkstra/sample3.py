import pygame
import sys
import os
import tkinter as tk
import random
from pygame.locals import QUIT, KEYDOWN, K_UP,K_DOWN,K_SPACE,K_a,Rect



def visited() :
    # 새 창 설정
    new_window_width, new_window_height = 800, 600
    new_window = pygame.display.set_mode((new_window_width, new_window_height))
    pygame.display.set_caption("새로운 창")

    new_window.fill(white)  # 새 창을 흰색으로 채우기
    pygame.display.flip()  # 화면 업데이트
    pygame.time.delay(5000)  # 1초 동안 대기
    new_window.fill(black)  # 새 창을 검은색으로 채우기
    pygame.display.flip()  # 화면 업데이트

class Draw:
    def __init__(self,col,rect,speed = 0):
        self.col = col
        self.rect = rect
        self.speed = speed
    def move(self):
        self.rect.centerx += self.speed
    def draw_E(self):
        pygame.draw.ellipse(SURFACE,self.col,self.rect)
    def draw_R(self):
        pygame.draw.rect(SURFACE,self.col,self.rect)


def Game_Border():
    Start_Point = [(100,150),(100,150),(100,550),(900,150)]
    End_Point = [(100,550),(900,150),(900,550),(900,550)]
    for index in range(len(Start_Point)):
        pygame.draw.line(SURFACE,(255,255,255),Start_Point[index],End_Point[index])

def shot():
    rock_speed = -5
    RockWIDTH = 50
    RockHEIGHT = 50
    xpos = 880
    ypos = random.randint(0,8)
    Rock = []
    game_start = False
    Miss = 0
    Score = 0
    Beam_Count = 0
    Cir = Draw((255, 255, 255), Rect(50,300, 30,30))
    Beam = Draw((255, 255, 0), Rect(Cir.rect.centerx, Cir.rect.centery, 5, 5), 10)
    while True:
        message_Title = Big_font.render("SHOOT_GAME", True, (255, 255, 255))  # 게임제목 적기
        message_Score = Small_font.render("Score: {}".format(Score), True, (255, 255, 255))  # 스코어
        message_Miss = Small_font.render("Miss_Point: {}".format(Miss), True, (255, 255, 255))  # 놓친장애물수
        message_game_start = Small_font.render("Game_start : Click the Space_Bar", True, (255, 255, 255))  # 게임시작
        message_game_over = Big_font.render("Game_over_Score : {}".format(Score), True, (255, 255, 255))  # 게임오버
        message_caution = Small_font.render("Missile_Button : A , Missile is only one ", True, (255, 255, 255))
        SURFACE.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    rock_speed = -5
                    Miss = 0
                    Score = 0
                    game_start = True
                elif event.key == K_UP:
                    Cir.rect.centery -= 10
                elif event.key == K_DOWN:
                    Cir.rect.centery += 10
                elif event.key == K_a:
                    if Beam_Count == 0:
                        Beam_Count =1
                        Beam.rect.center = Cir.rect.center
                    else:
                        Beam.draw_E()
                        #Beam.move() a를 계속 누르고 잇으면 빔속도가 빨라진다.
        if  game_start:
            SURFACE.blit(message_Title, (350, 20))  # 화면상에 제목 표시
            SURFACE.blit(message_Score, (750, 160))  # 화면상에 스코어 표시
            SURFACE.blit(message_caution,(280,100)) #화면상에 주의사항 표시
            SURFACE.blit(message_Miss,(700,200)) #놓친블럭수 표시
            Game_Border()
            Cir.draw_E()

            if Cir.rect.centery <= 170:
                Cir.rect.centery = 170
            elif Cir.rect.centery >= 530:
                Cir.rect.centery = 530

            if Beam_Count == 1:
                Beam.draw_E()
                Beam.move()
                if Beam.rect.centerx >= 900:
                    Beam.rect.center = Cir.rect.center
                    Beam_Count = 0

            if len(Rock) == 0:
                Rock.append(Draw((0, 255, 0), Rect(xpos, ypos * 40 + 170, RockWIDTH - ypos*3 , RockHEIGHT - ypos*3), rock_speed))
            elif len(Rock) ==1:
                Rock[0].draw_R()
                Rock[0].move()
                if Rock[0].rect.colliderect(Beam.rect):
                    Beam.rect.center = Cir.rect.center
                    Beam_Count = 0
                    Score +=100
                    rock_speed -=0.25
                    del Rock[0]
                    ypos = random.randint(0, 8)
                elif Rock[0].rect.centerx <= 100:
                    Beam.rect.center = Cir.rect.center
                    Beam_Count = 0
                    Miss +=1
                    del Rock[0]
                    ypos = random.randint(0, 8)
            if Miss == 3:
                game_start = False

        elif not game_start and Miss ==3:
            SURFACE.blit(message_game_over, (250, 200))
            SURFACE.blit(message_game_start, (300, 300))
        else:
            SURFACE.blit(message_Title, (320, 200))
            SURFACE.blit(message_game_start, (300, 300))

        pygame.display.update()
        FPSCLOCK.tick(30)




# 파이게임 초기화
pygame.init()

# 화면 설정
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("파이게임 시작 화면")



# 색상 정의
white = (255, 255, 255)
black = (0, 0, 0)

# 시작 화면 텍스트
font = pygame.font.Font(None, 36)
text = font.render("Press Spacebar to Start", True, black)
text_rect = text.get_rect(center=(width // 2, height // 2))

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "image")
# 두 번째 화면 이미지
second_screen_image = pygame.image.load(os.path.join(image_path, "map.jpg"))
scaled_width, scaled_height = 800, 600
second_screen_image = pygame.transform.scale(second_screen_image, (scaled_width, scaled_height))
second_screen_rect = second_screen_image.get_rect()

player_pos_x = 402
player_pos_y = 105

rect_x, rect_y = width // 2, height // 2
rect_width, rect_height = 60, 60

# 이벤트 루프
start_screen = True
while start_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start_screen = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            start_screen = False  # 스페이스바를 누르면 시작 화면 종료

    # 화면을 흰색으로 채우기
    screen.fill(white)

    # 시작 화면 텍스트 그리기
    screen.blit(text, text_rect)

    # 화면 업데이트
    pygame.display.flip()

# 두 번째 화면 설정
second_screen = True

# 이벤트 루프 (두 번째 화면)
while second_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            second_screen = False


    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        player_pos_x -= 0.3
    
    if key_event[pygame.K_RIGHT]:
        player_pos_x += 0.3

    if key_event[pygame.K_UP]:
        player_pos_y -= 0.3
    
    if key_event[pygame.K_DOWN]:
        player_pos_y += 0.3

    if key_event[pygame.K_a]:
        current_x, current_y = player_pos_x, player_pos_y
        if (rect_x - 320 <= current_x <= rect_x - 260) and (rect_y - 10 <= current_y <= rect_y + 50):
            pygame.key.set_repeat(15,15)
            SURFACE = pygame.display.set_mode((1000,600))
            FPSCLOCK = pygame.time.Clock()
            Big_font = pygame.font.SysFont(None, 80)
            Small_font = pygame.font.SysFont(None, 40)
            shot()


    # 화면에 이미지 표시
    screen.blit(second_screen_image, second_screen_rect)

    

    pygame.draw.rect(screen, black, (rect_x - 320, rect_y - 10, rect_width, rect_height))
    
    pygame.draw.circle(screen, (255, 255, 255), (player_pos_x, player_pos_y), 20)
    
    # 화면 업데이트
    pygame.display.flip()

# 파이게임 종료
pygame.quit()
sys.exit()




