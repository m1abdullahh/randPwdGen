import random
from time import sleep
from pause import pause
from clear import Clear
import array

# This simple generates a strong random password based on how long the user wants the password to be.
print("Enter the amount of numbers you want your password to consist of")

MAX_LEN = int(input())

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')']

COMBINED_LIST = DIGITS + LOCASE_CHARACTERS + UPCASE_CHARACTERS + SYMBOLS

RAND_DIG = random.choice(DIGITS)
RAND_LOCASE = random.choice(LOCASE_CHARACTERS)
RAND_UPCASE = random.choice(UPCASE_CHARACTERS)
RAND_SYMBOL = random.choice(SYMBOLS)

temp_pass = RAND_DIG + RAND_LOCASE + RAND_UPCASE + RAND_SYMBOL

for x in range((MAX_LEN - 4)):
    temp_pass = temp_pass + random.choice(COMBINED_LIST)
    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)
password = ""
for x in temp_pass_list:
    password = password + x

print(password)