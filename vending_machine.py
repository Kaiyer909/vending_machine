#This part deals with storing information in a directory to refrence during the process.
items = [
    { 
    'code':1,
    'name':'chips',
    'value':2,
    },
    { 
        'code':2,
        'name':'soda',
        'value':3,
    },
    {
        'code':3,
        'name':'beef jerky',
        'value':5,
    },
        ]

is_quit = False
item = ''
# This part makes sure you can see what's in stock
while is_quit == False:
    print("Hello! Welcome to my virtual vending machine :) ")
    for i in items:
        print(f"Item Name: {i['name']} - value: {i['value']} - code:{i['code']}")
#As you can see this part asks for user input of what item they'll like
#It goes through the directory and gives you information from the exact code you entered
    query = int(input("please enter the code of the item youll like to purchase: "))
    for i in items:
        if query == i['code']:
            item = i
    if item == '':
        print('INVALID CODE')    
    else:                      #Here it'll show you how much your item costs and makes sure you pay up the excac amount
        print(f"{item['name']} will cost {item['value']} ")

        value = int(input(f"Please enter amount of {item['value']} here: "))
        if value == item['value']:
            print(f"Thank you! Now dispensing your item, enjoy!:D ")
        else:
            print(f"Pleae enter required amount :( ")
# this feature gives you the choice to continue ordering or to quit
query = input("If you'll like to quit, please input q or input any character to continue: ")
if query == 'c':
    is_quit = False
else:
    is_quit = True 
print('')

