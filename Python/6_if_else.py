# Using following list of cities per country,

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

# Write a program that asks user to enter a city name and it should tell which country the city belongs to

city=input("Enter a city name:")
city=str(city)
if city in india:
    print(f'{city} belong to india')
elif city in pakistan:
    print(f'{city} belong to pakistan')
elif city in bangladesh:
    print(f'{city} belongs to bangladesh')
else:
     print(f"I won't be able to tell you which country {city} is in! Sorry!")
     
#  Write a program that asks user to enter two cities and it tells you if they both are in same country or not. 
#  For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and 
#  dhaka it should print "They don't belong to same country"

print("Enter 2 cities:")
city1=input("1.")
city2=input("2.")
city1=str(city1)
city2=str(city2)
if city1 and city2 in india:
    print(f'{city1} and {city2} belong to india')
elif city in pakistan:
    print(f'{city1} and {city2} belong to pakistan')
elif city in bangladesh:
    print(f'{city1} and {city2} belongs to bangladesh')
else:
     print(f"They don't belong to same country")
     
     
     
# Write a python program that can tell you if your sugar is normal or not.Normal fasting level sugar range is 80 to 100.


# Ask user to enter his fasting sugar level
# If it is below 80 to 100 range then print that sugar is low
# If it is above 100 then print that it is high otherwise print that it is normal


s_level=input('Enter your fasting sugar level:')
s_level=int(s_level)

# ternary (conditional) expression
print("by using ternary cond:")
print("your sugar is low") if s_level<80 else print("its too high")  if s_level>100 else print("it is normal") 

# by using if .. else condtions
print("by using if else cond:")
if s_level<80:
    print("your sugar is low")
elif s_level>100:   
    print("its too high")
else:
    print("it is normal") 