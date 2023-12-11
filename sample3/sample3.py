import pygame
import sys
import os
import random
from pygame.locals import QUIT, KEYDOWN, K_UP,K_DOWN,K_SPACE,K_a,Rect
import tkinter as tk
from tkinter import messagebox
from Brainer import *
from NoBrainer import *
from Back import *
from Description import *



# 다익스크라 경로 답
ANS = ['House', 'Salon', 'Market', 'Academy', 'Restaurant', 'Bank', 'School']
p = 1
p = int(p)
result = 0

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



def over(): 
    pygame.quit()
    sys.exit()


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


Des()


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

        # 미용실
        if (rect_x - 320 <= current_x <= rect_x - 260) and (rect_y - 10 <= current_y <= rect_y + 50):
            if (ANS[p] == 'Salon') :
                messagebox.showinfo("경로 확인", "경로 선택 성공")
                success()
                result = back2()
                p = p + result
                print(p)
                result = 0
            else :
                messagebox.showinfo("경로 확인", "경로 선택 실패")
                fail()
        # 슈퍼마켓
        elif (rect_x - 40 <= current_x <= rect_x + 40) and (rect_y - 80 <= current_y <= rect_y - 20):
            if (ANS[p] == 'Market') :
                messagebox.showinfo("경로 확인", "경로 선택 성공")
                success()
                result = back2()
                p = p + result
                print(p)
                result = 0
            else :
                messagebox.showinfo("경로 확인", "경로 선택 실패")
                fail()
        # 학원
        elif (rect_x + 230 <= current_x <= rect_x + 300) and (rect_y - 110 <= current_y <= rect_y - 20):
            if (ANS[p] == 'Academy') :
                messagebox.showinfo("경로 확인", "경로 선택 성공")
                success()
                result = back2()
                p = p + result
                print(p)
                result = 0
            else :
                messagebox.showinfo("경로 확인", "경로 선택 실패")
                fail()
        # 레스토랑
        elif (rect_x - 140 <= current_x <= rect_x - 70) and (rect_y + 50 <= current_y <= rect_y + 110):
            if (ANS[p] == 'Restaurant') :
                messagebox.showinfo("경로 확인", "경로 선택 성공")
                success()
                result = back2()
                p = p + result
                print(p)
                result = 0
            else :
                messagebox.showinfo("경로 확인", "경로 선택 실패")
                fail()
        # 은행
        elif (rect_x - 30 <= current_x <= rect_x + 70) and (rect_y + 150 <= current_y <= rect_y + 230):
            if (ANS[p] == 'Bank') :
                messagebox.showinfo("경로 확인", "경로 선택 성공")
                success()
                result = back2()
                p = p + result
                print(p)
                result = 0
            else :
                messagebox.showinfo("경로 확인", "경로 선택 실패")
                fail()
        # 학교
        elif (rect_x + 190 <= current_x <= rect_x + 285) and (rect_y + 100 <= current_y <= rect_y + 180):
            if (ANS[p] == 'School') :
                messagebox.showinfo("경로 확인", "경로 선택 성공")
                success()
                result = back2()
                p = p + result
                print(p)
                result = 0
                messagebox.showinfo("Game clear", "Congratulations !")
                pygame.quit()
                sys.exit()
            else :
                messagebox.showinfo("경로 확인", "경로 선택 실패")
                fail()

    # 화면에 이미지 표시
    screen.blit(second_screen_image, second_screen_rect)

    
    # 노드 좌표
    #pygame.draw.rect(screen, black, (rect_x - 320, rect_y - 10, rect_width, rect_height))              # 미용실
    #pygame.draw.rect(screen, black, (rect_x - 40, rect_y - 80, rect_width + 20, rect_height))          # 슈퍼마켓
    #pygame.draw.rect(screen, black, (rect_x + 230, rect_y - 110, rect_width + 10, rect_height + 30))   # 학원
    #pygame.draw.rect(screen, black, (rect_x - 140, rect_y + 50, rect_width + 10, rect_height))         # 레스토랑
    #pygame.draw.rect(screen, black, (rect_x - 30, rect_y + 150, rect_width + 10, rect_height + 20))    # 은행
    #pygame.draw.rect(screen, black, (rect_x + 190, rect_y + 100, rect_width + 35, rect_height + 20))   # 학교

    # 플레이어 좌표
    pygame.draw.circle(screen, (255, 255, 255), (player_pos_x, player_pos_y), 15)
    
    # 화면 업데이트
    pygame.display.flip()

# 파이게임 종료
pygame.quit()
sys.exit()

