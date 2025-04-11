'''
Generates the token for users for the below section based on user input:
P : Perfume Section
M : Medicine Section
G : Grocery Section
E : Exit
Usage of Decorator and Generator.
'''
import sys;

def perfume_gen():              # Generator for Perfume
    for i in range(1,100):
        yield f"P-{i}"

def medicine_gen():             # Generator for Medicine
    for i in range(1,100):
        yield f"M-{i}"

def grocery_gen():              # Generator for Grocery
    for i in range(1,100):
        yield f'G-{i}'

pnumber = perfume_gen()
mnum = medicine_gen()
gnum = grocery_gen()

def decor(user_input_func):   # user_input_func is generator object <class 'generator'>
    def inner():
        print("Your Token Number is ", )
        print(next(user_input_func))
        print("Wait for assistance")
    return inner

print("Welcome to Mall! Please select your section")
print("P : Perfume Section")
print("M : Medicine Section")
print("G : Grocery Section")
print("E : Exit")

while(True):
    user_input = input("Please Enter from above options ") 

    if (user_input == "P"):
        inner = decor(pnumber)
        inner()
    elif (user_input == "M"):
        inner = decor(mnum)
        inner()
    elif (user_input == "G"):
        inner = decor(gnum)
        inner()
    elif (user_input == "E"):
        print("Good Bye!")
        sys.exit()
    else:
        print("Wrong Character")
    