# Programmer : Teresa Fischer
# Date : 12/8/24
# Program # 2

import sqlite3

MIN_CHOICE = 1
MAX_CHOICE = 8
ASCENDING = 1
DESCENDING = 2
NAME = 3
TOTAL = 4
AVERAGE = 5
HIGHEST = 6
LOWEST = 7
EXIT = 8

def main():
    choice = 0
    if choice != EXIT:
        display_choices()
        choice = get_menu_choice()
        if choice == ASCENDING:
            ascending()
        elif choice == DESCENDING:
            descending()
        elif choice == NAME:
            name()
        elif choice == TOTAL:
            total()
        elif choice == AVERAGE:
            average()
        elif choice == HIGHEST:
            highest()
        elif choice == LOWEST:
            lowest()

# displays the choices for user
def display_choices():
     print('\n----- Operations -----')
     print('1. Display a list of cities sorted by population, in ascending order')
     print('2. Display a list of cities sorted by population, in descending order')
     print('3. Display a list of cites sorted by name')
     print('4. Display the total population of all the cites')
     print('5. Display the average popluation of all the cites')
     print('6. Display the city with the highest population')
     print('7. Display the city with the lowest population')
     print('8. Exit the program')

def get_menu_choice():
     choice = int(input('Enter a choice: '))
     print('\n')
     # Validate input
     while choice < MIN_CHOICE or choice > MAX_CHOICE:
         print(f'Valid choices are {MIN_CHOICE} through {MAX_CHOICE}. Please rerun and try again')
         break
     return choice

def fetch_data(query):
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    conn.close()
    return result

def display_results(results):
    for row in results:
        print(str(row))

def ascending():
    print('---- Cites sorted by Population in Ascending Order ----')
    query = "SELECT CityName, Population FROM Cities ORDER BY Population ASC"
    results = fetch_data(query)
    display_results(results)

def descending():
    print('---- Cites sorted by Population in Descending Order ----')
    query = "SELECT CityName, Population FROM Cities ORDER BY Population DESC"
    results = fetch_data(query)
    display_results(results)

def name():
    print('---- Cites sorted by Name ----')
    query = "SELECT CityName, Population FROM Cities ORDER BY CityName"
    results = fetch_data(query)
    display_results(results)

def total():
    print('Total Population of All the Cities:')
    query = "SELECT SUM(Population) FROM Cities"
    result = fetch_data(query)
    print(f'{result[0][0]} people')

def average():
    print('Average Population of All the Cities:')
    query = "SELECT AVG(Population) FROM Cities"
    result = fetch_data(query)
    print(f'{result[0][0]} people')

def highest():
    print('City with Highest Population:')
    query = "SELECT CityName, Population FROM Cities ORDER BY Population DESC LIMIT 1"
    result = fetch_data(query)
    print(f'{result[0]}')

def lowest():
    print('City with Lowest Population:')
    query = "SELECT CityName, Population FROM Cities ORDER BY Population ASC LIMIT 1"
    result = fetch_data(query)
    print(f'{result[0]}')


# instance of main()
if __name__ == '__main__':
    main()
