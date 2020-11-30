from adafruit_circuitplayground.express import cpx
import touchio
import board

OFF = (0, 0, 0)
WARNING = (96, 185, 187)
GREEN = (0, 255, 0)
A1 = board.A1
touch = touchio.TouchIn(A1)

while True:
    if cpx.switch:
        cpx.red_led = False
        cpx.pixels.fill(OFF)
        if cpx.button_a:
            print("Temperature: ", cpx.temperature)
        if cpx.button_b:
            print("Light value: ", cpx.light)
    else:
        # for soil moisture sensing:
        cpx.red_led = True
        moisture = touch.raw_value
        print(moisture)
        if moisture < 1700:
            cpx.pixels.fill(WARNING)
        else:
            cpx.pixels.fill(OFF)
   
