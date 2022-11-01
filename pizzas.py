# Name: Dwight Dart
# Prog Purpose: This program prepares a receipt for a Palermo Pizza customer's order.
#       Small Pizza:       $  9.99
#       Medium Pizza:      $ 12.99
#       Large Pizza:       $ 14.99
#       Extra Large Pizza: $ 17.99

import datetime

# pizza prices
SMALL_PIZZA_PRICE = 9.99
MEDIUM_PIZZA_PRICE = 12.99
LARGE_PIZZA_PRICE = 14.99
EXTRA_LARGE_PIZZA_PRICE = 17.99
SALES_TAX = .055

#define global variables
pizza_size = "" # S means Small, M means Medium, L means Large, X means Extra Large

small_pizza_count = 0
medium_pizza_count = 0
large_pizza_count = 0
extra_large_pizza_count = 0

total_small_pizza_cost = 0
total_medium_pizza_cost = 0
total_large_pizza_cost = 0
total_extra_large_pizza_cost = 0

subtotal = 0
total = 0
salestax = 0

###########    define program functions    ############
def main():
    another_pizza = True
    while another_pizza:
        get_user_data()
        perform_calculations()
        yesno = input("\nWould you like another delicious Palermo pizza? (Y/N): ")
        if yesno.upper() != "Y":
            another_pizza = False
            display_results()

def get_user_data():
    global pizza_size, small_pizza_count, medium_pizza_count, large_pizza_count, extra_large_pizza_count
    pizza_size = input('What size pizza would you like (S, M, L, X)?: ')
    if pizza_size.upper() == 'S':
        small_pizza_count += 1  
    if pizza_size.upper() == 'M':
        medium_pizza_count += 1
    if pizza_size.upper() == 'L':
        large_pizza_count += 1 
    if pizza_size.upper() == 'X':
        extra_large_pizza_count += 1
    
def perform_calculations():
    global total_small_pizza_cost, total_medium_pizza_cost, total_large_pizza_cost, total_extra_large_pizza_cost, subtotal, salestax, total
    total_small_pizza_cost = small_pizza_count * SMALL_PIZZA_PRICE
    total_medium_pizza_cost = medium_pizza_count * MEDIUM_PIZZA_PRICE
    total_large_pizza_cost = large_pizza_count * LARGE_PIZZA_PRICE
    total_extra_large_pizza_cost = extra_large_pizza_count * EXTRA_LARGE_PIZZA_PRICE
    subtotal = total_small_pizza_cost + total_medium_pizza_cost + total_large_pizza_cost + total_extra_large_pizza_cost
    salestax = subtotal * SALES_TAX 
    total = subtotal + salestax

def display_results():
    print('\n--------------------------------------------')
    print('          ******PALERMO PIZZA******')
    print('         YOUR NEIGHBORHOOD PIZZA SHOP')
    print('--------------------------------------------')
    print('         Small Pizzas       : ', small_pizza_count)
    print('         Medium Pizzas      : ', medium_pizza_count)
    print('         Large Pizzas       : ', large_pizza_count)
    print('         Extra Large Pizzas : ', extra_large_pizza_count)
    print('         Pizza Cost:        $', format(subtotal, '8,.2f'))
    print('         Sales Tax:         $', format(salestax, '8,.2f'))
    print('         Total:             $', format(total, '8,.2f'))
    print('--------------------------------------------')
    print('         ', str(datetime.datetime.now()))
    
################    call on main program to execute     ####################
main()