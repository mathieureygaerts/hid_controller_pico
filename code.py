import time
import board
import digitalio
import analogio
import rotaryio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


def normalise_potentiometer(poto):
    noise = 500
    normalised = max(0, (poto - noise)) / (65520 - noise)
    return normalised


def pot_volt(poto):
    return poto * 3.3 / 65520

button_red_one = digitalio.DigitalInOut(board.GP1)
button_red_one.switch_to_input(pull=digitalio.Pull.DOWN)
button_red_one_state = False
button_red_two = digitalio.DigitalInOut(board.GP0)
button_red_two.switch_to_input(pull=digitalio.Pull.DOWN)
button_red_two_state = False
button_green_one = digitalio.DigitalInOut(board.GP3)
button_green_one.switch_to_input(pull=digitalio.Pull.DOWN)
button_green_one_state = False
button_green_two = digitalio.DigitalInOut(board.GP2)
button_green_two.switch_to_input(pull=digitalio.Pull.DOWN)
button_green_two_state = False
button_blue_one = digitalio.DigitalInOut(board.GP12)
button_blue_one.switch_to_input(pull=digitalio.Pull.DOWN)
button_blue_one_state = False
button_blue_two = digitalio.DigitalInOut(board.GP11)
button_blue_two.switch_to_input(pull=digitalio.Pull.DOWN)
button_blue_two_state = False

pot_one = analogio.AnalogIn(board.GP26)
pot_one_last_position = normalise_potentiometer(pot_one.value)
pot_two = analogio.AnalogIn(board.GP27)
pot_two_last_position = normalise_potentiometer(pot_two.value)

rotary_encoder_button = digitalio.DigitalInOut(board.GP19)
rotary_encoder_button.switch_to_input(pull=digitalio.Pull.DOWN)
rotary_encoder_button_state = False

rotary_encoder = rotaryio.IncrementalEncoder(board.GP20, board.GP21)
rotary_last_position = rotary_encoder.position


keyboard = Keyboard(usb_hid.devices)

time.sleep(2)

# while True:
#     print(pot_volt(pot_one.value))
#     time.sleep(0.2)

while True:
    # 6 buttons code
    if button_red_one.value and button_red_one_state is False:
        button_red_one_state = True
    if not button_red_one.value and button_red_one_state is True:
        # keyboard.press(Keycode.ALT, Keycode.F1)
        # keyboard.release(Keycode.ALT, Keycode.F1)
        print('red one')
        button_red_one_state = False

    if button_red_two.value and button_red_two_state is False:
        button_red_two_state = True
    if not button_red_two.value and button_red_two_state is True:
        # keyboard.press(Keycode.ALT, Keycode.F2)
        # keyboard.release(Keycode.ALT, Keycode.F2)
        print('red two')
        button_red_two_state = False

    if button_green_one.value and button_green_one_state is False:
        button_green_one_state = True
    if not button_green_one.value and button_green_one_state is True:
        # keyboard.press(key_shift, key_C)
        # keyboard.release(key_shift, key_C)
        print('green one')
        button_green_one_state = False

    if button_green_two.value and button_green_two_state is False:
        button_green_two_state = True
    if not button_green_two.value and button_green_two_state is True:
        # keyboard.press(key_shift, key_D)
        # keyboard.release(key_shift, key_D)
        print('green two')
        button_green_two_state = False

    if button_blue_one.value and button_blue_one_state is False:
        button_blue_one_state = True
    if not button_blue_one.value and button_blue_one_state is True:
        # keyboard.press(key_shift, key_E)
        # keyboard.release(key_shift, key_E)
        print('blue one')
        button_blue_one_state = False

    if button_blue_two.value and button_blue_two_state is False:
        button_blue_two_state = True
    if not button_blue_two.value and button_blue_two_state is True:
        # keyboard.press(key_shift, key_E)
        # keyboard.release(key_shift, key_E)
        print('blue two')
        button_blue_two_state = False

    # Potentiometer code
    pot_one_current_position = normalise_potentiometer(pot_one.value)
    pot_one_position_change = abs(pot_one_current_position - pot_one_last_position)
    if pot_one_position_change > 0.015:
        if pot_one_current_position < 0.01:
            pot_one_value = 0
        elif pot_one_current_position > 0.98:
            pot_one_value = 1
        else:
            pot_one_value = pot_one_current_position
        print('Potentioneter one {}'.format(pot_one_value))
        pot_one_last_position = pot_one_current_position

    pot_two_current_position = normalise_potentiometer(pot_two.value)
    pot_two_position_change = abs(pot_two_current_position - pot_two_last_position)
    if pot_two_position_change > 0.015:
        if pot_two_current_position < 0.01:
            pot_two_value = 0
        elif pot_two_current_position > 0.98:
            pot_two_value = 1
        else:
            pot_two_value = pot_two_current_position
        print('Potentioneter two {}'.format(pot_two_value))
        pot_two_last_position = pot_two_current_position

    # Rotary encoder code
    rotary_current_position = rotary_encoder.position
    rotary_position_change = rotary_current_position - rotary_last_position
    if rotary_position_change > 0:
        for _ in range(rotary_position_change):
            # keyboard.press(key_shift, key_G)
            # keyboard.release(key_shift, key_G)
            pass
        print(rotary_current_position)
    elif rotary_position_change < 0:
        for _ in range(-rotary_position_change):
            # keyboard.press(key_shift, key_H)
            # keyboard.release(key_shift, key_H)
            pass
        print(rotary_current_position)
    rotary_last_position = rotary_current_position
    if rotary_encoder_button.value and rotary_encoder_button_state is False:
        rotary_encoder_button_state = True
    if not rotary_encoder_button.value and rotary_encoder_button_state is True:
        print("Rotary Button pressed.")
        # keyboard.press(key_shift, key_I)
        # keyboard.release(key_shift, key_I)
        rotary_encoder_button_state = False
