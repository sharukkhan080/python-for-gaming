from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *

class cordinates():
    replaybtn = (417,525)
    dinosaur = (238,532)

def restartGame():
    pyautogui.click(cordinates.replaybtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')

restartGame()
time.sleep(1)
pressSpace()


def imageGrab():
    box = (cordinates.dinosaur[0] + 60, cordinates.dinosaur[1],
           cordinates.dinosaur[0] + 120, cordinates.dinosaur[1] +30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())

while True:
    imageGrab()

def main():
    restartGame()
    while True:
        if(ImageGrab()!=2047):
            pressSpace()
            time.sleep(0.1)


main()
