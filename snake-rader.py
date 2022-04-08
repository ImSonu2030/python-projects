from tkinter.constants import ON
import pygame
import random

from pygame.time import Clock
pygame.init()

#Screen Resolution
screen_width= 1200
screen_hieght=1000

#Window Color(R G B)
white = (255,255,255)
red = (255,0,0,)
black = (0,0,0)

#Game Window
gameWindow=pygame.display.set_mode((screen_width,screen_hieght))
pygame.display.set_caption("Feed The Snake")
pygame.display.update()  #Updating all changes on the window

font = pygame.font.SysFont("BAZOOKA",50)

#Function to print the Score
def screen_text(txt,color,place_x,place_y):
    text_onscreen=font.render(txt,True,color)
    gameWindow.blit(text_onscreen,[place_x,place_y])

def snake(gamewindow,color,snake_list,snake_size,snake_width,snake_rad,snake_face1,sanke_face2):
    for x,y in snake_list:
        pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size],snake_width,snake_rad,snake_face1,sanke_face2)

def highScore(txt,color,place_x,place_y):
    text_onscreen2=font.render(txt,True,color)
    gameWindow.blit(text_onscreen2,[place_x,place_y])

def Home_window():
    exit_game=False
    while not exit_game:
        gameWindow.fill((32,32,32))
        screen_text("Welcome To Feed The Snake",white,380,450)
        screen_text("Press space to Start Game",white,400,500)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameLoop()
        pygame.display.update()
    

def gameLoop():
    #Game Spesific Variable
    exit_game=False
    game_over=False
    snake_x=400
    snake_y=400
    snake_size=20
    velocity_x=0
    velocity_y=0
    score=0
    with open("game_highScore.txt","r") as f:
        h_Score=f.read()
    
    fps=50
    snake_rad=2
    snake_rightface=-5
    snake_leftface=-5
    food_x=random.randint(20,screen_width/2)
    food_y=random.randint(20,screen_hieght/2)
    food_radius=10
    clock = pygame.time.Clock()
    snake_list=[]
    snake_len=1
    
    #Run Game
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            screen_text("Game Over Press Enter to Continue",red,300,400)
            screen_text("High Score "+str(h_Score),red,10,10)
            screen_text("Your Score "+str(score),black,450,500)
            with open("game_highScore.txt","w") as f:
                f.write(str(h_Score))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        Home_window()
                        
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                    with open("game_highScore.txt","w") as f:
                        f.write(str(h_Score))

                #Snake Movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 5
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -5
                        velocity_y = 0

                    if event.key==pygame.K_UP:
                        velocity_y=-5
                        velocity_x=0

                    if event.key==pygame.K_DOWN:
                        velocity_y=5
                        velocity_x=0
            snake_x += velocity_x
            snake_y += velocity_y

            #Snake and Food Collisoin
            if abs(snake_x-food_x)<20 and abs(snake_y-food_y)<20:
                score+=5
                food_x=random.randint(20,screen_width/2)
                food_y=random.randint(20,screen_hieght/2)
                snake_len+=5

            if int(h_Score)>=score:
                pass
            elif int(h_Score)<score:
                h_Score=score

            pygame.display.update()
            gameWindow.fill(white)
            
            screen_text("High Score "+str(h_Score),red,200,20)
            screen_text("Score "+str(score),black,500,20)
            pygame.draw.circle(gameWindow,red,(food_x,food_y),food_radius)

            '''
            if int(h_Score)<=score:
                highScore("High Score "+str(h_Score),red,200,20)    
            elif int(h_Score)>score:
                h_Score=score
                highScore("High Score "+str(h_Score),red,200,20)
            '''   
            
            snake_head=[]
            snake_head.append(snake_x)
            snake_head.append(snake_y)
            snake_list.append(snake_head)
            if len(snake_list)>snake_len:
                del snake_list[0]

            #Collision With Snake 
            if snake_head in snake_list[:-1]:
                game_over=True
            #Snake Collision
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_hieght:
                game_over=True
            snake(gameWindow,black,snake_list,snake_size,0,snake_rad,snake_rightface,snake_leftface)
            
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()


Home_window()
