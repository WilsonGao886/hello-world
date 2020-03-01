##___________The First chapter..  print hello world  ___________#
#print("HEllo world!")   
#
##____________The Second variate  ___________#
#message = "Hello World!"
#print(message)
#message = "Hello Python Crash Course World!"
#print(message)
#
##____________ string _____________#
#name = "zhangfuhua lovelace"
#print(name.title())
#name = "ZHANGFUHUA LOVELACE"
#print(name.title())
#name = "ZHANgfuhua lovelaCE"
#print(name.upper())
#print(name.lower())
## merge #
#first_name = "ada"
#last_name = "lovelace"
#full_name = first_name + " " + last_name
#print(full_name)
#print(full_name.title())
## delete right null or left null
#favorite_language = '    Python is good language   '
#print(favorite_language)
#print(favorite_language.rstrip()) #delete right
#print(favorite_language.lstrip()) #delete left  
#print(favorite_language.strip())  #delete both    
## exercise #
#name = "Wei Gao"
#message = "Hello," + name + ",you are so nic!"
#print(message)
#print(name.title())
#print(name.upper())
#print(name.lower())
##________________________ number _________________#
#print(2 * 4)
#print(2 ** 3)
#print(2+6  )
#print(1+7 )
##___________________The Third  THE List ____________________#
##___________________The Forth Operation list__________________________#
#magicians = ['zhangfuha','zhoulun','fuhukai']
#for magician in magicians:
#    print(magician.title() + ", is handsome man.")
# create a list of values #
#for value in range(1,5):
#    print(value)
#numbers = list(range(1,5)) #create 1 to 4;
#print(numbers)
#even_numbers = list(range(2,11,2))  #form 2 to 11, always plus 2; 2 4 6 8 10
#print(even_numbers)
#squares = []       # create the square of 1 to 10 ;   1 4 9 16 25 ... 100
#for value in range(1,11):
#    squares.append(value**2)
#print(squares)
## list of analytical #
#squares = [value**2 for value in range(1,11)] # create the square of 1 to 10 ;   1 4 9 16 25 ... 100]
#print(squares)
# exercise #
for value in range(1,21):
    print(value)
numbers = list(range(1,1000001))
#print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
odd_numbers = list(range(1,21,2))
for odd_number in odd_numbers:
    print(odd_number)
print("\n")
numbers_plus3 = list(range(3,30,3))
for number in numbers_plus3:
    print(number)
print("\n")
cubes = [value**3 for value in range(1,11)]
print(cubes)
for cube in cubes:
    print(cube)
print("\n")










