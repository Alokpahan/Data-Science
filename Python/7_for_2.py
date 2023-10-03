# After flipping a coin 10 times you got this result,
result = ["heads", "tails", "tails", "heads", "tails",
          "heads", "heads", "tails", "tails", "tails"]
# Using for loop figure out how many times you got heads

count = 0
output = "heads"
for coin in result:
    if coin == output:
        count = count+1
print("Heads count: ", count)

print("\n")

# Print square of all numbers between 1 to 10 except even numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i*i)

# Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ["January", "February", "March", "April", "May"]
user = input("Enter an expanse amount:")
user = int(user)

month = -1
for j in range(len(expense_list)):
    if user == expense_list[j]:
        month = j
        break

if month != -1:
    print(f'you spent {user} in {month_list[month]}')
else:
    print(f'you did not spent {user} in any month')


print("\n")
# Lets say you are running a 5 km race. Write a program that,

# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message


for k in range(5):
    print(f"You ran {k+1} miles")  # i starts with zero hence adding 1
    person = input("Are you tired ? ('yes' or 'no'): ")
    if person == 'yes':
        break
if k == 4:    # 4 because the index starts from 0
    print("Hurray! You are a rock star! You just finished 5 km race!")
else:
    print(
        f'You didn\'t finish 5 km race but hey congrats anyways! You still ran {k+1} miles')


print("\n")
# 5. Write a program that prints following shape
# ```
# *
# **
# ***
# ****
# *****
# ```

for l in range(1, 6):
    star = ''
    for m in range(l):
        star = star + '*'

    print(star)
