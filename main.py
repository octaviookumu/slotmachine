import random


MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
  "A": 2,
  "B": 4,
  "C": 6,
  "D": 8
}

symbol_value = {
  "A": 5,
  "B": 4,
  "C": 3,
  "D": 2
}

def check_winnings(columns, lines, bet, values):
  winnings = 0
  winning_lines = []
  for line in range(lines): # looping through every row
    symbol = columns[0][line] # symbol in the first column of the current row
    for column in columns: # loop through every column and check for that symbol. if we get to the end without breaking out (meaning the symbols are the same) it means the user won, else: runs
      symbol_to_check = column[line] # symbol from column at the current row
      if symbol != symbol_to_check:
        break # we check the next line i.e [for line in range(lines) runs]
      # if you break the else statement doesn't run. - 
    else:  # if there's no break in the for loop the else statement runs
      winnings += values[symbol] * bet # the bet on each line. they could win on one line and lose on the other
      winning_lines.append(line + 1)

  return winnings, winning_lines

# what symbols are going to be in each column (generate items that will be in slot machine)
def get_slot_machine_spin(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items(): # e.g symbol A, symbol_count 2
    for _ in range(symbol_count): # loop through symbol_count i.e. 2
      all_symbols.append(symbol) # add symbol 2 times into all_symbols

  # select what values will go in every single column
  columns = [] # nested list represents value in column
  # for every column generate a certain number of symbols
  for _ in range(cols): # generate a column for every column we have
    # pick random values for each row in our column
    column = []
    current_symbols = all_symbols[:] # copy a list (slice operator)
    for _ in range(rows):
      value = random.choice(current_symbols)
      current_symbols.remove(value) # removes the value so we don't pick it again
      column.append(value) # add the value to column

    columns.append(column)

  return columns

def print_slot_machine(columns):
  # known as transposing
  # the number of rows is the number of elements in each column
  for row in range(len(columns[0])): # loop through every row
    for i, column in enumerate(columns): # for every row we loop through every column
      if i != len(columns) - 1:
        print(column[row], end=" | ")
      else:
        print(column[row], end="")
    print()


def deposit():
  while True:
    amount = input("What would you like to deposit? KES")

    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("Amount must be greater than 0.")
    else:
      print("Please enter a number.")

  return amount

def get_number_of_lines():
  while True:
    lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")

    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print("Please enter a valid number of lines.")
    else:
      print("Please enter a number.")
  return lines

def get_bet():
  while True:
    amount = input("What would you like to bet on each line? KES")
    if amount.isdigit():
      amount = int(amount)
      if MIN_BET <= amount <= MAX_BET:
        break
      else:
        print(f"Amount must be between KES{MIN_BET} - KES{MAX_BET}")
    else:
      print("Please enter a number.")
  return amount

def spin(balance):
  lines = get_number_of_lines()
  
  while True:
    bet = get_bet()
    total_bet = bet * lines

    if total_bet > balance:
      print(f"You do not have enough to bet that amount, current balance is: {balance}")
    else:
      break

  print(f"You are betting KES{bet} on {lines} lines. Total bet is equal to: KES{total_bet}")

  slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
  print_slot_machine(slots)
  winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
  print(f"You won KES{winnings}")
  print(f"You won on lines:", *winning_lines)
  return winnings - total_bet

def main():
  balance = deposit()
  while True:
    print(f"Current balance is KES{balance}")
    answer = input("Press enter to play (q to quit).")
    if answer == "q":
      break
    else:
      balance += spin(balance)

  print(f"You left with KES{balance}")

main()