# Country	Population
# China	143
# India	136
# USA	32
# Pakistan	21
# Write a program that asks user for three type of inputs
    # a. print: if user enter print then it should print all countries with their population in this format
    # b. add: if user input add then it should further ask for a country name to add. 
    #         If country already exist in our dataset then it should print that it exist and do nothing. 
    #         If it doesn't then it asks for population and add that new country/population in our dictionary and print it
    # c. remove: when user inputs remove it should ask for a country to remove. 
    #            If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). 
    #            Else print that country doesn't exist!
    # d. query: on this again ask user for which country he or she wants to query. 
    #           When user inputs that country it will print population of that country.
    
# countries = { 'china':'143','india':'136','usa':'32','pakistan':'21'}

# Initialize a dictionary to store countries as keys and their populations as values
countries = {'china': '143', 'india': '136', 'usa': '32', 'pakistan': '21'}

# Function to print the countries and their populations
def print_():
    for i in countries:
        print(i, "==>", countries[i])
        
#           or 

# Alternative implementation using dictionary items()
# def print_():
#     for i, country in countries.items():
#         print(i, "==>", country)

# Function to add a new country and its population
def add_():
    con = input("Enter country name:")
    con = str(con)
    if con in countries:
        print(f'{con} already exists, so no action taken!')
    else:
        pop = input(f'Enter the population of {con}:')
        pop = int(pop)
        countries[con] = pop
        print_()

# Function to remove a country
def remove_():
    con = input("Please provide country name:") 
    con = con.lower() 
    if con in countries:
        del countries[con]
        print_()
    else:
        print(f'{con} does not exist!')

# Function to query the population of a country
def query_():
    con = input("Please provide country name for query:")
    con = con.lower()
    if con in countries:
        print(f'{con} ==> {countries[con]}')
    else:
        print("Sorry, can't find any result, try again..")   

# Main program logic
def main():
    choice = input("Enter your choice: \n P for print, A for add, R for remove, and Q for query: ")
    choice = choice.lower()
    if choice == 'p':
        print_()
    elif choice == 'a':
        add_()
    elif choice == 'r':
        remove_()  
    elif choice == 'q':
        query_()  

# Entry point of the program
if __name__ == '__main__':
    main()
