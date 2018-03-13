import pyautogui as pya
import time
import itertools
import string
from sys import argv

def guess_password(real):
    username = argv[1]
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    password_length = 8
    for guess in itertools.product(chars, repeat=password_length):
        attempts += 1
        guess = ''.join(guess)
        pya.typewrite(username)
        pya.press('tab')
        pya.typewrite(guess)
        pya.press('enter')
        time.sleep(0.1)
        if guess == real:
            return 'password is {}. found in {} guesses.'.format(guess, attempts)
        print(guess, attempts)

time.sleep(5)
print(guess_password('aaaaaagh'))

