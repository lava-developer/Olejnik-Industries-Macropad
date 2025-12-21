# Importing necessary modules
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

# Defining keyboard object
keyboard = KMKKeyboard()

# Defining macros
macros = Macros()
keyboard.modules.append(macros)

#  Defining pins
PINS = [board.D3, board.D6, board.D10, board.D1, board.D2, board.D9, board.D0, board.D7, board.D8]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Basic numpad keymap
keyboard.keymap = [
    [KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9]
]

# Starting kmk
if __name__ == '__main__':
    keyboard.go()