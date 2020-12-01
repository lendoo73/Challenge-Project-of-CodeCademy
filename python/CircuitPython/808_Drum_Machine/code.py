from adafruit_circuitplayground.express import cpx

# The seven audio files
audiofiles = [
    "bd_tek.wav", 
    "elec_hi_snare.wav", 
    "elec_cymbal.wav", 
    "elec_blip2.wav", 
    "bd_zome.wav", 
    "bass_hit_c.wav", 
    "drum_cowbell.wav"
]

def play_file(i):
    print(i)
    cpx.play_file(audiofiles[i - 1])
    cpx.pixels[i] = (i ** 2, i ** 3, i ** 4)


while True:
    cpx.pixels.fill(
        (0, 0, 0)
    )
    if cpx.touch_A1:
        play_file(1)
    if cpx.touch_A2:
        play_file(2)
    if cpx.touch_A3:
        play_file(3)
    if cpx.touch_A4:
        play_file(4)
    if cpx.touch_A5:
        play_file(5)
    if cpx.touch_A6:
        play_file(6)
    if cpx.touch_A7:
        play_file(7)