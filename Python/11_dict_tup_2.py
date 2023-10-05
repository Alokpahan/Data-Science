# You are given following list of stocks and their prices in last 3 days,

# Stock	Prices
# info	[600,630,620]
# ril	[1430,1490,1567]
# mtl	[234,180,160]

# Write a program that asks user for operation. Value of operations could be,
# print: When user enters print it should print following,
#        info ==> [600, 630, 620] ==> avg:  616.67
#        ril ==> [1430, 1490, 1567] ==> avg:  1495.67
#        mtl ==> [234, 180, 160] ==> avg:  191.33

# add: When user enters 'add', it asks for stock ticker and price.
#      If stock already exist in your list (like info, ril etc) then it will append the price to the list.
#      Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560]
#      to the dictionary of stocks.




# Import the statistics module to calculate the average
import statistics

# Dictionary to store stock information with stock symbols as keys and lists of prices as values
stocks = {'info': [600, 630, 620], 'ril': [1430, 1490, 1567], 'mtl': [234, 180, 160]}

# Function to print stock information, including the stock symbol, price list, and average price
def print_():
    for stock, price_list in stocks.items():
        # Calculate the average price using the statistics.mean() function
        avg = statistics.mean(price_list)
        # Print the stock symbol, price list, and average price (rounded to 2 decimal places)
        print(f'{stock} ==> {price_list} ==> avg:{round(avg, 2)}')

# Function to add a new price to a stock's price list
def add_():
    s = input("Enter a stock ticker to add:")
    p = input("Enter a price to add:")
    p = float(p)
    if s in stocks:
        stocks[s].append(p)
    else:
        stocks[s] = [p]
    # After adding the new price, call the print_() function to display updated information
    print_()

# Main program logic
def main():
    choice = input("Enter operation (P for print, A for add): ")
    choice = choice.lower()

    if choice == "p":
        print_()
    elif choice == "a":
        add_()
    else:
        print("Invalid option. Please try again...")

# Entry point of the program
if __name__ == '__main__':
    main()