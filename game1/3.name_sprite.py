import pygame

pygame.init() #초기화작업

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("EungJeom Game")


#배경 이미지 불러오기
background = pygame.image.load("C:/Users/CKIRUser/Desktop/background.png")

#캐릭터(스프라이트) 불러오기
character =pygame.image.load("C:/Users/CKIRUser/Desktop/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터가로크기
character_height= character_size[1] # 캐릭터세로크기
character_x_pos = screen_width / 2 -35 # 화면 가로의 절반에 해당하는 곳에 위치
character_y_pos = screen_height-70  # 화면 세로 가장 아래에 위치

#이벤트루프
running = True # 게임이 진행중인가 여부
while running:
    for event in pygame.event.get(): # 어떤ㅇ ㅣ벤트가 발생했는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가발생하였는가 ? 
            running = False # 게임이 진행중이 아니다.
    screen.blit(background,(0,0)) #배경 그리기

    screen.blit(character,(character_x_pos,character_y_pos))
    
    pygame.display.update() # 게임 화면 다시 그리기
    
#게임이종료됐을경우
pygame.quit()
