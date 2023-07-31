import random
import datetime
from os import system

def gen_card(bin,exp_m,exp_y,cvv):
    #card number
    card_number = bin
    for _ in range(15-len(bin)):
        digit = random.randint(0, 9)
        card_number += str(digit)
    digits = [int(x) for x in card_number]
    for i in range(0, 16, 2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    total = sum(digits)
    check_digit = (10 - (total % 10)) % 10
    card_number += str(check_digit)
    #exp month
    if exp_m == "":
        exp_m = str(random.randint(1, 12)).zfill(2)
    else:
        exp_m = exp_m.zfill(2)
    #exp year
    if exp_y == "":
        current_year = datetime.datetime.now().year
        random_offset = random.randint(1, 5)
        exp_y = current_year + random_offset
    elif int(exp_y) >= 10 and int(exp_y) <= 99:
        exp_y = "20" + exp_y
    if cvv == "":
        cvv = str(random.randint(0, 999)).zfill(3)
    else:
        cvv = cvv.zfill(3)
    print(f"{card_number}|{exp_m}|{exp_y}|{cvv}")
# Main
try: system("cls")
except: system("clear")
a = input("Bin: ")
b = input("Month(Empty for random): ")
c = input("Year(Empty for random): ")
d = input("CVV(Empty for random): ")
e = int(input("Quantity: "))
f = 0
while f < e:
    gen_card(a,b,c,d)
    f += 1
