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
#이벤트루프
running = True # 게임이 진행중인가 여부
while running:
    for event in pygame.event.get(): # 어떤ㅇ ㅣ벤트가 발생했는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가발생하였는가 ? 
            running = False # 게임이 진행중이 아니다.
    #screen.fill((0,0,255)) #화면 채우기 (RGB값)
    screen.blit(background,(0,0)) #배경 그리기
    
    pygame.display.update() # 게임 화면 다시 그리기
    
#게임이종료됐을경우
pygame.quit()
