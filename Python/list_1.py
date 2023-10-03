mithai=['halva','kheer','jalebi','gulab jamun']

# print using +ve index

print(mithai[0])
print(mithai[1])
print(mithai[2])
print(mithai[3])
print('\n')

# print using -ve index

print(mithai[-1])
print(mithai[-2])
print(mithai[-3])
print(mithai[-4])
print('\n')

# print using slincing by range index

print(mithai[:])
print(mithai[:2])
print(mithai[0:2])
print(mithai[-4:])
print(mithai[-4:-3])
print(mithai[:0])
print(mithai[:-1])
print('\n')

# len() function
print(len('halva'))
print('\n')

# in operator
print('halva' in mithai)
print('samosa' in mithai)
print('\n')

# Append and insert functions
mithai.append('laduu')
print(mithai)

mithai.insert(1,'kulfi')
print(mithai)
print('\n')
#Adding two lists


tikha=['samosa','sev']
food=mithai+tikha
print(food)
print('\n')

# list items can be changed using index and slice index

mithai[0]='peda'
print(mithai)

mithai[0:2]='barfee'
print(mithai)
mithai[0:6]=['barfee']
print(mithai)
mithai[0:4]=['kaju kattli']
print(mithai)

mithai[0:1]=[5,6,7,8,9,0]
print(mithai)


# print(dir(mithai))