import pygame

pygame.init() #초기화작업

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("EungJeom Game")

#FPS
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/CKIRUser/Desktop/game1/background.png")

#캐릭터(스프라이트) 불러오기
character =pygame.image.load("C:/Users/CKIRUser/Desktop/game1/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터가로크기
character_height= character_size[1] # 캐릭터세로크기
character_x_pos = screen_width / 2 -35 # 화면 가로의 절반에 해당하는 곳에 위치
character_y_pos = screen_height-70  # 화면 세로 가장 아래에 위치

#이동할 좌표

to_x = 0
to_y = 0
#이동속도
character_speed = 0.6

#이벤트루프
running = True # 게임이 진행중인가 여부
while running:
    dt = clock.tick(30) # 게임화면 초당 프레임 30
    #print("fps : " + str(clock.get_fps())) 
    for event in pygame.event.get(): # 어떤ㅇ ㅣ벤트가 발생했는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가발생하였는가 ? 
            running = False # 게임이 진행중이 아니다.

        if event.type == pygame.KEYDOWN : # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT : #캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key ==pygame.K_RIGHT : #캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key ==pygame.K_UP : #캐릭터를 위쪽으로
                to_y -= character_speed
            elif event.key ==pygame.K_DOWN : #캐릭터를 아래쪽으로
                to_y += character_speed
        if event.type == pygame.KEYUP : # 방향키를 뗴면 멈춤
            if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key ==pygame.K_DOWN:
                to_y = 0
    character_x_pos +=to_x *dt
    character_y_pos +=to_y * dt

    # 가로 경계값처리
    if character_x_pos <0:
        character_x_pos=0
    elif character_x_pos > screen_width- character_width:
        character_x_pos=screen_width - character_width
     # 세로 경계값처리
    if character_y_pos <0:
        character_y_pos=0
    elif character_y_pos > screen_height- character_height:
        character_y_pos=screen_height - character_height
              
            
    screen.blit(background,(0,0)) #배경 그리기

    screen.blit(character,(character_x_pos,character_y_pos)) #캐릭터그리기 
    
    pygame.display.update() # 게임 화면 다시 그리기
    
#게임이종료됐을경우
pygame.quit()
