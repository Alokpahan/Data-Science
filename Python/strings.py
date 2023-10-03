# Create 3 variables to store street, city and country, now create address variable to store entire address.
# Use two ways of creating this variable, one using + operator and the other using f-string.
# Now Print the address in such a way that the street, city and country prints in a separate line

street = "kanke road"
city = "ranchi"
country = "india"

address = street + '\n' + city + '\n' + country
print("Address using + operator:", address)

print(street+" "+city+" "+country)

address = f'{street}\n{city}\n{country}'
print("Address using f-string:", address)


# Create a variable to store the string "Earth revolves around the sun"
# Print "revolves" using slice operator
# Print "sun" using negative index

var = "Earth revolves around the sun"
print(var[6:14])
print(var[26:])
print(var[-3:])


# Create two variables to store how many fruits and vegetables you eat in a day.
# Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
# Use python f string for this.

num_fruits=10
num_veggies=5
print(f"I eat {num_fruits} veggies and {num_veggies} fruits daily")



# I have a string variable called s='maine 200 banana khaye'.
# This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'.
# Replace incorrect words in original strong with new ones and print the new string.
# Also try to do this in one line.

s='maine 200 banana khaye'
s=s.replace('200','10')
s=s.replace('banana','samosa')
print("Using two line replace:",s)

s=s.replace('banana','samosa').replace('200','10')
print("Using single line:",s)