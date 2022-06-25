import pygame
import time

pygame.init()

char_volume = "void"
volume = 0
player_answer = "void"



def Print_Name():

    global sound

    print("\n\n")
    print("            *  *   ****  *****  *****  *   *    *******                  ")
    print("            * *    *  *  *   *  *      **  *   *                         ")
    print("            **     *  *  *****  *****  * * *  *    *****                 ")
    print("            * *    *  *  *      *      *  **   *     *                   ")
    print("            *  *   ****  *      *****  *   *    *******                  ")
    print("\n\n")

    sound = pygame.mixer.Sound("starting msg.mp3")

    for x in range(1):
        sound.play(0)



def Input_PlayerChoiceMusic():
    
    global ChoiceMusic
    global sound

    ChoiceMusic = input("어떤 곡으로 알람을 맞추시겠습니까? : ")
    sound = pygame.mixer.Sound(ChoiceMusic)



def Input_PlayerChoiceMusicVolume():

    global char_volume
    global volume
    global sound

    char_volume = input("알람소리 크기를 몇으로 설정하시겠습니까? (1 ~ 100) : ")
    volume = int(char_volume)
    volume = volume / 50       # 볼륨 크기 설정
    sound.set_volume(volume)



def Input_PlayerChoiceMusicSecond():
    
    global char_TimeSet
    global WaitTime
    
    char_TimeSet = input("알람을 몇분에 한번씩 울리시겠습니까? : ")
    WaitTime = float(char_TimeSet)       # 몇분에 한번씩 울릴지 설정
    WaitTime = WaitTime * 600



def Start_ClockTimer():
    
    global StartTime
    global WaitTime
    global sound
    global player_answer

    print("\n\n지금 부터 타이머를 시작합니다...\n\n")
    
    
    time.sleep(WaitTime)
    
    while True:
        sound.play(0)
        print("타이머를 끄시려면 enter를 눌러주세요...")
        player_answer = input("")
        sound.stop()
        break
    
    while True:

        player_answer = input("\n\n타이머를 다시 시작하시겠습니까? (y or n) : ")

        if player_answer == 'y':
            Start_ClockTimer()
        elif player_answer == 'n':
            print("\n\n")
            exit()
        else:
            print("\n다시 입력해주세요...\n")



def play():
    
    Print_Name()
    Input_PlayerChoiceMusic()
    Input_PlayerChoiceMusicVolume()
    Input_PlayerChoiceMusicSecond()
    Start_ClockTimer()

play()