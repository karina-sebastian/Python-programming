''' Write a program that repeatedly prompts the user to enter a number.
 If the user presses Ctrl+C, catch the KeyboardInterrupt exception and
 display a message indicating that the program was interrupted.'''
'''
try:
    while True:
        try:
            number = int(input("Enter a number: "))
            print("You entered:", number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
except KeyboardInterrupt:
    print("\n Program was interrupted.")
'''

'''2. Write a program that defines a dictionary with some key-value pairs. Prompt the user
to enter a key and then display the corresponding value.
Handle the case where the user enters a key that doesn't
exist in the dictionary by displaying an error message.'''

my_dict = {
    "platinum": "1",
    "jasmine": "jasmine is a flower",
    "apple": "apple is a fruit",
    "potato": "potato is a vegetable"
}

while True:
    key = input("Enter a key: ")
    
    try:
        value = my_dict[key]
        print("Value:", value)
    except KeyError:
        print("Key not found. Please enter a valid key.")
