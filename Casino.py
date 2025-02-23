import random
import time
import threading
import sys
import os
import json
import datetime
from datetime import datetime, timedelta
import hashlib

os.system("title " + "Let's go gambling! dududu ehh. God damn it!")

# GAMES


RouletteWheelNumbers = [" 0","32","15","19"," 4","21"," 2","25","17","34"," 6","27","13","36","11","30"," 8","23","10"," 5","24","16","33"," 1","20","14","31"," 9","22","18","29"," 7","28","12","35"," 3","26"]
RouletteWheelColors =  ["🟩", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛", "🟥", "⬛" ]
RouletteRed =          [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
RouletteBlack =        [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

SlotSymbols = ["❌", "🍒", "🔔", "🍋", "🍒", "🔔", "🍋", "💎"] # Intended for Slot Mashines

# Keno.             No list to implement
# Horse betting.    No list to implement

cards = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13} # Casino war

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
wins_blackjack = 0
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

    print(f"Blackjack wins:     {wins_blackjack}")
    print(f"Roulette wins:      {wins_roulette}")
    print(f"Slots wins:         {wins_slots}")
    print(f"Keno wins:          {wins_keno}")
    print(f"Horse betting wins: {wins_horsebetting}")
    print(f"Casino war wins:    {wins_casinowar}")
    print(f"Coinflip wins:      {wins_coinflip}")
    print(f"Crash wins:         {wins_crash}\n")

    print(f"Press enter to exit")
    input()

def Blackjack():
    global money, wins_blackjack, dealer_turn_end, player_turn_end
    print("\033[H\033[J", end="")
    print("🃏 Welcome to blackjack 🃏")
    print("The goal of blackjack is to have a hand value closer to 21 than the dealer's without exceeding 21.")
    print(f"\nCurrent balance: {money}")
    print("Enter your bet.")
    while True:
        try:
            input_bet = input()
            bet_blackjack = int(input_bet)
            if -1 < bet_blackjack < money+1:
                money -= bet_blackjack
                break
            else:
                print("Please select a valid bet")
        except ValueError:
            print("Please select a valid number")
    dealer_cards = []
    player_cards = []
    dealer_cards_num = []
    player_cards_num = []

    def add_card(person):
        random_card = random.choice(list(cards.keys()))
        random_cards_value = cards[random_card]
        if person == "player":
            player_cards.append(random_card)
            player_cards_num.append(random_cards_value)
        else:
            dealer_cards.append(random_card)
            dealer_cards_num.append(random_cards_value)

    dealer_turn_end = False

    def dealer_AI():
        global dealer_turn_end, player_turn_end
        if sum(dealer_cards_num) < 17:
            add_card("dealer")
            time.sleep(0.25)
        else:
            dealer_turn_end = True

    def lose_game_blackjack():
        global money
        time.sleep(0.25)
        print("You lost", bet_blackjack, "dollars!")
    def win_game_blackjack():
        global money
        time.sleep(0.25)
        money += bet_blackjack*2
        print("You won", bet_blackjack, "dollars!")

    def tie_game_blackjack():
        global money
        time.sleep(0.25)
        money += bet_blackjack
        print("Tie! You didnt win any money!")

    ended = False
    player_turn_end = False
    def add_first_cards():
        add_card("player")
        add_card("player")
        add_card("dealer")
    add_first_cards()
    while sum(player_cards_num) > 21:
        
        dealer_cards = []
        player_cards = []
        dealer_cards_num = []
        player_cards_num = []
        add_first_cards()
    hitorstand = "N/A"
    while not ended:
        time.sleep(0.1)
        dealer_cards_question_marks = ""
        for i in range(len(dealer_cards)-1): # Probably not the best way to do it, but adds the question marks next to the "Dealer's cards: " text minus one
            dealer_cards_question_marks += " ?"
        def mainmenu():
            print("\033[H\033[J", end="")
            print(f"🃏===🃏===🃏===🃏===🃏===🃏===🃏")
            print(f"Your cards: {', '.join(player_cards)} (Value: {sum(player_cards_num)})")
            print(f"Dealer's cards: {dealer_cards[0]}{dealer_cards_question_marks}")
            print(f"🃏===🃏===🃏===🃏===🃏===🃏===🃏")
        if sum(player_cards_num) > 21:
            player_turn_end = True
            hitorstand = "N/A"
        mainmenu()
        if not player_turn_end:
            print(f"1) Hit")
            print(f"2) Stand")
            hitorstand = input()
        if hitorstand == "1":
            add_card("player")
        if hitorstand == "2":
            player_turn_end = True
        mainmenu()
        dealer_AI()
        
        if dealer_turn_end and player_turn_end: # Win/lose scenarios
            time.sleep(0.25)
            print("\033[H\033[J", end="")
            print("🃏==========================🃏")
            print(f"Your cards: {', '.join(player_cards)} (Value: {sum(player_cards_num)})")
            print(f"Dealer's cards: {', '.join(dealer_cards)} (Value: {sum(dealer_cards_num)})")
            print("🃏==========================🃏")
            if sum(player_cards_num) == sum(dealer_cards_num):
                tie_game_blackjack()
            if sum(player_cards_num) < sum(dealer_cards_num) <= 21:
                lose_game_blackjack()
            elif sum(player_cards_num) > 21:
                lose_game_blackjack()
            elif sum(dealer_cards_num) > 21:
                win_game_blackjack()
            elif sum(dealer_cards_num) < sum(player_cards_num) <= 21:
                win_game_blackjack()
            ended = True
    time.sleep(2)
    print("\033[H\033[J", end="")

def Roulette():
    global money, wins_roulette, xp

    def WinRoulette(winmultiplier, winxp):
        global money, wins_roulette, xp    
        money += bet_roulette*winmultiplier
        print("You won ", bet_roulette*winmultiplier, " dollars ")
        wins_roulette += 1
        print(f"You gained {winxp} XP ")
        xp += winxp
    
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
    print("| 1st 12 | 2nd 12 | 3rd 12  |")
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

    for i in range(random.randint(15, 51)): # if you change this to 1 ( eg. for testing), youll get the result 15. The default is random.randint(15, 51)
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

    # <del>Holy Yandere Dev.</del> Not anymore :)
    
    expected_inputs = ["1st12", "2nd12", "3rd12"]
    conditions = [13, 25, 37]
    won_roulette = False
    try:
        if int(userinputroulette) == result:
            if result == 0:
                WinRoulette(10, 75)
            else:
                WinRoulette(5, 50)
    except ValueError:
        for index in range(3):
            if userinputroulette == expected_inputs[index] and result < conditions[index]:
                WinRoulette(2, 15)
                won_roulette = True
                
        if userinputroulette == "odd" and is_odd(result) or userinputroulette == "even" and not is_odd(result):
            WinRoulette(2, 15)
        elif userinputroulette == "black" and result_color == "⬛" or userinputroulette == "red" and result_color == "🟥":
            WinRoulette(2, 15)
        elif won_roulette == False:
            print("You lost ", bet_roulette, " dollars ")

    time.sleep(2)


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
    
    def menu(decor = "==", decor2 = "==", decor3 = "=="):
        print(f"+={decor}==={decor2}==={decor3}=+\n| {slot_one} | {slot_two} | {slot_three} |\n+={decor}==={decor2}==={decor3}=+")

    for _ in range(random_time):
        print("\033[H", end="")
        menu()
        slot_one = random.choice(SlotSymbols)
        slot_two = random.choice(SlotSymbols)
        slot_three = random.choice(SlotSymbols)
        time.sleep(0.25)
    for _ in range(5):
        print("\033[H", end="")
        menu("##")
        slot_two = random.choice(SlotSymbols)
        slot_three = random.choice(SlotSymbols)
        time.sleep(0.25)
    for _ in range(5):
        print("\033[H", end="")
        menu("##", "##")
        slot_three = random.choice(SlotSymbols)
        time.sleep(0.25)
    print("\033[H", end="")
    menu("##", "##", "##")
    time.sleep(0.25)

    def win_slots(slot):
        global money,xp, wins_slots, xpwin, youwon
        decor_value = 1
        xpwin = 0

        def win_win_slots(winmultiplier, winxp):
            global money,xp, wins_slots, xpwin, youwon
            money += bet_slots*winmultiplier
            youwon = bet_slots*winmultiplier
            xpwin += winxp


        conditions = ["🍒", "🍋", "🔔", "💎", "🍒2", "🍋2", "🔔2", "💎2"]
        MoneyMultiplier = [1.25, 1.5, 1.75, 2, 3, 4, 5, 10]
        XpMultiplier = [3, 4, 5, 10, 10, 15, 20, 25]
        for index in range(8):
            if slot == conditions[index]:
                win_win_slots(MoneyMultiplier[index], XpMultiplier[index])
        for _ in range(12):
            decor_print = "/"
            decor_1 = "/"
            decor_2 = "|"
            decor_3 = "\\"
            if decor_value == 1 or decor_value == 4 or decor_value == 7 or  decor_value == 10:
                decor_print = decor_1
            elif decor_value == 2 or decor_value == 5 or decor_value == 8 or  decor_value == 11:
                decor_print = decor_2
            else:
                decor_print = decor_3
            decor_value += 1
            print("\033[H", end="")
            menu("##", "##", "##")
            print(decor_print, " You won ", youwon, " dollars ", decor_print)
            print(decor_print, " You gained ", xpwin," XP ", decor_print)
            time.sleep(0.15)

        xp += xpwin
        time.sleep(0.2)
        wins_slots += 1

    def lost_slots():
        decor_value = 1
        end_screen1 = f"x=##===##===##=x\n| {slot_one} | {slot_two} | {slot_three} |\nx=##===##===##=x\n\\ You lost , {bet_slots}, dollars /"
        end_screen2 = f"+=##===##===##=+\n| {slot_one} | {slot_two} | {slot_three} |\n+=##===##===##=+\n  You lost , {bet_slots}, dollars  "
        for _ in range(7):
            if decor_value == 1:
                print("\033[H", end="")
                print(end_screen1)
                decor_value += 1
            else:
                print("\033[H", end="")
                print(end_screen2)
                decor_value -= 1
            time.sleep(0.5)
    if slot_one == slot_two or slot_one == slot_three or slot_two == slot_three:

        if slot_one == slot_two == slot_three:
            if slot_two != "❌":
                win_slots(f"{slot_two}2")
            
        elif slot_one == "❌" and slot_two == "❌" or slot_two == "❌" and slot_three == "❌" or slot_three == "❌" and slot_one == "❌":
            lost_slots()
        else:
            if slot_two != "❌":
                win_slots(f"{slot_two}")
    
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

    def winhorsebetting(horseinput, randfloat, horsiewinner):
        global money, wins_horsebetting, xp
        money += round((horseinput*randfloat), 0)
        wins_horsebetting += 1
        xp += 15
        print(f"# {horsiewinner} won the race! #")
        print("You won ", horseinput*randfloat, " dollars")
        print("You gained 15 XP ")

    def losehorsebetting(horseinput, horsiewinner):
        global money
        money -= horseinput
        print(f"\\ {horsiewinner} won the race! /")
        print(f"You lost {horseinput} dollars")
        round(money, 0)

    print("\033[H\033[J", end="")
    round(money, 0)
    Horse1progressleft = Horse2progressleft = Horse3progressleft = Horse4progressleft = ""
    Horse1progressright= Horse2progressright= Horse3progressright= Horse4progressright = "-------------------------------------------------"

    random_float_1 = round(random.uniform(1, 2), 2)
    random_float_2 = round(random.uniform(1, 2), 2)    
    random_float_3 = round(random.uniform(1, 2), 2)
    random_float_4 = round(random.uniform(1, 2), 2)    
    
    print("🐎 Welcome to horse betting 🐎\n")
    print("The point of the game is to bet on the horse that will win the race\nYour winnings are calculated using the odds of winning (bet*odds)\n")
    print("Current odds:")
    print("Horse 1: ", round(random_float_1,2))
    print("Horse 2: ", round((random_float_2),2))
    print("Horse 3: ", round((random_float_3),2))
    print("Horse 4: ", round((random_float_4),2))
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
    horseright = ["-------------------------------------------------" for _ in range(4)]
    horseleft = ["" for _ in range(4)]
    horses = ["Horse 1", "Horse 2", "Horse 3", "Horse 4"]
    floats = [random_float_1, random_float_2, random_float_3, random_float_4]
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
        a = random.randint(0,3)
        
        horseleft[a] += "-"
        horseright[a] = horseright[a].replace("-", "", 1)

        print("\033[H", end="")
        print(cooleffecthorsetexttitle)
        for i in range(4):
            print(f"{horses[i]}: [{horseleft[i]}🏇{horseright[i]}]")
        print(cooleffecthorsetexttitle)

        for index in range(4):
            if horseright[index] == "":
                horsiewinner = horses[index]
                if horsiechooseinput == index + 1:
                    winhorsebetting(horsiebetinput, floats[index], horsiewinner)
                    break
                else:
                    losehorsebetting(horsiebetinput, horsiewinner)
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
    
    def deal_cards():
        global card_value_dealer, card_value_player
        picked_card_player = random.choice(list(cards.keys()))
        picked_card_dealer = random.choice(list(cards.keys()))
        
        card_value_player = cards[picked_card_player]
        card_value_dealer = cards[picked_card_dealer]
        
        print("\033[H\033[J", end="")
        print("Dealing cards...")
        time.sleep(1)
        print(f"Your war card: \n[ {picked_card_player} ]")
        time.sleep(1)
        print(f"Dealer's war card: \n[ {picked_card_dealer} ]")
        time.sleep(0.1)
        print("\033[H\033[J", end="")
        print(f"Your card: \n[ {picked_card_player} ]")
        print(f"Dealer's card: \n[ {picked_card_dealer} ]")
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
        deal_cards()
        time.sleep(1)
        
        if card_value_player > card_value_dealer:
            print(f"= You won {bet} dollars =")
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
                            deal_cards()
                            if card_value_player >= card_value_dealer:
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
    def coinflipwin(b):
        global money, wins_coinflip, xp
        money = money+(b*2)
        wins_coinflip += 1
        print("You won ", b, "dollars!")
        print("You gained 10 XP ")
        xp += 10
    def coinfliplose(b):
        global money
        money = money-b
        print("You lost", b, "dollars!")
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

        stringeffect = stringeffect2 = result = ""
        count = speed = 0
        while count < random.randint(9,10):
            print("\033[H\033[J", end="")
            print(stringeffect + "Tossing..." + stringeffect2)
            if count == 1 or count == 3 or count == 5 or count == 7 or count == 9:
                print("->  Heads  <-")
                result = "heads"
            else:
                print("->  Tails  <-")
                result = "tails"
            print(stringeffect + "Tossing..." + stringeffect2)
            if count == 3 or count == 6 or count == 9:
                stringeffect2 += "]"
                stringeffect += "["
            count += 1
            speed += 0.075
            time.sleep(speed)
        if result == "heads":
            if a == 1:
                coinflipwin(b)
            else:
                coinfliplose(b)
        else:
            if a == 1:
                coinfliplose(b)
            else:
                coinflipwin(b)
    time.sleep(2)
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
    def menu():
        print("\033[H\033[J", end="")
        print("Your daily reward is...")
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
            
    timediff = currenttime - lastrewardtime
    if timediff.days >= 1:
        print("Spin a wheel which gives you a random amount of money or XP.\nThe more levels that you have, the bigger the payout\n\nPress enter to continue")
        input()
        menu()
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
                menu()
                print(f"[ {randmoney*level} $ ]")
            else:
                randxp = random.choice(dailyrewardlistXP)
                menu()
                print(f"[ {randxp*level} XP ]")
            sleepytime += 0.1
            time.sleep(sleepytime)
        if bigrandom == 1:
            money += randmoney*level
            menu()
            print(f"> {randmoney*level} $ <")
        else:
            xp += randxp*level
            menu()
            print(f"> {randxp*level} XP <")
        time.sleep(2)
        lastrewardtime = datetime.now()
        next_reward_time = lastrewardtime + timedelta(hours=24)
        formatted_next_reward_time = next_reward_time.strftime("%Y-%m-%d %H:%M:%S")
        now_str = lastrewardtime.isoformat()
        json_datetime = json.dumps({"current_time": now_str})
        save_game()
    else:
        next_reward_time = lastrewardtime + timedelta(hours=24)
        
        formatted_next_reward_time = next_reward_time.strftime("%Y-%m-%d %H:%M:%S")
        print("You have already collected your daily reward\n")
        print("Please wait until ", formatted_next_reward_time)
        time.sleep(2)
        now_str = lastrewardtime.isoformat()
        json_datetime = json.dumps({"current_time": now_str})
def CasinoMenu():
    global cashout, dead, coolstoppingargument, username, money, xp,level,xptoreach
    money = round(money)
    xp = round(xp)
    while True:
        xptoreach = xptoreachbase*level
        while xp >= xptoreach:
            print("Calculating your new level...")
            xp -= xptoreach
            level += 1
            print("\033[H\033[J", end="")
        xptoreach = xptoreachbase*level
        xp_filled_value = round((xp / xptoreach) * 20)
        xp_filled = ""
        for _ in range(xp_filled_value):
            xp_filled += '#'
        for _ in range(20 - xp_filled_value):
            xp_filled += '-'

        print("\033[H\033[J", end="")
        save_game()
        print(f"Welcome to the Casino, \033[1m{username}!\033[0m")
        print(f"Money:    {money}")
        print(f"Level:    {level}")
        print(f"XP:       {xp} / {xptoreach}")
        print(f"[{xp_filled}]\n")
        print("1) Blackjack")
        print("2) Roulette")
        print("3) Slots")
        print("4) Horse Betting")
        print("5) Casino War")
        print("6) Coin Flip")
        print("7) Crash")
        print("8) Keno")
        print("9) Daily reward\n")

        print("s) Stats")
        print("q) Exit")
        while True:
            try: 
                choicemenu = input("\nSelect an option: ")

                if choicemenu == "1":
                    Blackjack() 
                if choicemenu == "2":
                    Roulette()
                elif choicemenu == "3":
                    Slots()
                elif choicemenu == "4":
                    HorseBettin()
                elif choicemenu == "5":
                    CasinoWar()
                elif choicemenu == "6":
                    Coinflip()
                elif choicemenu == "7":
                    coolstoppingargument = True
                    cashout = False
                    dead = False
                    Crash()
                elif choicemenu == "8":
                    Keno()
                elif choicemenu == "9":
                    dailyreward()
                elif choicemenu == "s":
                    Stats()
                elif choicemenu == "q":
                    sys.exit()
                break
            except ValueError:
                print("Please select a valid option")

# This is designed for saving and loading. Remove the next 3 definitions to remove this feature, and end the script with CasinoMenu()

def save_game():
    global xptoreach, value1, legit, json_datetime, m
    m = hashlib.sha256(f"{money+xp+xptoreach+level+wins_roulette+wins_slots+wins_keno+wins_casinowar+wins_coinflip+wins_crash+wins_horsebetting}".encode())
    value1 = m.hexdigest()
    
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
        "wins_blackjack": wins_blackjack,
        "value1": value1,
        "legit": legit,
        "json_datetime": json_datetime
    }
    if legit == False:
        game_state["value1"] = "cheater"
        game_state["legit"] = False

    with open(save_file, 'w') as file:
        json.dump(game_state, file)

def load_game():
    global m, json_datetime, lastrewardtime, legit, value1, load_fail, money, merry_christmas, username, xp, xptoreach, wins_casinowar, wins_coinflip, wins_crash, wins_horsebetting, wins_keno, wins_roulette, wins_slots, level, username, wins_blackjack
    if os.path.exists(save_file):
        try:
            with open(save_file, 'r') as file:
                game_state = json.load(file)
                username = game_state.get("username", "N/A")
                money = game_state.get("money", 1000)
                merry_christmas = game_state.get("merry_christmas", True)
                xp = game_state.get("xp", 0)
                xptoreach = game_state.get("xptoreach", 0)
                level = game_state.get("level", 1)
                wins_roulette = game_state.get("wins_roulette", 0)
                wins_slots = game_state.get("wins_slots", 0)
                wins_keno = game_state.get("wins_keno", 0)
                wins_casinowar = game_state.get("wins_casinowar", 0)
                wins_coinflip = game_state.get("wins_coinflip", 0)
                wins_crash = game_state.get("wins_crash", 0)
                wins_horsebetting = game_state.get("wins_horsebetting", 0)
                wins_blackjack = game_state.get("wins_blackjack", 0)
                value1 = game_state["value1"]
                legit = game_state["legit"]
                json_datetime = game_state["json_datetime"]
            g = hashlib.sha256(f"{money+xp+xptoreach+level+wins_roulette+wins_slots+wins_keno+wins_casinowar+wins_coinflip+wins_crash+wins_horsebetting}".encode())
            new_value1 = g.hexdigest()
            if legit == True:
                if new_value1 == value1:
                    legit = True
                else:
                    legit = False
        except Exception as e:
            print(f"You have an outdated or a corrupted save file! Error {e} \n A value might be missing")
            time.sleep(3)
            sys.exit()

        if legit == False: # ):
            print("I should have allowed you to change the odds \nof the games in the save file aswell, eh?")
            time.sleep(7)
            if money > 999999999:
                print("Youre so greedy aswell...")
                money = 0
                time.sleep(3)
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
            print("You seem to be new here. Let's create you an account!\nYou will be prompted to pick an username. You can also quit this program with Ctrl+C.")
            a = input("Pick an username: ")
            print(f"Your username will {a}.")
            b = input("Proceed? (y/N) ")
            if b.lower() == "y" or b.lower == "yes":
                break
        username = a
    CasinoMenu()

pickusername()
