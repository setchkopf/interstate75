
import interstate75

# import jpegdec
from pngdec import PNG
# import picographics

from machine import Timer 

i75 = interstate75.Interstate75(display=interstate75.DISPLAY_INTERSTATE75_32X32)
graphics = i75.display

width = i75.width
height = i75.height

import os
#imgs = ["white.png", "tri-test.png","waves.png"]

#Create list of all png files
imgs=[]
for filename in os.listdir("."):
    if filename.endswith(".png"):
        imgs.append(filename)

allow_switch = 1

def timer_callback(t):
    global allow_switch
    allow_switch = 1
    print("timer")
    
bounce_delay = 800 #ms   
timer = Timer(period=bounce_delay, mode=Timer.PERIODIC, callback=timer_callback) #hacky bounce prevention

def button_A():
    if allow_switch == 1:
        img = imgs.pop(0) #grab first in list
        imgs.append(img) #add to end of list
        update_img(img)
        
def button_boot():
    if allow_switch == 1:
        img = imgs.pop() #grab last in list
        imgs.insert(0, img) #add to start
        update_img(img)

def update_img(img):
    global allow_switch
    allow_switch = 0
    png = PNG(graphics)
    png.open_file(img)
    png.decode(0, 0)
    i75.update()

update_img("standby.png")

while 1:
    if i75.switch_pressed(interstate75.SWITCH_A):
        button_A()
    if i75.switch_pressed(interstate75.SWITCH_BOOT):
        button_boot()
