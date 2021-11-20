import cv2
import mediapipe as mp
import numpy as np
import random
import pygame
import time

pygame.mixer.init() 

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(1)
cap.set(3, 1200)
cap.set(4, 720)
w,h=cap.get(3),cap.get(4)

qu=0
speed=3

bullet= cv2.imread("res/bullet.png",cv2.IMREAD_UNCHANGED)
girl= cv2.imread("res/girl.jpg",1)
main= cv2.imread("res/main.jpeg",1)
killTitle=cv2.imread('res/killTitle.png',cv2.IMREAD_UNCHANGED)
oldguy= cv2.imread("res/oldguy.jpg",1)
squareSplash= cv2.imread("res/squareSplash.png",cv2.IMREAD_UNCHANGED)
allSplash= cv2.imread("res/allSplash.png",cv2.IMREAD_UNCHANGED)
titleSplash= cv2.imread("res/titleSplash.png",cv2.IMREAD_UNCHANGED)
thumbsup= cv2.imread("res/thumbsup.png",cv2.IMREAD_UNCHANGED)
circle= cv2.imread("res/circle.png",1)
triangle= cv2.imread("res/triangle.png",1)
square= cv2.imread("res/square.png",1)
boss= cv2.imread("res/boss.jpeg",1)
title= cv2.imread("res/title.jpg",1)
title2= cv2.imread("res/title2.png",1)
moneyheap= cv2.imread("res/moneyheap.png",cv2.IMREAD_UNCHANGED)
fallingmoney= cv2.imread("res/fallingmoney.png",cv2.IMREAD_UNCHANGED)
winTitle= cv2.imread("res/win.png",cv2.IMREAD_UNCHANGED)
quit= cv2.imread("res/quit.png",cv2.IMREAD_UNCHANGED)
restart= cv2.imread("res/restart.png",cv2.IMREAD_UNCHANGED)


bullet= cv2.resize(bullet, (40,40))
girl= cv2.resize(girl, (110,75))
main= cv2.resize(main, (70,50))
oldguy= cv2.resize(oldguy, (480,380))
squareSplash= cv2.resize(squareSplash, (500,600))
titleSplash= cv2.resize(titleSplash, (600,300))
allSplash= cv2.resize(allSplash,(500,160))
thumbsup= cv2.resize(thumbsup,(90,100))
boss= cv2.resize(boss, (150,90))
title= cv2.resize(title, (290,190))
title2= cv2.resize(title2, (290,190))
circle= cv2.resize(circle,(63,100))
triangle= cv2.resize(triangle,(63,100))
square= cv2.resize(square,(63,100))
moneyheap= cv2.resize(moneyheap,(500,650))
fallingmoney= cv2.resize(fallingmoney,(360,360))
winTitle= cv2.resize(winTitle,(500,100))
restart= cv2.resize(restart,(450,150))
quit= cv2.resize(quit,(450,150))

girl=cv2.flip(girl, 1)
main=cv2.flip(main, 1)
killTitle=cv2.flip(killTitle, 1)
bullet=cv2.rotate(bullet,cv2.ROTATE_90_CLOCKWISE)
oldguy=cv2.flip(oldguy, 1)
squareSplash=cv2.flip(squareSplash, 1)
allSplash=cv2.flip(allSplash, 1)
titleSplash=cv2.flip(titleSplash,1)
thumbsup=cv2.flip(thumbsup,1)
boss=cv2.flip(boss, 1)
title=cv2.flip(title, 1)
title2=cv2.flip(title2, 1)
winTitle=cv2.flip(winTitle, 1)
restart=cv2.flip(restart, 1)
quit=cv2.flip(quit, 1)

music = pygame.mixer.music.load('res/remix.mp3')
pygame.mixer.music.play(1)
splash=True

def drawCircle():
    return random.randint(13,20),random.randint(50,350),random.randint(50,200)
