#!/usr/bin/python

# Simple strand test for Adafruit Dot Star RGB LED strip.
# This is a basic diagnostic tool, NOT a graphics demo...helps confirm
# correct wiring and tests each pixel's ability to display red, green
# and blue and to forward data down the line.  By limiting the number
# and color of LEDs, it's reasonably safe to power a couple meters off
# USB.  DON'T try that with other code!

import time
from dotstar import Adafruit_DotStar
import random


from PIL import Image


mush= Image.open("Mushroom.jpg")
rainbow=Image.open("Rainbow.jpg")
RR=Image.open("RRLogo.jpg")

array_LED = []
aspect_ratio = [23,50]



def turn_to_2d(aspect_ratio,array_LED):
    count = 0
    result = [[array_LED[count] for x in range(aspect_ratio[0])] for y in range(aspect_ratio[1])]

    for x in range(int(n_pixels/n_columns)):
        for y in range (n_columns):
            result[x][y] = array_LED[count]
            count+=1
    return result


def get_rgb_from_image(image,aspect_ratio):
    abc = Image.open(image)
    pix = abc.load()

    result = [rgb2hex(pix[x,y]) for x in range(aspect_ratio[0]) for y in range(aspect_ratio[1])]

    print(result)
    return result


def rgb2hex(rgb):
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    return "#{:02x}{:02x}{:02x}".format(r,g,b)


numpixels = 1152 # Number of LEDs in strip

# Here's how to control the strip from any two GPIO pins:
strip    = Adafruit_DotStar(numpixels, 2000000)

# Alternate ways of declaring strip:
#  Adafruit_DotStar(npix, dat, clk, 1000000) # Bitbang @ ~1 MHz
#  Adafruit_DotStar(npix)                    # Use SPI (pins 10=MOSI, 11=SCLK)
#  Adafruit_DotStar(npix, 32000000)          # SPI @ ~32 MHz
#  Adafruit_DotStar()                        # SPI, No pixel buffer
#  Adafruit_DotStar(32000000)                # 32 MHz SPI, no pixel buf
# See image-pov.py for explanation of no-pixel-buffer use.
# Append "order='gbr'" to declaration for proper colors w/older DotStar strips)

strip.begin()           # Initialize pins for output
strip.setBrightness(64) # Limit brightness to ~1/4 duty cycle

# Runs 10 LEDs at a time along strip, cycling through red, green and blue.
# This requires about 200 mA for all the 'on' pixels + 1 mA per 'off' pixel.

#head  = 0               # Index of first 'on' pixel
#tail  = -10             # Index of last 'off' pixel
color = 0xFF0000        # 'On' color (starts red)

on = 100
off = 40
led = 0

array_strip=
color_strip= get_rgb_from_image(rainbow, aspect_ratio)


while True:                              # Loop forever


	for row in array_strip:
		for column in array_strip[row]:

		strip.setPixelColor(array_strip[row][column], color_strip[row][column])
		strip.show()
