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

head  = 0               # Index of first 'on' pixel
tail  = -2             # Index of last 'off' pixel
color = 0xFFFFFF        # 'On' color (starts red)
unit1 = []
unit2 = []
unit3 = []
unit4 = []
unit5 = []
unit6 = []
units = [unit1,unit2,unit3,unit4,unit5,unit6]
unit_pairs = [(unit1,unit2), (unit3,unit4), (unit5,unit6)]
on = 384
off = 370
value = 190
led = 0


for unit in units:
    for i in range(192):
	unit.append(led)
        led += 1


while True:                              # Loop forever
    
    head += 1                        # Advance head position
    if(head >= 3):           # Off end of strip?
        head    = 0              # Reset to start
        color >>= 8              # Red->green->blue->black
        if(color == 0): color = 0xFF0000 # If black, reset to red

    tail += 1                        # Advance tail position
    if(tail >= 3): tail = 0  # Off end? Reset
    
    
    
    
    
    
    
    
    

    all_leds = []
    for a, b in unit_pairs:
        u_leds = []
        #for x in all_leds:
        #    strip.setPixelColor(x,0)
        for i in range(3):
            for x in range(on):
            #print(unit[0][0], unit[1][-1])
                led = random.randint(a[0], b[-1])
                strip.setPixelColor(led, color)
                u_leds.append(led)
                all_leds.append(led)
	    
            #for led in u_leds:
            #    strip.setPixelColor(led, color)
            strip.show()
            time.sleep(1.0 /20)
 
        
        
	#strip.show()
		#for led in all_leds:
		#	strip.setPixelColor(led, 0)
	


        #for x in range(off):
	#    led = random.choice(u_leds)
	#    strip.setPixelColor(led, 0)
	    
	strip.show()
        time.sleep(1.0 /10)
        
        
        for i in range(3):
            for x in range(value):
                led2 = random.choice(u_leds)
                strip.setPixelColor(led2,0)
            strip.show()
            time.sleep(1.0 /20)
 
        
        for x in all_leds:
            strip.setPixelColor(x,0)

	#strip.setPixelColor(head, color) # Turn on 'head' pixel
	#strip.setPixelColor(tail, 0)     # Turn off 'tail'
	#strip.show()                     # Refresh strip
    #time.sleep(1.0 )             # Pause 20 milliseconds (~50 fps)



'''

	head += 1                        # Advance head position
	if(head >= numpixels):           # Off end of strip?
		head    = 0              # Reset to start
		color >>= 8              # Red->green->blue->black
		if(color == 0): color = 0xFF0000 # If black, reset to red

	tail += 1                        # Advance tail position
	if(tail >= numpixels): tail = 0  # Off end? Reset


'''

