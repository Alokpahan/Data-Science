#  Read mode

f = open("text_1.txt", "r")
# for line in f:
#     print(line)
#       or
lines = f.readlines()
print(lines)

f.close()

#  Read mode without f.close()
print("by using 'with'")
with open("text_1.txt", "r") as f:
    for line in f:
        print(line)



# write mode

f = open("text_2.txt", "w")
f.write("Today is friday")
f.close()

#   or  by using  writelines
f = open("text_2.txt", "w")
f.writelines(["Today is friday\n","how is your day?\n","Its fine"])
f.close()


# Append mode

f = open("text_2.txt", "a")
f.write("\ngood morning")
f.close()

