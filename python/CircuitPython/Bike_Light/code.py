from adafruit_circuitplayground.express import cpx
import time

RED = (255, 0, 0)
OFF = (0, 0, 0)
blink = False

while True:
    if cpx.switch:
        cpx.pixels.fill(RED)
        
        # switch on blinking:
        if cpx.button_a:
            blink = True
        
        # switch off blinking:
        if cpx.button_b:
            blink = False
        
        if blink:
            time.sleep(0.5)
            cpx.pixels.fill(OFF)
            time.sleep(0.5)
            cpx.pixels.fill(RED)

    else:
        cpx.pixels.fill(OFF)
