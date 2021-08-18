import cv2
import numpy as np
import pyautogui
import pydirectinput
import keyboard
from PIL import ImageGrab
import time

def mining_forward():
    terminated = False
    while not found_diamonds and not terminated:
        pydirectinput.keyDown("w")
        if keyboard.is_pressed("u"):
            pydirectinput.keyUp("w")
            terminated = True
            print("Loop Deacitvated")
def torch_timer():
    torch_time = time.time()
    if(time.time()> torch_time + torch_interval):
        torch_time = time.time
        print("Placing Torch")
        #place_torch()
def place_torch():
    placing_torch = True
    pydirectinput.moveRel(0,500)
    pydirectinput.rightClick()
    pydirectinput.moveRel(0,-500)
    placing_torch = False

def Update():
    
    found_diamonds = False
    terminated = False
    pause = False
    torch_interval = 5.6
    lower_range_diamond = np.array([75, 80, 100])
    upper_range_diamond = np.array([90, 255, 255])
    lower_range_lava = np.array([7, 216, 193])
    upper_range_lava = np.array([23, 255, 255])
    timer = time.time()
    screenshot_timer = time.time()
    #Break the Application to end
    while True:
        
        if not found_diamonds and not terminated:
            pydirectinput.keyDown("w")#Move Forward
            pydirectinput.mouseDown()
            #else:
                #Paused Functions
            if keyboard.is_pressed("u"):
                ReleaseBinds()
                break #Terminate the Application
            #Timer for ScreenShot
            if (time.time()> screenshot_timer+0.4):
                ScreenShot()
                img1 = cv2.imread("screenshot.png")
                hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
                diamond_mask = cv2.inRange(hsv, lower_range_diamond, upper_range_diamond)
                lava_mask = cv2.inRange(hsv, lower_range_lava, upper_range_lava)
                cv2.imwrite("HSV.png", hsv)
                cv2.imwrite("Diamond_Mask.png", diamond_mask)
                cv2.imwrite("Lava_mask.png", lava_mask)
                print("Diamond color: " + str(cv2.countNonZero(diamond_mask)))
                print("Lava color: " + str(cv2.countNonZero(lava_mask)))
                if cv2.countNonZero(diamond_mask)>2000:
                    found_diamonds = True
                    print("Found Diamonds!!!")
                if cv2.countNonZero(lava_mask)>2000:
                    terminated = True
                    EmergencyBucket()
                    print("Found LAVA!!!")
            #Timer for Torches
            if(time.time() > timer + torch_interval):
                timer = time.time()
                print("Torch Placement")
                ReleaseBinds()
                pydirectinput.move(400,0, relative=True)
                time.sleep(0.1)
                pydirectinput.rightClick()
                pydirectinput.move(-400,0, relative=True)
                time.sleep(1)
        else:
            ReleaseBinds()
            break

def ScreenShot():
    myScreenShot = pyautogui.screenshot('screenshot.png')
    #myScreenShot.save('.\screenshot.png')     
    
def ReleaseBinds():
    pydirectinput.keyUp("w")
    pydirectinput.mouseUp()
def EmergencyBucket():
    ReleaseBinds()
    pydirectinput.move(0,500, relative=True)
    pydirectinput.keyDown("3")
    pydirectinput.rightClick()
def Test():
    EmergencyBucket()




time.sleep(5)
#Test()
Update()
#mining_forward()
#torch_timer()
print("Application Closed")