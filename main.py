import random
import random as rand


MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

# value of machine
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(lines + 1)
    return winnings, winnings_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        deposito = input('¿Qué te gustaría depositar? $')
        if deposito.isdigit():
            deposito = int(deposito)
            if deposito > 0:
                break
            else:
                print('Introduzca un numero mayor a 0')
        else:
            print('Introduzca un numero')

    return deposito


def get_number_of_lines():
    while True:
        lines = input('¿Introduzca el numero de las lineas a las que quiere apostar (1-?' + str(MAX_LINE)+')? ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print('Introduzca un numero mayor a 0')
        else:
            print('Introduzca un numero')

    return lines


def get_bet():
    while True:
        bet = input('¿Introduzca caunto desea apostar apostar y en que linea? ')
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f'Introduzca un numero mayor a 0 ${MIN_BET} - ${MAX_BET}')
        else:
            print('Introduzca un numero')

    return bet


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total = bet * lines
        if total > balance:
            print(f'No dispones de suficiente dinero para apostar, su deposito actual es de: ${balance}')
        else:
            break
    print(f'Estas apostando: ${bet} en la linea {lines}. '
          f'Su total apuesta es de: ${total}')
    # generar las colunmas de nuestra maquina
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_line = check_winnings(slots, lines, bet, symbol_values)
    print(f'Usted gano ${winnings}.')
    print(f'Usted gano en la linea:', *winning_line)
    return winnings - total


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


if __name__ == '__main__':
    main()