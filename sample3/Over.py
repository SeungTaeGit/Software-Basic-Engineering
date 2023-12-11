import pygame
from pygame.locals import QUIT, KEYDOWN, K_UP,K_DOWN,K_SPACE,K_a,Rect
import tkinter as tk
from tkinter import messagebox
from Brainer import *
from NoBrainer import *
from Back import *



### 쓰레기 파일



# 게임 오버 텍스트 추가
gameover_font = pygame.font.Font(pygame.font.match_font('Arial'), 20)
gameover_text = gameover_font.render('GAME OVER',True,(255,0,0))
 
# Gameover 텍스트의 사이즈 가져오기 (화면 가운데 배치시키기 위해)
size_text_width = gameover_text.get_rect().size[0]
size_text_height = gameover_text.get_rect().size[1]
 
# gameover의 좌표를 화면 가운데 배치
x_pos_gameover = scaled_width/2-size_text_width/2
y_pos_gameover = scaled_height/2-size_text_height/2


# 게임 오버 함수
def over():
    screen.blit(gameover_text, (x_pos_gameover, y_pos_gameover))
    pygame.display.update()
    pygame.time.delay(2000) # 약 2초동안 GAME OVER 화면 유지
    second_screen = False