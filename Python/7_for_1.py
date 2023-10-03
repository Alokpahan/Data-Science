# Expenses total using simple sum
exp = [1200, 1300, 1400, 1500, 1600]
total1 = exp[0]+exp[1]+exp[2]+exp[3]+exp[4]
print("Total amount:", total1)

# Expense using for loop
print("for loop ")
total2 = 0
for i in exp:
    total2 = total2+i
print("Total amt:", total2)

# range() function
for j in range(1, 11):
    print(j)

# Print month number, expenses and then total with context of above exp list
total3 = 0
for k in range(len(exp)):
    print(f'month {k+1},expense: {exp[k]}')
    total3 = total3+exp[k]
print("Total Amt:", total3)


# break
# without using break
mobile_location = "table"
location = ['chair', 'bed', 'sofa', 'table', 'kitchen',]
for loc in location:
    if loc == mobile_location:
        print("Device found at: ", loc)
    else:
        print("Device not found at: ", loc)


print("\n")

# by using break
mobile_location = "sofa"
location = ['chair', 'bed', 'sofa', 'table', 'kitchen',]
for loc in location:
    if loc == mobile_location:
        print("Device found at: ", loc)
        break
    else:
        print("Device not found at: ", loc)

print("\n")

# continue: Print odd numbers between 1 to 20
for i in range(20):
    if i % 2 == 0:
        # eg 2%2 =0,then it will go for next iteration if it dont get == to zero then print(i) is executed.
        continue
    print(i)


print("\n")
# while
num = 0
while num <= 20:
    print(num)
    num = num+1
