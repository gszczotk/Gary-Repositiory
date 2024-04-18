try:
    num = int(input("Enter a number: "))
    num += 10
except:
    print("You did not enter a number.")

print("continue")

# you can change ending character of print statement by defining parameter end
print('The rain in Spain', end= ' ')
print('stays mainly in the plain.')

# f-strings allow to embed variables inside strings


# opening and using files
with open("movies.txt") as file:
    for line in file:
        line = line.strip() # gets rid of new line at the end of the string variable
        print(line)

with open("heights.txt") as file:
    for line in file:
        line = line.strip()
        lst = line.split() # every time empty space is found, string is split into seperate strings in a list
        print(lst)