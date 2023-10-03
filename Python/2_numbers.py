# You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.

length = 92
breadth = 48.8
area = length*breadth
print(round(area, 1))
print(round(area))


# You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar.
# Find out using python, how many dollars is the shopkeeper going to give you back?

packet = 9
each_packet_cost = 1.49
paid = 20
return_amt = (paid-(packet*1.49))
print(return_amt)


# You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.
# If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles.
# Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)

length = 5.5
area = length**2
cost = 500
total_cost = cost*area
print(total_cost)


# Print binary representation of number 17
number = 17
print(format(number, 'b'))
