"""Button example for Pico. Prints message to serial console when button is pressed.
REQUIRED HARDWARE:* Button switch on pin GP13."""
import time
import board
import digitalio
import analogio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

button_red_one = digitalio.DigitalInOut(board.GP1)
button_red_one.switch_to_input(pull=digitalio.Pull.DOWN)
button_red_two = digitalio.DigitalInOut(board.GP0)
button_red_two.switch_to_input(pull=digitalio.Pull.DOWN)
button_green_one = digitalio.DigitalInOut(board.GP3)
button_green_one.switch_to_input(pull=digitalio.Pull.DOWN)
button_green_two = digitalio.DigitalInOut(board.GP2)
button_green_two.switch_to_input(pull=digitalio.Pull.DOWN)
button_blue_one = digitalio.DigitalInOut(board.GP12)
button_blue_one.switch_to_input(pull=digitalio.Pull.DOWN)
button_blue_two = digitalio.DigitalInOut(board.GP11)
button_blue_two.switch_to_input(pull=digitalio.Pull.DOWN)

pot_one = analogio.AnalogIn(board.GP26)
pot_two = analogio.AnalogIn(board.GP27)

key_A = Keycode.A
key_B = Keycode.B
key_C = Keycode.C
key_D = Keycode.D
key_E = Keycode.E
key_F = Keycode.F
key_Shift = Keycode.SHIFT
keyboard = Keyboard(usb_hid.devices)

time.sleep(2)

while True:
    if button_red_one.value:
        keyboard.press(key_Shift, key_A)
        keyboard.release(key_Shift, key_A)
        time.sleep(0.2)
    elif button_red_two.value:
        keyboard.press(key_Shift, key_B)
        keyboard.release(key_Shift, key_B)
        time.sleep(0.2)
    elif button_green_one.value:
        keyboard.press(key_Shift, key_C)
        keyboard.release(key_Shift, key_C)
        time.sleep(0.2)
    elif button_green_two.value:
        keyboard.press(key_Shift, key_D)
        keyboard.release(key_Shift, key_D)
        time.sleep(0.2)
    elif button_blue_one.value:
        keyboard.press(key_Shift, key_E)
        keyboard.release(key_Shift, key_E)
        time.sleep(0.2)
    elif button_blue_two.value:
        keyboard.press(key_Shift, key_F)
        keyboard.release(key_Shift, key_F)
        time.sleep(0.2)
   else:
       print('Pot one: {}'.format(pot_one.value))
       print('Pot two: {}'.format(pot_two.value))
       time.sleep(0.5)
