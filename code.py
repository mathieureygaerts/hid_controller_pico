import time
import board
import digitalio
import analogio
import rotaryio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.consumer_control import ConsumerControl


def pot_volt(poto):
    return poto * 3.3 / 65520


def normalise_potentiometer(poto, in_min, in_max, out_min, out_max):
    normalised = (poto - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    return int(normalised)


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

# pot_one = analogio.AnalogIn(board.GP26)
# pot_one_last_position = normalise_potentiometer(pot_one.value)

# Set the 2nd potentiometer to control the volume.
pot_two = analogio.AnalogIn(board.GP27)
# pot_two_last_position = normalise_potentiometer(pot_two.value, 200, 65520, 0, 32)
pot_two_last_position = 0
consumer_control = ConsumerControl(usb_hid.devices)
# Set the volume to 0
for i in range(32):
    consumer_control.send(ConsumerControlCode.VOLUME_DECREMENT)


rotary_encoder_button = digitalio.DigitalInOut(board.GP19)
rotary_encoder_button.switch_to_input(pull=digitalio.Pull.DOWN)
rotary_encoder_button_state = False

rotary_encoder = rotaryio.IncrementalEncoder(board.GP20, board.GP21)
rotary_last_position = rotary_encoder.position


keyboard = Keyboard(usb_hid.devices)

time.sleep(2)


while True:
    # 6 buttons code
    if button_red_one.value and button_red_one_state is False:
        button_red_one_state = True
    if not button_red_one.value and button_red_one_state is True:
        keyboard.press(Keycode.ALT, Keycode.F2)
        keyboard.release(Keycode.ALT, Keycode.F2)
        # print('red one')
        button_red_one_state = False

    if button_red_two.value and button_red_two_state is False:
        button_red_two_state = True
    if not button_red_two.value and button_red_two_state is True:
        keyboard.press(Keycode.ALT, Keycode.F1)
        keyboard.release(Keycode.ALT, Keycode.F1)
        # print('red two')
        button_red_two_state = False

    if button_green_one.value and button_green_one_state is False:
        button_green_one_state = True
    if not button_green_one.value and button_green_one_state is True:
        keyboard.press(Keycode.CTRL, Keycode.K)
        keyboard.release(Keycode.CTRL, Keycode.K)
        # print('green one')
        button_green_one_state = False

    if button_green_two.value and button_green_two_state is False:
        button_green_two_state = True
    if not button_green_two.value and button_green_two_state is True:
        keyboard.press(Keycode.ALT, Keycode.F3)
        keyboard.release(Keycode.ALT, Keycode.F3)
        # print('green two')
        button_green_two_state = False

    if button_blue_one.value and button_blue_one_state is False:
        button_blue_one_state = True
    if not button_blue_one.value and button_blue_one_state is True:
        keyboard.press(Keycode.SHIFT, Keycode.F2)
        keyboard.release(Keycode.SHIFT, Keycode.F2)
        # print('blue one')
        button_blue_one_state = False

    if button_blue_two.value and button_blue_two_state is False:
        button_blue_two_state = True
    if not button_blue_two.value and button_blue_two_state is True:
        keyboard.press(Keycode.SHIFT, Keycode.F1)
        keyboard.release(Keycode.SHIFT, Keycode.F1)
        # print('blue two')
        button_blue_two_state = False

    # # Potentiometer code
    # pot_one_current_position = normalise_potentiometer(pot_one.value)
    # pot_one_position_change = abs(pot_one_current_position - pot_one_last_position)
    # if pot_one_position_change > 0.015:
    #     if pot_one_current_position < 0.01:
    #         pot_one_value = 0
    #     elif pot_one_current_position > 0.98:
    #         pot_one_value = 1
    #     else:
    #         pot_one_value = pot_one_current_position
    #     print('Potentioneter one {}'.format(pot_one_value))
    #     pot_one_last_position = pot_one_current_position


    pot_two_current_position = normalise_potentiometer(pot_two.value, 200, 65520, 0, 32)
    pot_two_position_change = abs(pot_two_current_position - pot_two_last_position)
    if pot_two_position_change > 1:
        print(pot_two_current_position)
        if pot_two_current_position < pot_two_last_position:
            for _ in range(pot_two_position_change):
                consumer_control.send(ConsumerControlCode.VOLUME_INCREMENT)
                print("Volume up")
        elif pot_two_current_position > pot_two_last_position:
            for _ in range(pot_two_position_change):
                consumer_control.send(ConsumerControlCode.VOLUME_DECREMENT)
                print("Volume down")


        pot_two_last_position = pot_two_current_position

    # Rotary encoder code
    rotary_current_position = rotary_encoder.position
    rotary_position_change = rotary_current_position - rotary_last_position
    if rotary_position_change > 0:
        for _ in range(rotary_position_change):
            keyboard.press(Keycode.ALT, Keycode.SHIFT, Keycode.F2)
            keyboard.release(Keycode.ALT, Keycode.SHIFT, Keycode.F2)
            pass
        print(rotary_current_position)
    elif rotary_position_change < 0:
        for _ in range(-rotary_position_change):
            keyboard.press(Keycode.ALT, Keycode.SHIFT, Keycode.F1)
            keyboard.release(Keycode.ALT, Keycode.SHIFT, Keycode.F1)
            pass
        print(rotary_current_position)
    rotary_last_position = rotary_current_position
    if rotary_encoder_button.value and rotary_encoder_button_state is False:
        rotary_encoder_button_state = True
    if not rotary_encoder_button.value and rotary_encoder_button_state is True:
        # print("Rotary Button pressed.")
        keyboard.press(Keycode.SHIFT, Keycode.F3)
        keyboard.release(Keycode.SHIFT, Keycode.F3)
        rotary_encoder_button_state = False
