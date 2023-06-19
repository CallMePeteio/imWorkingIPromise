

import time 
import mouse
import random 
import pyautogui
import pandas as pd

googleList = pd.read_csv("C:/Users/petter/Desktop/coding/python/imWorkingIPromise/seartch.csv")

def sleepRandint():
    time.sleep(random.uniform(0, 1.5))
def moveWheel(range_, minSleep): 
    for i in range(int(range_)):
        mouse.wheel(1)
        time.sleep(minSleep)

    sleepRandint()

    if random.randint(0, 100) <= 10:
        for i in range(range_):
            if random.randint(0, 100) <= 35:
                mouse.wheel(-1.3)
            else: 
                mouse.wheel(1.3)
            time.sleep(minSleep/2)
        return None


    for i in range(range_):
        mouse.wheel(-1)
        time.sleep(minSleep)

    sleepRandint()
def moveMouse(pos=None, speed=None):
        
    if pos == None and speed == None:
        mosePosZ = mouse.get_position()[1] 
        if mosePosZ > 800:
            mouse.move(random.randint(-100, 100), random.randint(-400, 0), absolute=False, duration=random.uniform(0.1, 0.3))
        else: 
            mouse.move(random.randint(-100, 100), random.randint(-500, 300), absolute=False, duration=random.uniform(0.1, 0.5))
    else: 
        print(mouse.get_position())
        mouse.move(pos[0], pos[1], absolute=False, duration=speed)
        print(mouse.get_position())




def google(googleChanse): 

    if random.randint(0, 100) < googleChanse:
        random_item = googleList.sample(n=1)
        search_string = random_item["seartch"].values[0]



        pyautogui.hotkey('ctrl', 't') # PRESSES CTR + T (NEW PAGE)
        pyautogui.click(-1100, 52) # PRESSES THE GOOGLE CHROME SEARTCH BAR
        
        for char in list(search_string): # LOOPS OVER ALL OF THE CHARACHTERS OF THE STRING
            pyautogui.press(char) # ENTERS THE LETTERS
            time.sleep(random.uniform(0.05, 0.3)) # SLEEPS A BIT

        pyautogui.press("enter")

        return 1
    return 0    


time.sleep(2)
i=0
while True:


    #i+=1
    #if random.randint(0, 100) < 30:
    #    moveWheel(random.randint(0, 30), random.uniform(0, 0.1))
    #else: 
    #    moveMouse()
#
    #
    #if random.randint(0, 100) < 90 and mouse.get_position()[1] <= 90:
    #    if random.randint(0, 100) < 50:
    #        mouse.move(40, 0, absolute=False, duration=random.uniform(0.25, 0.5))
    #    else: 
    #        mouse.move(0, 40, absolute=False, duration=random.uniform(0.25, 0.5))
#
#
    #    mouse.click("left")
    #    time.sleep(0.5)
    #    mouse.move(0, 800, absolute=False, duration=random.uniform(0.25, 0.5))
    #
    #elif random.randint(0, 100) < 85:
    #    mouse.click("left")


    google(100)

    print(i)
    print(mouse.get_position())

    




















































































