from Utility.Colour.colour import water
from Utility.Fruits.fruits import orange_fruit, blueberry, banana, strawberry, seven, raspberry
from os import system
from random import randint
import time
import sqlite3


# Cash class to manage player's credits and bets
class Cash:
    def __init__(self, credit=100, bet=2):
        self.credit = credit
        self.bet = bet
        self.bets = [2, 5, 10, 20]

    def change_bet(self):
        # Changes the bet amount by rotating the list of available bets
        self.bets.append(self.bets.pop(0))
        self.bet = self.bets[0]

    def charge(self):
        # Checks if the player has enough credit to place a bet and deducts the bet amount from the credit
        if self.bet <= self.credit:
            self.credit -= self.bet
            self.update_credit_in_db()
            return False
        else:
            machine.still()
            print('\n\t     Not enough credit to place a bet')
            time.sleep(2)
            return True

    def update_credit_in_db(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS credits (credit INTEGER)")

        cursor.execute("SELECT COUNT(*) FROM credits")
        result = cursor.fetchone()
        if result[0] == 0:
            cursor.execute("INSERT INTO credits (credit) VALUES (?)", (self.credit,))
        else:
            cursor.execute("UPDATE credits SET credit = ? WHERE rowid = 1", (self.credit,))

        conn.commit()
        conn.close()

    def load_credit_from_db(self):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS credits (credit INTEGER)")
        cursor.execute("INSERT OR IGNORE INTO credits (rowid, credit) VALUES (1, 100)")

        cursor.execute("SELECT credit FROM credits WHERE rowid = 1")
        result = cursor.fetchone()
        if result is not None:
            self.credit = result[0]
        conn.close()


# Slots class to manage the slot machine
class Slots:

    def __init__(self):
        # Slots class to manage the slot machine
        self.slot_one = [(strawberry, 2), (banana, 10), (blueberry, 3), (strawberry, 2), (raspberry, 5), (blueberry, 3),
                         (orange_fruit, 8), (seven, 15)]
        self.slot_two = [banana, strawberry, blueberry, orange_fruit, strawberry, blueberry, raspberry, seven]
        self.slot_three = [blueberry, strawberry, raspberry, orange_fruit, blueberry, strawberry, seven, banana]

    def roll(self):
        # Simulates the rolling of the slots

        a, b, c = 1, 1, 1
        while a % 6 != 0:
            a = randint(70, 110)
        while b % 6 != 0:
            b = randint(60, 90)
        while c % 6 != 0:
            c = randint(70, 100)

        i = 1
        for _ in range(a):
            system('cls')
            if i == 6:
                i = 0
                # After each 6 jumps of slots by single line first symbol of each slot list will be moved at the end
                self.slot_one.append(self.slot_one.pop(0))
                self.slot_two.append(self.slot_two.pop(0))
                self.slot_three.append(self.slot_three.pop(0))

            s1 = self.slot_one[0][0][i:] + self.slot_one[1][0] + self.slot_one[2][0] + self.slot_one[3][0][0:i]
            s2 = self.slot_two[0][i:] + self.slot_two[1] + self.slot_two[2] + self.slot_two[3][0:i]
            s3 = self.slot_three[0][i:] + self.slot_three[1] + self.slot_three[2] + self.slot_three[3][0:i]
            i += 1
            layout(s1, s2, s3)
            time.sleep(0.02)

        i = 1
        for _ in range(b):
            system('cls')
            if i == 6:
                i = 0
                self.slot_two.append(self.slot_two.pop(0))
                self.slot_three.append(self.slot_three.pop(0))

            s1 = self.slot_one[0][0] + self.slot_one[1][0] + self.slot_one[2][0]
            s2 = self.slot_two[0][i:] + self.slot_two[1] + self.slot_two[2] + self.slot_two[3][0:i]
            s3 = self.slot_three[0][i:] + self.slot_three[1] + self.slot_three[2] + self.slot_three[3][0:i]
            i += 1
            layout(s1, s2, s3)
            time.sleep(0.02)

        i = 1
        for t in range(c):
            system('cls')
            if i == 6:
                i = 0
                self.slot_three.append(self.slot_three.pop(0))

            s1 = self.slot_one[0][0] + self.slot_one[1][0] + self.slot_one[2][0]
            s2 = self.slot_two[0] + self.slot_two[1] + self.slot_two[2]
            s3 = self.slot_three[0][i:] + self.slot_three[1] + self.slot_three[2] + self.slot_three[3][0:i]
            i += 1
            layout(s1, s2, s3)
            time.sleep(0.02 + t ** 2 / 90000)

    def still(self):
        # Function composes states of slots while not moving and passes to print
        system('cls')
        fin1 = self.slot_one[0][0] + self.slot_one[1][0] + self.slot_one[2][0]
        fin2 = self.slot_two[0] + self.slot_two[1] + self.slot_two[2]
        fin3 = self.slot_three[0] + self.slot_three[1] + self.slot_three[2]
        layout(fin1, fin2, fin3)
        print('\n\t  [ENTER] Play   [B] Change bet   [Q] Quit ')

    def adding_credits(self, prize):
        # Adds credits to the player's account, 1 credit for prize times
        for _ in range(prize):
            self.still()
            money.credit += 1
            money.update_credit_in_db()
            time.sleep(0.03)


def win_amount():
    # function checks if a match in slots exist.
    if machine.slot_one[0][0] == machine.slot_two[0] == machine.slot_three[0]:
        return money.bet * machine.slot_one[0][1]
    elif machine.slot_one[1][0] == machine.slot_two[1] == machine.slot_three[1]:
        return money.bet * machine.slot_one[1][1]
    elif machine.slot_one[2][0] == machine.slot_two[2] == machine.slot_three[2]:
        return money.bet * machine.slot_one[2][1]
    elif machine.slot_one[0][0] == machine.slot_two[1] == machine.slot_three[2]:
        return money.bet * machine.slot_one[0][1]
    elif machine.slot_one[2][0] == machine.slot_two[1] == machine.slot_three[0]:
        return money.bet * machine.slot_one[2][1]
    else:
        return 0


def layout(s1, s2, s3):
    # Layout of graphical representation.
    print('\n\t   __________________________________________')
    print('\t  /                                         /|')
    print('\t /_________________________________________/ |')
    print('\t|                                         |  |')
    print('\t|       ____ ___  _ ____  _____ _____     |  |')
    print('\t|      /  __\\\  \///  __\/  __//__ __ \   |  |')
    print('\t|      |  \/| \  / | | //|  \    / \\      |  |')
    print('\t|      |  __/ / /  | |_\\\|  /_   | |      |  |')
    print('\t|      \_/   /_/   \____/\____\  \_/      |  |')
    print('\t|                                         |  |')
    print('\t|   -----------------------------------   |  |')
    for l, m, r in zip(s1, s2, s3):
        print('\t|  |', l, '|', m, '|', r, '|  |  |')
    print('\t|   -----------------------------------   |  |')
    print('\t|                                         |  |')
    print(f'\t|    BET  {money.bet:2}              CREDIT {money.credit:5}    |  |')
    print('\t|                                         | /')
    print('\t|_________________________________________|/')


def welcome():
    logo = water("""
 ________  ___    ___ ________  _______  _________   
|\   __  \|\  \  /  /|\   __  \|\  ___ \|\___   ___\ 
\ \  \|\  \ \  \/  / | \  \|\ /\ \   __/\|___ \  \_| 
 \ \   ____\ \    / / \ \   __  \ \  \_|/__  \ \  \  
  \ \  \___|\/  /  /   \ \  \|\  \ \  \_|\ \  \ \  \ 
   \ \__\ __/  / /      \ \_______\ \_______\  \ \__\\
    \|__||\___/ /        \|_______|\|_______|   \|__|
         \|___|/                                     
""")
    split = logo.splitlines()
    for line in split:
        print(line)
        time.sleep(0.1)
    time.sleep(1)


if __name__ == '__main__':
    system('cls')
    welcome()
    money = Cash()
    money.load_credit_from_db()
    machine = Slots()

    while True:
        machine.still()
        again = input('\n')
        if again == 'q':
            break
        elif again == 'b':
            money.change_bet()
            continue
        elif again == '':
            if money.charge():
                continue
            machine.roll()
            machine.adding_credits(win_amount())

    time.sleep(1)
    system('cls')