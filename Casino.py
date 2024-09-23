import random
import time
import threading
import sys
import os
import json
import datetime
from datetime import datetime, timedelta
os.system("title " + "Let's go gambling! dududu ehh. God damn it!")

# GAMES


RouletteWheelNumbers = [" 0","32","15","19"," 4","21"," 2","25","17","34"," 6","27","13","36","11","30"," 8","23","10"," 5","24","16","33"," 1","20","14","31"," 9","22","18","29"," 7","28","12","35"," 3","26"]
RouletteWheelColors =  ["🟩", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛" ]
RouletteRed =          [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
RouletteBlack =        [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

SlotSymbols = ["❌", "🍒", "🍒", "🔔", "🔔", "🍋", "🍋", "💎"] # Intended for Slot Mashines

# Keno.             No list to implement
# Horse betting.    No list to implement

cards = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13} # Casino war

# Coin flip.        No list to implement
# Crash.            No list to implement

dailyrewardlistmoney = [250, 500, 750, 1000]
dailyrewardlistXP = [75, 100, 125, 150]

money = 1000
merry_christmas = True


username = "N/A"
xp = 0
xptoreachbase = 100
level = 1
wins_roulette = 0
wins_slots = 0
wins_keno = 0
wins_casinowar = 0
wins_coinflip = 0
wins_crash = 0
wins_horsebetting = 0
json_datetime = "N/A"
legit = True
value1 = 0

save_file = "Casinosave.json"

def Stats():
    global username, xp, xptoreach, level, wins_casinowar, wins_coinflip, wins_crash, wins_horsebetting, wins_keno, wins_slots, wins_roulette

    xptoreach = xptoreachbase*level
    xp_filled_value = round((xp / xptoreach) * 20)
    xp_filled = ""
    for _ in range(xp_filled_value):
        xp_filled += '#'
    for _ in range(20 - xp_filled_value):
        xp_filled += '-'
    
    print("\033[H\033[J", end="")


    print(f"Username: {username}")
    print(f"Money:    {money}")
    print(f"Level:    {level}")
    print(f"XP:       {xp} / {xptoreach}")
    print(f"[{xp_filled}]\n")

    print(f"Roulette wins:      {wins_roulette}")
    print(f"Slots wins:         {wins_slots}")
    print(f"Keno wins:          {wins_keno}")
    print(f"Horse betting wins: {wins_horsebetting}")
    print(f"Casino war wins:    {wins_casinowar}")
    print(f"Coinflip wins:      {wins_coinflip}")
    print(f"Crash wins:         {wins_crash}\n")

    print(f"Press enter to exit")
    input()

def Roulette():
    global money, wins_roulette, xp
    
    def is_odd(number):
        return number % 2 != 0

    print("\033[H\033[J", end="")
    print("🎲 Welcome to Roulette 🎲")
    print("The goal of roulette is to predict the spot which the \"ball\" will land.\nYou can bet on specific numbers, colors or whenever the result is odd or even")
    print(f"\nCurrent balance: {money}")
    print("Enter your bet or say \"Color\" for the color table")

    inputlist = ["red", "black", "odd", "even", "1st12", "2nd12", "3rd12"]
    userinputroulette = ""

    while True:
        try:
            input_payout_or_bet = input()
            bet_roulette = int(input_payout_or_bet)
            if -1 < bet_roulette < money+1:
                money -= bet_roulette
                break
            else:
                print("Please select a valid bet")
        except ValueError:
            if input_payout_or_bet.lower() == "color":
                print("= Color table =")
                print("Red: ", RouletteRed)
                print("Black: ", RouletteBlack)
                print("Enter your bet or say \"Color\" for the color table")
            if input_payout_or_bet == "xameren":
                print("xamarin???")
            else:
                print("Please select a valid bet")
    print("\033[H\033[J", end="")
    print("|       Select the bet      |")
    print("+---------------------------+")
    print("| Red | Black || Odd | Even |")
    print("|===========================|")
    print("| 1st 12 | 2nd 12 | 13rd 12 |")
    print("|===========================|")
    print("| Individual numbers (0-36) |")
    print("+---------------------------+")
    while True:
        try:
            input_roulette = input()
            if input_roulette in inputlist or -1 < int(input_roulette) < 37:
                break
            else:
                print("Please select a valid option")
        except ValueError:
            if input_payout_or_bet.lower() == "color":
                print("= Color table =")
                print("Red: ", RouletteRed)
                print("Black: ", RouletteBlack)
                print("Enter your bet or say \"Color\" for the color table")
            else:
                print("Please select a valid bet")
    userinputroulette = input_roulette
    roulette_speed = 0
    decor = 1
    print("\033[H\033[J", end="")

    for i in range(15, 51): # change to 1 when testing, the result is 15. The default is random.randint(15, 51)
        start_index = i % len(RouletteWheelNumbers)
        the_roulette = RouletteWheelNumbers[start_index:start_index+5]
        if len(the_roulette) < 5:
            the_roulette += RouletteWheelNumbers[:5 - len(the_roulette)]
        the_roulette_colors = RouletteWheelColors[start_index:start_index+5]
        if len(the_roulette_colors) < 5:
            the_roulette_colors += RouletteWheelColors[:5 - len(the_roulette_colors)]

        translationtable = str.maketrans(",", "|", "[\']")
        cleanedtext = str(the_roulette).translate(translationtable)
        cleanedcolors = str(the_roulette_colors).translate(translationtable)
        time.sleep(roulette_speed)
        #if roulette_speed < 0.75:
        roulette_speed += 0.01
        if decor == 1:
            decortext = "/"
            decor += 1
        elif decor == 2:
            decortext = "|"
            decor += 1
        else:
            decortext = "\\"
            decor = 1
        print("\033[H", end="")
        print(decortext, " Roulette wheel ", decortext)
        print("|‾‾‾‾‾‾‾‾\\/‾‾‾‾‾‾‾‾|")
        print(f"|{cleanedtext}|")
        print(f"|{cleanedcolors}|")
        print("|________/\\________|")
        print(decortext, " Roulette wheel ", decortext)

    textdecorup   = "|‾‾‾‾‾‾‾‾##‾‾‾‾‾‾‾‾|"
    textdecordown = "|________##________|"
    textdecornumberrouletteend = 0
    for i in range(5):    
    
        print("\033[H", end="")
        print()
        print(decortext, " Roulette wheel ", decortext)
        print(textdecorup)
        print(f"|{cleanedtext}|")
        print(f"|{cleanedcolors}|")
        print(textdecordown)
        print(decortext, " Roulette wheel ", decortext)
        textdecornumberrouletteend += 1
        time.sleep(0.2)
        if textdecornumberrouletteend == 1:
            textdecorup   = "|‾‾‾‾‾‾‾>##<‾‾‾‾‾‾‾|"
            textdecordown = "|_______>##<_______|"
        elif textdecornumberrouletteend == 2:   
            textdecorup   = "|‾‾‾‾‾‾>>##<<‾‾‾‾‾‾|"
            textdecordown = "|______>>##<<______|"
        else:   
            textdecorup   = "|‾‾‾‾‾>>>##<<<‾‾‾‾‾|"
            textdecordown = "|_____>>>##<<<_____|"

    if str(RouletteWheelNumbers[start_index+2:start_index+3]).translate(translationtable) != '':
        result = int(str(RouletteWheelNumbers[start_index+2:start_index+3]).translate(translationtable))
    else:
        result = 0
    result_color = str(RouletteWheelColors[start_index+2:start_index+3]).translate(translationtable)

    # Now, there might be a better way to implement this.
    # Now, I dont want to search for a better way to do this.
    # Now, enjoy this Yandere Dev teir code.
    
    try:
        if -1 < int(userinputroulette) < 37:
            if int(userinputroulette) == result:
                print("You won ", bet_roulette*5, " dollars ")
                money += bet_roulette*5
                wins_roulette += 1
                print("You gained 50 XP ")
                xp += 50
            else:
                print("You lost ", bet_roulette, " dollars ")
    except ValueError:
        
        if result == 0:
            try:
                if int(userinputroulette) == result:
                    print("You won ", bet_roulette*10, " dollars ")
                    money += bet_roulette*10
                    wins_roulette += 1
                    print("You gained 75 XP ")
                    xp += 75
            except ValueError: 
                if userinputroulette == "odd":
                    print("You won ", bet_roulette*2, " dollars ")
                    money += bet_roulette*2
                    wins_roulette += 1
                    print("You gained 15 XP ")
                    xp += 15
                else:
                    print("You lost ", bet_roulette, " dollars ")
                    
        elif userinputroulette == "1st12":
            if result < 13:
                print("You won ", bet_roulette*2, " dollars ")
                money += bet_roulette*2
                wins_roulette += 1
                print("You gained 15 XP ")
                xp += 15
            else:
                print("You lost ", bet_roulette, " dollars ")
        elif userinputroulette == "2nd12":
            if 12 < result < 25:
                print("You won ", bet_roulette*2, " dollars ")
                money += bet_roulette*2
                wins_roulette += 1
                print("You gained 15 XP ")
                xp += 15
            else:
                print("You lost ", bet_roulette, " dollars ")
        elif userinputroulette == "3rd12":
            if 24 < result:
                print("You won ", bet_roulette*2, " dollars ")
                money += bet_roulette*2
                wins_roulette += 1
                print("You gained 15 XP ")
                xp += 15
            else:
                print("You lost ", bet_roulette, " dollars ")
        elif userinputroulette == "odd":
            if is_odd(result):
                print("You won ", bet_roulette*2, " dollars ")
                money += bet_roulette*2
                wins_roulette += 1
                print("You gained 15 XP ")
                xp += 15
            else:
                print("You lost ", bet_roulette, " dollars ")
        elif userinputroulette == "even":
            if is_odd(result):
                print("You lost ", bet_roulette, " dollars ")
            else:
                money += bet_roulette*2
                print("You won ", bet_roulette*2, " dollars ")
                wins_roulette += 1
                print("You gained 15 XP ")
                xp += 15
        elif userinputroulette == "black":
            if result_color == "⬛":
                money += bet_roulette*2
                print("You won ", bet_roulette*2, " dollars ")
                wins_roulette += 1
                print("You gained 15 XP ")
                xp += 15
            else:
                print("You lost ", bet_roulette, " dollars ")
        elif userinputroulette == "red":
            if result_color == "🟥":
                money += bet_roulette*2
                print("You won ", bet_roulette*2, " dollars ")
                wins_roulette += 1
                print("You gained 15 XP ")
                xp += 15
            else:
                print("You lost ", bet_roulette, " dollars ")
        
        else:
            print("big error")


    time.sleep(2)

#Roulette()
def Slots():
    global money, wins_slots, merry_christmas
    print("\033[H\033[J", end="")
    print("🎰 Welcome to slots 🎰")
    print("Slots is a game where the goal is to roll the same symbols multiple times for a payout")
    print(f"\nCurrent balance: {money}")
    print("Enter your bet or say \"Payout\" for the payout table")
    while True:
        try:
            input_payout_or_bet = input()
            bet_slots = int(input_payout_or_bet)
            if -1 < bet_slots < money+1:
                money -= bet_slots
                break
            else:
                print("Please select a valid bet")
        except ValueError:
            if input_payout_or_bet.lower() == "payout":
                #"❌", "🍒", "🔔", "🍋", "💎"
                print("= Payout table =")
                print("❌ - Empty slot")
                print("🍒🍒 - 1.25x")
                print("🍋🍋 - 1.5x")
                print("🔔🔔 - 1.75x")
                print("💎💎 - 2x")
                print("🍒🍒🍒 - 3x")
                print("🍋🍋🍋 - 4x")
                print("🔔🔔🔔 - 5x")
                print("💎💎💎 - 10x")
                print("Enter your bet or say \"Payout\" for the payout table")
            else:
                print("Please select a valid bet")
            if input_payout_or_bet.lower() == "merry christmas":
                if merry_christmas == True:
                    print("Merry christmas and happy new year")
                    money += 100
                    merry_christmas = False
    
    slot_one = "💎"
    slot_two = "💎"
    slot_three = "💎"
    print("\033[H\033[J", end="")

    
    random_time = random.randint(20,25)
    
    for _ in range(random_time):
        print("\033[H", end="")
        print("+==============+")
        print(f"| {slot_one} | {slot_two} | {slot_three} |")
        print("+==============+")
        slot_one = random.choice(SlotSymbols)
        slot_two = random.choice(SlotSymbols)
        slot_three = random.choice(SlotSymbols)
        time.sleep(0.25)
    for _ in range(5):
        print("\033[H", end="")
        print("+=##===========+")
        print(f"| {slot_one} | {slot_two} | {slot_three} |")
        print("+=##===========+")
        slot_two = random.choice(SlotSymbols)
        slot_three = random.choice(SlotSymbols)
        time.sleep(0.25)
    for _ in range(5):
        print("\033[H", end="")
        print("+=##===##======+")
        print(f"| {slot_one} | {slot_two} | {slot_three} |")
        print("+=##===##======+")
        slot_three = random.choice(SlotSymbols)
        time.sleep(0.25)
    print("\033[H", end="")
    print("+=##===##===##=+")
    print(f"| {slot_one} | {slot_two} | {slot_three} |")
    print("+=##===##===##=+")
    time.sleep(0.25)

    def win_slots(slot):
        global money,xp
        decor_value = 1
        xpwin = 1
        if slot == "🍒":
            money += bet_slots*1.25
            youwon = bet_slots*1.25
            xpwin += 3
        elif slot == "🍋":
            money += bet_slots*1.5
            youwon = bet_slots*1.5
            xpwin += 4
        elif slot == "🔔":
            money += bet_slots*1.75
            youwon = bet_slots*1.75
            xpwin += 5
        elif slot == "💎":
            money += bet_slots*2
            youwon = bet_slots*2
            xpwin += 10
        elif slot == "🍒2":
            money += bet_slots*3
            youwon = bet_slots*3
            xpwin += 10
        elif slot == "🍋2":
            money += bet_slots*4
            youwon = bet_slots*4
            xpwin += 15
        elif slot == "🔔2":
            money += bet_slots*5
            youwon = bet_slots*5
            xpwin += 20
        elif slot == "💎2":
            money += bet_slots*10
            youwon = bet_slots*10
            xpwin = 25
        else:
            print("som mes up")
        for _ in range(12):
            decor_print = "/"
            decor_1 = "/"
            decor_2 = "|"
            decor_3 = "\\"
            if decor_value == 1 or decor_value == 4 or decor_value == 7 or  decor_value == 10:
                decor_print = decor_1
                decor_value += 1
            elif decor_value == 2 or decor_value == 5 or decor_value == 8 or  decor_value == 11:
                decor_print = decor_2
                decor_value += 1
            else:
                decor_print = decor_3
                decor_value += 1
            print("\033[H", end="")
            print("+=##===##===##=+")
            print(f"| {slot_one} | {slot_two} | {slot_three} |")
            print("+=##===##===##=+")
            print(decor_print, " You won ", youwon, " dollars ", decor_print)
            print(decor_print, " You gained ", xpwin," XP ", decor_print)

            xp += xpwin
            time.sleep(0.2)
    wins_slots += 1

    def lost_slots():
        decor_value = 1
        for _ in range(7):
            if decor_value == 1:
                print("\033[H", end="")
                print("x=##===##===##=x")
                print(f"| {slot_one} | {slot_two} | {slot_three} |")
                print("x=##===##===##=x")
                print("\\ You lost ", bet_slots, " dollars /")
                decor_value += 1
            else:
                print("\033[H", end="")
                print("+=##===##===##=+")
                print(f"| {slot_one} | {slot_two} | {slot_three} |")
                print("+=##===##===##=+")
                print("  You lost ", bet_slots, " dollars  ")
                decor_value -= 1
            time.sleep(0.5)
    if slot_one == slot_two or slot_one == slot_three or slot_two == slot_three:

        if slot_one == slot_two == slot_three:
            if slot_two == "🍒":
                win_slots("🍒2")
            elif slot_two == "🍋":
                win_slots("🍋2")
            elif slot_two == "🔔":
                win_slots("🔔2")
            elif slot_two == "💎":
                win_slots("💎2")
        else:
            if slot_one == "🍒":
                win_slots("🍒")
            elif slot_one == "🍋":
                win_slots("🍋")
            elif slot_one == "🔔":
                win_slots("🔔")
            elif slot_one == "💎":
                win_slots("💎")
    else:
        lost_slots()
    time.sleep(2)


def Keno():
    global money, wins_keno, xp
    print("\033[H\033[J", end="")
    print("🍀 Welcome to keno 🍀\n")
    print("Keno is a game where you choose numbers from a set between 1 and 60, and win prizes based on how many of\nyour chosen numbers match those drawn randomly (Which is different 20 numbers). You can bet up to 20 numbers at once (More guesses = Bigger payout)")
    print(f"\nCurrent balance: {money}")
    print("Enter your bet or say \"Payout\" for the payout table")
    

    # Picks: {mistake count: multiplier, mistake count: multiplier, mistake count: multiplier, mistake count: multiplier, }
    payout_keno = { 
        1: {0: 1.5},
        2: {0: 1.6, 1: 1.15},
        3: {0: 1.8, 1: 1.15, 2: 1},
        4: {0: 2, 1: 1.2, 2: 1.1, 3: 1},
        5: {0: 2.5, 1: 1.5, 2: 1.2, 3: 1},
        6: {0: 3, 1: 2, 2: 1.5, 3: 1.2, 4: 1},
        7: {0: 3.5, 1: 2, 2: 1.5, 3: 1.2, 4: 1.1, 5: 1},
        8: {0: 4, 1: 3.5, 2: 3, 3: 1.5, 4: 1.2, 5: 1.1, 6: 1},
        9: {0: 4.5, 1: 4, 2: 3.5, 3: 2, 4: 1.5, 5: 1.1, 6: 1},
        10: {0: 5, 1: 4.5, 2: 4, 3: 2, 4: 1.5, 5: 1.2, 6: 1.1, 7: 1},
        11: {0: 7, 1: 6, 2: 5, 3: 4, 4: 1.5, 5: 1.2, 6: 1.1, 7: 1},
        12: {0: 8, 1: 7, 2: 6, 3: 5, 4: 2, 5: 1.2, 6: 1.1, 7: 1},
        13: {0: 9, 1: 8, 2: 7, 3: 4, 4: 2, 5: 1.2, 6: 1.1, 7: 1},
        14: {0: 10, 1: 9, 2: 8, 3: 5, 4: 2, 5: 1.2, 6: 1.15, 7: 1},
        15: {0: 15, 1: 10, 2: 9, 3: 6, 4: 2, 5: 1.2, 6: 1.15, 7: 1},
        16: {0: 25, 1: 15, 2: 10, 3: 7, 4: 2, 5: 1.2, 6: 1.15, 7: 1},
        17: {0: 40, 1: 25, 2: 15, 3: 8, 4: 2, 5: 1.2, 6: 1.15, 7: 1},
        18: {0: 50, 1: 40, 2: 25, 3: 15, 4: 2, 5: 1.5, 6: 1.3, 7: 1},
        19: {0: 75, 1: 50, 2: 25, 3: 10, 4: 5, 5: 2.5, 6: 2, 7: 1},
        20: {0: 100, 1: 75, 2: 50, 3: 25, 4: 10, 5: 5, 6: 2.5, 7: 1.5, 8: 1},
    }
    while True:
        try:
            bet_keno = input()
            bet_keno_int = int(bet_keno)
            if bet_keno_int > money or 0 > bet_keno_int:
                print("Please select a valid bet")
            else:
                break
        except ValueError:
            if bet_keno.lower() == "payout":
                print("1 pick: 0 mistakes = 1.5x  |                   |                   |")
                print("2 picks: 0 mistakes = 1.6x | 1 mistake = 1.15x |                   |")
                print("3 picks: 0 mistakes = 1.8x | 1 mistake = 1.15x | 2 mistakes = 1x   |")
                print("4 picks: 0 mistakes = 2x   | 1 mistake = 1.2x  | 2 mistakes = 1.1x | 3 mistakes = 1x")
                print("5 picks: 0 mistakes = 2.5x | 1 mistake = 1.5x  | 2 mistakes = 1.2x | 3 mistakes = 1x")
                print("6 picks: 0 mistakes = 3x   | 1 mistake = 2x    | 2 mistakes = 1.5x | 3-4 mistakes = 1.2-1x")
                print("7 picks: 0 mistakes = 3.5x | 1 mistake = 2x    | 2 mistakes = 1.5x | 3-5 mistakes = 1.2-1x")
                print("8 picks: 0 mistakes = 4x   | 1 mistake = 3.5x  | 2 mistakes = 3x   | 3-6 mistakes = 1.5-1x")
                print("9 picks: 0 mistakes = 4.5x | 1 mistake = 4x    | 2 mistakes = 3.5x | 3-6 mistakes = 2-1x")
                print("10 picks: 0 mistakes = 5x  | 1 mistake = 4.5x  | 2 mistakes = 4x   | 3-7 mistakes = 2-1x")
                print("11-20 picks: Multiplier increases with higher picks, max 100x for 0 mistakes in 20 picks.")
            else:
                print("Please select a valid number")
    print("Select your chosen numbers (in a format of \"1, 2, 3\".)")
    while True:
        user_input_keno = input()
        try:
            chosen_number_list = [int(x.strip()) for x in user_input_keno.split(",")]
            if all(1 <= number <= 60 for number in chosen_number_list) and len(chosen_number_list) <= 10:
                print("Valid numbers:", chosen_number_list)
                break
            else:
                print("One or more of your numbers is out of range.")

        except ValueError:
            print("Invalid choise or format")
    
    NumbersPicked = []

    money -= bet_keno_int

    print("\033[H\033[J", end="")
    while True:
        while True:
            a = random.randint(1, 60)
            if a not in NumbersPicked:
                NumbersPicked.append(a)
                break
        test = str(NumbersPicked)
        print("\033[H", end="")
        print("Numbers which you have picked: [", user_input_keno, "]")
        print("Numbers randomally chosen: ", NumbersPicked)

        if len(NumbersPicked) == 20:
            break
        time.sleep(0.5)

    matches = set(chosen_number_list).intersection(NumbersPicked)
    num_matches = len(matches)
    num_picks = len(chosen_number_list)
    num_mistakes = num_picks - num_matches

    payout_for_num_picks = payout_keno.get(num_picks, {})
    reward_multiplier = payout_for_num_picks.get(num_mistakes, 0)


    money += bet_keno_int * reward_multiplier
    
    print("You won ", bet_keno_int*reward_multiplier, " dollars")
    print("You gained ", 2*reward_multiplier," XP")
    xp += 2*reward_multiplier
    if bet_keno_int*reward_multiplier > 0:
        wins_keno += 1
    time.sleep(2)
    print("\033[H\033[J", end="")

    
#keno()

def HorseBettin():
    global money, wins_horsebetting, xp
    print("\033[H\033[J", end="")
    round(money, 0)
    Horse1progressleft = ""
    Horse1progressright = "-------------------------------------------------"
    Horse2progressleft = ""
    Horse2progressright = "-------------------------------------------------"
    Horse3progressleft = ""
    Horse3progressright = "-------------------------------------------------"
    Horse4progressleft = ""
    Horse4progressright = "-------------------------------------------------"

    random_float_1 = round(random.uniform(1, 2), 2)
    random_float_2 = round(random.uniform(1, 2), 2)    
    
    print("🐎 Welcome to horse betting 🐎\n")
    print("The point of the game is to bet on the horse that will win the race\nYour winnings are calculated using the odds of winning (bet*odds)\n")
    print("Current odds:")
    print("Horse 1: ", round(random_float_1,2))
    print("Horse 2: ", round((random_float_2 + 0.15),2))
    print("Horse 3: ", round((random_float_1 + 0.15),2))
    print("Horse 4: ", round((random_float_2),2))
    print(f"\nCurrent balance: {money}")
    print("Pick a horse you will bet on")

    while True:
        try:
            horsiechooseinput = int(input())
            if 0 < horsiechooseinput < 5:
                break
            else:
                print("Please select a valid horse")
        except ValueError:
            print("Please select a valid number")

    print("How much will you bet?")

    while True:
        try:
            horsiebetinput = int(input())
            if -1 < horsiebetinput <= money:
                break
            else:
                print("Please select a valid bet")
        except ValueError:
            print("Please select a valid number")

    change_title = 1

    horsiewinner = ""
    print("\033[H\033[J", end="")
    while horsiewinner == "":
        if change_title <= 2:
            cooleffecthorsetexttitle = "-#- Race in progress -#- Race in progress -#- Race in progress -#-"
            change_title += 1
        else:
            cooleffecthorsetexttitle = "#-# Race in progress #-# Race in progress #-# Race in progress #-#"
            change_title += 1
        if change_title == 5:
            change_title = 1
        time.sleep(0.2)
        a = random.randint(1,4)
        if a == 1:
            Horse1progressleft += "-"
            Horse1progressright = Horse1progressright.replace("-", "", 1)
        if a == 2:
            Horse2progressleft += "-"
            Horse2progressright = Horse2progressright.replace("-", "", 1)
        if a == 3:
            Horse3progressleft += "-"
            Horse3progressright = Horse3progressright.replace("-", "", 1)
        if a == 4:
            Horse4progressleft += "-"
            Horse4progressright = Horse4progressright.replace("-", "", 1)
        print("\033[H", end="")
        print(cooleffecthorsetexttitle)
        print("Horse 1: [", Horse1progressleft, "🏇", Horse1progressright, "]")
        print("Horse 2: [", Horse2progressleft, "🏇", Horse2progressright, "]")
        print("Horse 3: [", Horse3progressleft, "🏇", Horse3progressright, "]")
        print("Horse 4: [", Horse4progressleft, "🏇", Horse4progressright, "]")
        print(cooleffecthorsetexttitle)

        if Horse1progressright == "":
            horsiewinner == "Horse 1"
            print("# Horse 1 won the race! #")
            if horsiechooseinput == 1:
                money += round(horsiebetinput*random_float_1, 0)
                wins_horsebetting += 1
                round(money, 0)
                print("You won ", horsiebetinput*random_float_1, " dollars")
                print("You gained 15 XP ")
                xp += 15
                break
            else:
                money -= horsiebetinput
                print("You lost ", horsiebetinput, " dollars")
                round(money, 0)
                break

        if Horse2progressright == "":
            horsiewinner == "Horse 2"
            print("# Horse 2 won the race! #")
            if horsiechooseinput == 2:
                money += round(horsiebetinput*random_float_2+0.15)
                wins_horsebetting += 1
                print("You won ", horsiebetinput*random_float_2+0.15, " dollars")
                print("You gained 15 XP ")
                xp += 15
                round(money, 0)
                break
            else:
                money -= horsiebetinput
                print("You lost ", horsiebetinput, " dollars")
                round(money, 0)
                break

        
        if Horse3progressright == "":
            horsiewinner == "Horse 3"
            print("# Horse 3 won the race! #")
            if horsiechooseinput == 3:
                money += round(horsiebetinput*random_float_1+0.15)
                wins_horsebetting += 1
                print("You won ", horsiebetinput*random_float_1+0.15, " dollars")
                print("You gained 15 XP ")
                xp += 15
                round(money, 0)
                break
            else:
                money -= horsiebetinput
                print("You lost ", horsiebetinput, " dollars")
                round(money, 0)
                break
        
        
        if Horse4progressright == "":
            horsiewinner == "Horse 4"
            print("# Horse 4 won the race! #")
            if horsiechooseinput == 4:
                money += round(horsiebetinput*random_float_2)
                wins_horsebetting += 1
                print("You won ", horsiebetinput*random_float_2, " dollars")
                print("You gained 15 XP ")
                xp += 15
                round(money, 0)
                break
            else:
                money -= horsiebetinput
                print("You lost ", horsiebetinput, " dollars")
                round(money, 0)
                break
    round(money, 0)
    print("Your current balance:", money)
    time.sleep(2)
    print("\033[H\033[J", end="")


def CasinoWar():
    global money, wins_casinowar, xp
    print("\033[H\033[J", end="")
    round(money, 0)
    print("⚓ Welcome to casino war ⚓\n")
    print("The point of the game is to receive a higher value card than your opponent.")
    print("If it's a tie, you can either surrender (losing half of your bet) or go into war \n(both receive yet another card. If your card is higher, you win; otherwise, you lose).\n")
    
    while True:
        try:
            print(f"\nCurrent balance: {money}")
            print("How much will you bet?")
            bet = int(input())
            if bet > -1 and bet <= money:
                break
            else:
                print("Please select a valid bet")
        except ValueError:
            print("Please choose a valid number")

    if bet > 0:
        if bet > money / 2:
            print("Caution: You have entered more than half of your money. You can't go into war. Proceed? (Y/N)")
            while True:
                proceed = input().upper()
                if proceed == "N":
                    return
                elif proceed == "Y":
                    break
                else:
                    print("Please choose 'Y' or 'N'.")
        print("\033[H\033[J", end="")
        
        
        picked_card_player = random.choice(list(cards.keys()))
        picked_card_dealer = random.choice(list(cards.keys()))
        
        card_value_player = cards[picked_card_player]
        card_value_dealer = cards[picked_card_dealer]
        print("Dealing cards...")
        time.sleep(1)
        print(f"Your card: \n[ {picked_card_player} ]")
        time.sleep(1)
        print(f"Dealer's card: \n[ {picked_card_dealer} ]")
        time.sleep(0.1)
        print("\033[H\033[J", end="")

        print(f"Your card: \n[ {picked_card_player} ]")
        print(f"Dealer's card: \n[ {picked_card_dealer} ]")

        time.sleep(1)
        
        
        if card_value_player > card_value_dealer:
            print(f"= You won {bet} dollars=")
            money += bet
            wins_casinowar += 1
            print("You gained 15 XP ")
            xp += 15
        elif card_value_player < card_value_dealer:
            print(f"\\ You lost {bet} dollars /")
            money -= bet
        else:
            print("You're tied!")
            print("1) Surrender\n2) Go into war")
            
            while True:
                try:
                    choice = int(input())
                    if choice == 1:
                        print("You surrendered.")
                        money -= (bet / 2)
                        break
                    elif choice == 2:
                        if money >= bet * 2:
                            print("You went into war!")
                            
                            picked_card_player_war = random.choice(list(cards.keys()))
                            picked_card_dealer_war = random.choice(list(cards.keys()))
                            
                            card_value_player_war = cards[picked_card_player_war]
                            card_value_dealer_war = cards[picked_card_dealer_war]
                            
                            print("\033[H\033[J", end="")
                            print("Dealing cards...")
                            time.sleep(1)

                            print(f"Your war card: \n[ {picked_card_player_war} ]")
                            time.sleep(1)
                            print(f"Dealer's war card: \n[ {picked_card_dealer_war} ]")
                            
                            if card_value_player_war >= card_value_dealer_war:
                                money += bet * 2
                                print(f"= You won {bet} dollars! =")
                                print("You gained 20 XP ")
                                xp += 20
                                round(money, 0)
                            else:
                                money -= bet * 2
                                print(f"\\ You lost {bet} dollars! /")
                                round(money, 0)
                        else:
                            print("You can't go into war as you do not have the required sum of money.")
                            money -= bet
                        break
                    else:
                        print("Please select a valid option.")
                except ValueError:
                    print("Please enter a valid choice (1 or 2).")
    round(money, 0)
    time.sleep(2)
    print("\033[H\033[J", end="")


def Coinflip():
    global money, wins_coinflip, xp
    print("\033[H\033[J", end="")
    round(money, 0)
    print("🪙 Welcome to coinflip 🪙")
    print("Guess the side which will land. If you guess it, you\nwill double your money. If not, you lose it")
    print(f"Current balance: {money}")
    print("How much will you bet?")
    while True:
        try:
            b = int(input())
            break
        except ValueError:
            print("Incorrect value")
    print("\033[H\033[J", end="")
    print("= Pick a Side =\n1) Heads\n2) Tails")

    leave = False

    while True:
        try:
            a = int(input())
            if a == 2 or a == 1:
                break
        except ValueError:
            print("Incorrect value")
        
    if leave != True:

        stringeffect = ""
        stringeffect2 = ""
        count = 0
        speed = 0
        while count < random.randint(9,10):
            print("\033[H\033[J", end="")
            print(stringeffect + "Tossing..." + stringeffect2)
            if count == 1 or count == 3 or count == 5 or count == 7 or count == 9:
                print("->  Heads  <-")
            else:
                print("->  Tails  <-")
            print(stringeffect + "Tossing..." + stringeffect2)
            if count == 3 or count == 6 or count == 9:
                stringeffect2 += "]"
                stringeffect += "["
            count += 1
            speed += 0.075
            time.sleep(speed)
        if count == 9:
            if a == 1:
                money = money+(b*2)
                print("You won ", b, "dollars!")
                print("You gained 10 XP ")
                xp += 10
                wins_coinflip += 1
            else:
                money = money-b
                print("You lost", b, "dollars!")
        else:
            if a == 1:
                money = money-b
                print("You lost", b, "dollars!")
            else:
                money = money+(b*2)
                wins_coinflip += 1
                print("You won ", b, "dollars!")
                print("You gained 10 XP ")
                xp += 10

#HorseBettin()
#keno()
#casinowar()
#Coinflip()
#input()

def stopper():
    global cashout, dead, coolstoppingargument
    while coolstoppingargument == False:
        input()
        cashout = True
        dead = False
        coolstoppingargument = True
        if coolstoppingargument == True:
            break



def Crash():
    global money, cashout, dead, coolstoppingargument, wins_crash,xp

    print("\033[H\033[J", end="")
    print("📈 Welcome to Crash 📈")
    print("The goal is to cash out before the game \"crashes,\" meaning the multiplier randomly stops,\ncausing those still in the game to lose their bets. \nThe longer you wait, the higher the potential payout, but with increased risk of losing everything.")

    while True:
        try:
            print(f"\nCurrent balance: {money}")
            print("How much will you bet?")
            bet = int(input())
            if bet > -1 and bet <= money:
                money -= bet
                break
            else:
                print("Please select a valid bet")
        except ValueError:
            print("Please choose a valid number")
    print("\033[H\033[J", end="")
    coolstoppingargument = False
    cashout = False
    multiplier = 0.80
    threading.Thread(target=stopper, daemon=True).start()
    
    while cashout == False:
        coolmultiplierrandomisation = random.randint(1, 14)
        multiplier = round(multiplier, 2)
        print("\033[H", end="")
        print("=== Crash ===")
        print("/=================\\")
        print(f"|Multiplier: {multiplier}x|")
        print("\\=================/")
        if coolmultiplierrandomisation == 1:
            dead = True
            cashout = True
        else: 
            multiplier = round(multiplier + 0.05, 2)
        time.sleep(0.25)
    if dead == True:
        print("Crash!")
        print("You lost", bet, " dollars")
        print("\nPress enter to continue")
        while coolstoppingargument == False:
            time.sleep(0.1)    # To whoever is reading this, DO NOT delete this part. If you do, it WILL crash
    else:
        print("You cashed out!")
        if multiplier > 1:
            print("You won ", bet*multiplier, " dollars")
            print("You gained ", 10*multiplier," XP")
            xp += 10*multiplier
            wins_crash += 1
        else:
            print("You lost ", bet-(bet*multiplier), " dollars")
        money += bet*multiplier
    coolstoppingargument = True
    time.sleep(2)

def dailyreward():
    global money, xp, lastrewardtime, json_datetime
    print("\033[H\033[J", end="")

    currenttime = datetime.now()
    try:
        lastrewardtime

    except NameError:
        try: 
            loaded_datetime = json.loads(json_datetime)
            lastrewardtime = datetime.fromisoformat(loaded_datetime["current_time"])
        except (json.JSONDecodeError, KeyError, ValueError)as e:
            lastrewardtime = datetime(year= 2020, month= 1, day= 1, hour= 1, minute= 1, second= 1, microsecond= 1)
            print("very bad", e)
    timediff = currenttime - lastrewardtime
    if timediff.days >= 1:
        print("Spin a wheel which gives you a random amount of money or XP.\nThe more levels that you have, the bigger the payout\n\nPress enter to continue")
        input()
        print("\033[H\033[J", end="")
        print("Your daily reward is...")
        decordaily = ""
        for _ in range(5):
            print("\033[H\033[J", end="")
            print("Your daily reward is...")
            print(f"[{decordaily}]")
            decordaily += "  "
            time.sleep(0.1)
        time.sleep(0.5)
        for _ in range(10):
            sleepytime = 0.1
            bigrandom = random.randint(1, 2)
            if bigrandom == 1:
                randmoney = random.choice(dailyrewardlistmoney)
                print("\033[H\033[J", end="")
                print("Your daily reward is...")
                print(f"[ {randmoney*level} $ ]")
            else:
                randxp = random.choice(dailyrewardlistXP)
                print("\033[H\033[J", end="")
                print("Your daily reward is...")
                print(f"[ {randxp*level} XP ]")
            sleepytime += 0.1
            time.sleep(sleepytime)
        if bigrandom == 1:
            money += randmoney
            print("\033[H\033[J", end="")
            print("Your daily reward is...")
            print(f"> {randmoney*level} $ <")
        else:
            xp += randxp
            print("\033[H\033[J", end="")
            print("Your daily reward is...")
            print(f"> {randxp*level} XP <")
        time.sleep(2)
        lastrewardtime = datetime.now()
    else:
        next_reward_time = lastrewardtime + timedelta(hours=24)
        
        formatted_next_reward_time = next_reward_time.strftime("%Y-%m-%d %H:%M:%S")
        print("You have already collected your daily reward\n")
        print("Please wait until ", formatted_next_reward_time)
        time.sleep(2)
        now_str = lastrewardtime.isoformat()
        json_datetime = json.dumps({"current_time": now_str})
def CasinoMenu():
    global cashout, dead, coolstoppingargument, username,xp,level,xptoreach
    while True:
        xptoreach = xptoreachbase*level
        while xp > xptoreach:
            print("Calculating your new level...")
            xp -= xptoreach
            level += 1
            print("\033[H\033[J", end="")

        print("\033[H\033[J", end="")
        save_game()
        print(f"Welcome to the Casino, {username}!")
        print("Which game would you like to play?\n")
        print("1.  Roulette")
        print("2.  Slots")
        print("3.  Horse Betting")
        print("4.  Casino War")
        print("5.  Coin Flip")
        print("6.  Crash")
        print("7.  Keno")
        print("8.  Stats")
        print("9.  Daily reward")
        print("10. Exit")
        while True:
            try: 
                choicemenu = int(input("\nSelect a number associated with the game.\n"))

                if choicemenu == 1:
                    Roulette()
                elif choicemenu == 2:
                    Slots()
                elif choicemenu == 3:
                    HorseBettin()
                elif choicemenu == 4:
                    CasinoWar()
                elif choicemenu == 5:
                    Coinflip()
                elif choicemenu == 6:
                    coolstoppingargument = True
                    cashout = False
                    dead = False
                    Crash()
                elif choicemenu == 7:
                    Keno()
                elif choicemenu == 8:
                    Stats()
                elif choicemenu == 9:
                    dailyreward()
                elif choicemenu == 10:
                    sys.exit()
                break
            except ValueError:
                print("Please select a valid option")


# This is designed for saving and loading. Remove the next 3 definitions to remove this feature, and end the script with CasinoMenu()


def save_game():
    global xptoreach, value1, legit, json_datetime

    value1 = money+xp+xptoreach+level+wins_roulette+wins_slots+wins_keno+wins_casinowar+wins_coinflip+wins_crash+wins_horsebetting

    game_state = {
        "money": money,
        "merry_christmas": merry_christmas,
        "username": username,
        "xp": xp,
        "xptoreach": xptoreach,
        "level": level,
        "wins_roulette": wins_roulette,
        "wins_slots": wins_slots,
        "wins_keno": wins_keno,
        "wins_casinowar": wins_casinowar,
        "wins_coinflip": wins_coinflip,
        "wins_crash": wins_crash,
        "wins_horsebetting": wins_horsebetting,
        "value1": value1,
        "legit": legit,
        "json_datetime": json_datetime
    }

    with open(save_file, 'w') as file:
        json.dump(game_state, file)

def load_game():
    global json_datetime, lastrewardtime, legit, value1, load_fail, money, merry_christmas, username, xp, xptoreach, wins_casinowar, wins_coinflip, wins_crash, wins_horsebetting, wins_keno, wins_roulette, wins_slots, level, username
    if os.path.exists(save_file):
        with open(save_file, 'r') as file:
            try:
                game_state = json.load(file)
                username = game_state["username"]
                money = game_state["money"]
                merry_christmas = game_state["merry_christmas"]
                username = game_state["username"]
                xp = game_state["xp"]
                xptoreach = game_state["xptoreach"]
                level = game_state["level"]
                wins_roulette = game_state["wins_roulette"]
                wins_slots = game_state["wins_slots"]
                wins_keno = game_state["wins_keno"]
                wins_casinowar = game_state["wins_casinowar"]
                wins_coinflip = game_state["wins_coinflip"]
                wins_crash = game_state["wins_crash"]
                wins_horsebetting = game_state["wins_horsebetting"]
                value1 = game_state["value1"]
                legit = game_state["legit"]
                json_datetime = game_state["json_datetime"]
            except Exception:
                print("You have an outdated or a corrupted save file!")
        if legit == True:
            if money+xp+xptoreach+level+wins_roulette+wins_slots+wins_keno+wins_casinowar+wins_coinflip+wins_crash+wins_horsebetting == value1:
                legit = True
            else:
                legit = False

        if legit == False: # ):
            print("I should have allowed you to change the odds \nof the games in the save file aswell, eh?")
            time.sleep(7)

        load_fail = False
    else:
        load_fail = True
        print("Cant find save file")
        time.sleep(0.1)
def pickusername():
    global username
    load_game()
    if load_fail == True:
        while True:
            print("\033[H\033[J", end="")
            print("You seem to be new here. Please enter your username.\n If you arent new, please restart this app")
            a = input()
            print("Are you sure? (Y/N)")
            b = input()
            if b.lower() == "y":
                break
        username = a
    CasinoMenu()

pickusername()