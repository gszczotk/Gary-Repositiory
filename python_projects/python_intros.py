print("hello world!")

# Loops

# iterates from 0 to (a-1), works like a standard for loop incrementing by 1
a = 5
for i in range(a):
    print(i)

nums = [10,20,30,40,50]
for i in range(len(nums)):
    print(nums[i])

# for each loop equivalent
for num in nums:
    print(num)

# first variable gets index value, second variable is value at the index
for i, val in enumerate(nums):
    print("i is", i, "and val is", val)

dogs = ["boomer", "rocky", "daisy", "cooper"]
for dog in dogs:
    print(dog)
for i in range(len(dogs)):
    print(dogs[i])
for i, dog in enumerate(dogs):
    print("index is", i, "and the dog's name is", dog)

to_sum = [5,10,15,20,25]
sum = 0
for val in to_sum:
    sum += val
print("The sum of all the values in to_sum is",sum)
print(f"the sum of to_sum is {sum}")

# functions
def hello(name = "friend"):
    print("Hello " + name + "!")
hello("Gary")
hello() # calls default parameter

# Strings
fname = 'Gary'
lname = "Szczotka"

# to embed one type of quote inside a string, enclose it in the other type
print("She's a great dancer.")
print('He said "Hi" to his friend.')

# use the str function to convert numbers to strings before concatenation:
fullname = fname + " " + lname
print(fullname)

first_char = fname[0]
print("The first letter of my first name is " + first_char)
# negative indexes start at the end with -1

name_3 = fname * 3
print(name_3)

platform_computing = "platform computing"
platform = platform_computing[0:8]
computing = platform_computing[9:18]
print(platform + " " + computing)

# no value before colon defaults to 0, and no value after the colon defaults to -1
platform = platform_computing[:8]
computing = platform_computing[9:]
print(platform + " " + computing)

#swapping values in an array
nums = [0,3,8,5,4]
print(nums)
temp = nums[2]
nums[2] = nums[4]
nums[4] = temp
print(nums)