with mp_hands.Hands(model_complexity=0,min_detection_confidence=0.5,min_tracking_confidence=0.5,max_num_hands
=1) as hands:
    while True:
        
        counter=60
        end=False
        win=False
        start=False
        levelPass=True
        move=True
        rotate=False
        ti=True
        x,y=0,0
        girl_movement=[50*i + x for i, x in enumerate(sorted(random.sample(range(32), 30)))][::2]
        i,j,k=0,0,0
        kill_song=True
        gameMusic=True
        winMusic=True
        i_prev=0
        kill=False
        qu=False
        rest=False
        timeOut=False
        counterColor=(155,50,125)
        while True:
            sT=time.time()
            cv2.waitKey(1) & 0xFF
            _, image = cap.read()
            
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if not splash:
                if gameMusic:
                    music = pygame.mixer.music.load('res/rlgl.mp3')
                    pygame.mixer.music.play(1)
                    gameMusic=False
                image.flags.writeable = True
                
                
                if start and not win and not kill:
                    j+=1
                if not end and not kill:
                    cv2.rectangle(image,(20,20),(370,220),(0,255,0),2)

                if start and levelPass:
                    r,x,y=drawCircle()
                    levelPass=False
                if i%35==0 and i!=0:
                    levelPass=True
            
                if x and y and not end and not kill:
                    cv2.circle(image,(x,y),r,(0,255,0),2)
                
                if i==0:
                    image[5:80,585:695]=girl
                if 670-i>82:
                    image[665-i:715-i,605:675]=main
                else:
                    image[0:360,260:620]=image[0:360,260:620] * (1 - fallingmoney[:, :, 3:] / 255) + fallingmoney[:, :, :3] * (fallingmoney[:, :, 3:] / 255)
                    image[70:720,120:620]=image[70:720,120:620] * (1 - moneyheap[:, :, 3:] / 255) + moneyheap[:, :, :3] * (moneyheap[:, :, 3:] / 255)
                    image[370:470,780:1280]=image[370:470,780:1280] * (1 - winTitle[:, :, 3:] / 255) + winTitle[:, :, :3] * (winTitle[:, :, 3:] / 255)
                    for k,j in zip(np.random.randint(0,1200,10),np.random.randint(0,720,10)):
                        cv2.circle(image,(k,j),random.randint(4,25),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),random.randint(1,6))
                    end=True
                    win=True
                    timeOut=True
                    
                    if winMusic:
                        music = pygame.mixer.music.load('res/end.mp3')
                        pygame.mixer.music.play(1)
                        winMusic=False
                    
                if not end:
                    image[230:320,90:240]=boss

                    image[230:330,1090:1153]=circle
                    image[440:540,1040:1103]=square
                    image[470:570,40:103]=triangle
                    image[5:80,585:695]=girl
                
                if (j>=girl_movement[0] and j<=girl_movement[1] and start) or timeOut:
                    
                    if rotate or timeOut:
                        
                        if i_prev!=i and not end:                 
                            if 650-i>k:
                                kill=True
                                timeOut=True
                                image[20+k:60+k,624:664]=image[20+k:60+k,624:664] * (1 - bullet[:, :, 3:] / 255) + bullet[:, :, :3] * (bullet[:, :, 3:] / 255)
                            image[200:351,200:1089]=image[200:351,200:1089] * (1 - killTitle[:, :, 3:] / 255) + killTitle[:, :, :3] * (killTitle[:, :, 3:] / 255)
                            cv2.line(image,(605,665-i),(675,715-i),(0,0,255),2)
                            cv2.line(image,(605,665-i+50),(675,715-i-50),(0,0,255),2)

                            image[330:710,100:580]=oldguy
                            k+=15
                            if kill_song:
                                music = pygame.mixer.music.load('res/sniper.mp3')
                                pygame.mixer.music.play(1)
                                time.sleep(.1)
                                music = pygame.mixer.music.load('res/kill.mp3')
                                pygame.mixer.music.play(1)
                                kill_song=False
                        
                    else:
                        if not end and not kill:
                            image[5:80,585:695]=cv2.rotate(girl,cv2.ROTATE_180)
                            i_prev=i

                    if girl_movement[1]-j<20 and not end:
                        cv2.rectangle(image,(585,5),(695,80),(0,0,255),3)
                
                else:
                    if start and not win:
                        girl_movement.pop(0)
                        
                        if not rotate:
                            rotate=True
                        else:
                            rotate=False

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        for id,lm in enumerate(hand_landmarks.landmark):
                            if not start:
                                if id==12:
                                    rect = ((int(lm.x*w),int(lm.y*h)-10),(30,30), random.randint(0,360))
                                    box=np.int0(cv2.boxPoints(rect))
                                    cv2.drawContours(image, [box], 0, (25,200,255), 3)
                                    if int(lm.x*w)<370 and int(lm.y*h)<220:
                                        start=True
                              
                            if id==8 and start:
                                if not win and not kill:
                                    if (int(lm.x*w)-x)**2+(int(lm.y*h)-y)**2<r**2:
                                        move=False
                                    else:
                                        if not end:
                                            move=True
                                            i+=speed
                                            
                                    cv2.circle(image,(int(lm.x*w),int(lm.y*h)),10,(100,250,100),-1)
                else:
                    if not kill and start:
                        i+=speed
                 
               
            else:
                
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        li=[]
                        for id,lm in enumerate(hand_landmarks.landmark):
                            mp_drawing.draw_landmarks(
                            image,
                            hand_landmarks,
                            mp_hands.HAND_CONNECTIONS,
                            mp_drawing_styles.get_default_hand_landmarks_style(),
                            mp_drawing_styles.get_default_hand_connections_style())
                            li.append(lm.y)
                        if li[4]<li[8] and li[4]<li[12] and li[4]<li[16] and li[4]<li[20] and li[4]*h<360:
                            splash=False
                            
                image[100:700,700:1200]=image[100:700,700:1200] * (1 - squareSplash[:, :, 3:] / 255) + squareSplash[:, :, :3] * (squareSplash[:, :, 3:] / 255)
                image[0:300,0:600]=image[0:300,0:600] * (1 - titleSplash[:, :, 3:] / 255) + titleSplash[:, :, :3] * (titleSplash[:, :, 3:] / 255)
                image[560:720,5:505]=image[560:720,5:505] * (1 - allSplash[:, :, 3:] / 255) + allSplash[:, :, :3] * (allSplash[:, :, 3:] / 255)
                image[300:400,5:95]=image[300:400,5:95] * (1 - thumbsup[:, :, 3:] / 255) + thumbsup[:, :, :3] * (thumbsup[:, :, 3:] / 255)
                
                
                
            if kill or win:
                image[550:700,750:1200]=image[550:700,750:1200] * (1 - restart[:, :, 3:] / 255) + restart[:, :, :3] * (restart[:, :, 3:] / 255)
                image[0:150,750:1200]=image[0:150,750:1200] * (1 - quit[:, :, 3:] / 255) + quit[:, :, :3] * (quit[:, :, 3:] / 255)
                
                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        for id,lm in enumerate(hand_landmarks.landmark):
                            if id==8:
                                cv2.circle(image,(int(lm.x*w),int(lm.y*h)),10,(100,250,100),-1)
                                if 750<lm.x*w<1200 and 0<lm.y*h<150:
                                    qu=True
                                    
                                if 750<lm.x*w<1200 and 550<lm.y*h<700:
                                    rest=True
                        

            if qu:
                break
            if rest:
                splash=False
                break
            if start and not timeOut:
                    if counter<0:
                        i_prev=0
                        timeOut=True
                    counter=counter-(time.time()-sT)
                    image=cv2.flip(image,1)
                    if counter<15:
                        counterColor=(0,0,225)
                    cv2.putText(image,f'{round(counter,2)}',(20,60),cv2.FONT_HERSHEY_DUPLEX,2,counterColor,2)
                    image=cv2.flip(image,1)
    
            cv2.imshow('Green light Red light', cv2.flip(image, 1))
        if qu:
            break
cap.release()
cv2.destroyAllWindows()