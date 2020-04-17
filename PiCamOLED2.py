from picamera import PiCamera
from time import sleep
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import io

import subprocess

RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

disp.begin()
disp.clear()
disp.display()

camera = PiCamera()
camera.rotation = 180

width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
padding = -2
top = padding
bottom = height-padding
font = ImageFont.load_default()
##
##draw.rectangle((0,0,width,height), outline=0, fill=0)
##draw.text((0, top), "Press R to take an ", font=font, fill = 255)
##draw.text((0, top+8), "image", font=font, fill = 255)
##draw.text((0, top+16), "Press D to display ", font=font, fill=255)
##draw.text((0, top+24), "the image", font=font, fill=255)
##
##disp.image(image)
##disp.display()
##
##
##y = 0
##
##while y < 5:
##    x = input("Press R or D")
##
##    if (x == 'R'):
##        camera.start_preview()
##        sleep(7)
##        camera.capture('/home/pi/Desktop/temp.png')
##        camera.stop_preview()
##    elif(x == 'D'):
##        disp.clear()
##        disp.display()
##        image2 = Image.open('/home/pi/Desktop/temp.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
##        disp.image(image2)
##        disp.display()
##        sleep(10)
##        disp.clear()
##        disp.display()
##        draw.rectangle((0,0,width,height), outline=0, fill=0)
##        draw.text((0, top), "Press R to take an ", font=font, fill = 255)
##        draw.text((0, top+8), "image", font=font, fill = 255)
##        draw.text((0, top+16), "Press D to display ", font=font, fill=255)
##        draw.text((0, top+24), "the image", font=font, fill=255)
##        disp.image(image)
##        disp.display()
##    y += 1

while True:

    stream = io.BytesIO()
##    with camera:
##        camera.start_preview()
##        time.sleep(2)
##        camera.capture(stream, format='png')
    camera.capture(stream, format='png')
    stream.seek(0)
    im = Image.open(stream).resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
    disp.image(im)
    disp.display()
