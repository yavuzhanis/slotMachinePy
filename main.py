import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {"X": 9, "W": 8, "Z": 7, "A": 2}
symbol_values = {"X": 5, "W": 4, "Z": 3, "A": 6}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)
    return winnings, winning_lines


def getSlotMachineSpin(rows, cols, symbols):
    allSymbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            allSymbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        currentSymbols = allSymbols[:]
        for _ in range(rows):
            value = random.choice(currentSymbols)
            currentSymbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])
        print()


# Slot machine
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please entrer a number")

    return amount


def getNumberOfLines():
    while True:
        lines = input(
            "Enter the number of lines to bet on ? (1-" + str(MAX_LINES) + ")?"
        )

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please entrer a number")

    return lines


def getBet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET}- ${MAX_BET}")
        else:
            print("Please entrer a number")

    return amount


def spin(balance):
    lines = getNumberOfLines()
    while True:
        bet = getBet()
        totalBet = bet * lines
        if totalBet > balance:
            print(
                f"You do not have enough to bet that amount , your current balance is : ${balance}"
            )
        else:
            break

    print(
        f"You are betting $ {bet} on {lines} lines. Total bet is equal to : ${totalBet} "
    )
    slots = getSlotMachineSpin(ROWS, COLS, symbol_count)
    printSlotMachine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}.")
    print(f"You Won ON lines : ", *winning_lines)
    return winnings - totalBet


def main():
    balance = deposit()
    while True:
        print(f"Current Balance is : ${balance}")
        answer = input("Please enter to spin (q to Quit)")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You Left with ${balance}")


main()
