# lists
lst = [10,20,30,40,50]
lst.append(5)
lst.append(6)
lst.append(7)
print(lst)

lst.remove(40) # remove by value
print(lst)
lst.pop(2) # remove by index
print(lst)

lst.reverse()
print(lst)
lst.sort()
print(lst)

lst[0] = 500
print(lst)

lst = lst[1:]
print(lst)

index10 = lst.index(10)
print(index10)
lst.append(20)
lst.append(20)
lst.append(20)
print(lst)
count20 = lst.count(20) # number of times something appears in a list
print(count20)

copy_lst = lst # memory address is copied, not the list contents
print(copy_lst)
copy_lst[0] = 99
print(copy_lst)
print(lst)

new_copy = lst.copy()
print(new_copy)
new_copy[0] = 500
print(new_copy)
print(lst)

new_copy = lst[:] # also works to make copy
                  # deep copy needs to be used on list with objects

empty_lst = []
for val in lst: # loop to fill in values into an empty list
    empty_lst.append(val)
print(empty_lst)

# Create several copies of a value in a list on initialization
empty_lst = [0] * 10
print(empty_lst)

# list comprehension - compact progamming expression used to create a new list based on a sequence

# creation with for loop
squares = []
for i in range(1,10):
    squares.append(i*i)
print(squares)

# creation with comprehension
squares = [x*x for x in range(1,10)]
print(squares)

plus5 = [x+5 for x in lst]
print(plus5)

small_vals = [x for x in lst if x < 20]
print(small_vals)

# dictionaries - maps a set of keys to their values, like hashmaps in java
fav_foods = {"Kathleen" : "pizza", "Hannah" : "pasta", "Kush": "fries", "Yamill" : "fries"}
print(fav_foods)

hff = fav_foods["Hannah"]
print(hff)

for key in fav_foods:
    print(f"{key}'s favorite food is {fav_foods[key]}") # fstring allows us to embed variables within the string

for person, food in fav_foods.items():
    print(f"{person}'s favorite food is {food}")

# to check if key exists
if "Bob" in fav_foods:
    print(fav_foods["Bob"])
else:
    fav_foods["Bob"] = "wings"
print(fav_foods)