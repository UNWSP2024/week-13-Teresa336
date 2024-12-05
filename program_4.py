# Programmer : Teresa Fischer
# Date : 12/8/24
# Program # 4

import sqlite3

MIN_CHOICE = 1
MAX_CHOICE = 4
READ = 1
UPDATE = 2
DELETE = 3
EXIT = 4


def main():
    choice = 0
    while choice != EXIT:
        display_menu()
        choice = get_menu_choice()
        if choice == READ:
            read()
        elif choice == UPDATE:
            update()
        elif choice == DELETE:
            delete()

def display_menu():
    print('\n----- Phonebook -----')
    print('1. Read a row')
    print('2. Update a row')
    print('3. Delete a row')
    print('4. Exit the program')


# get user input
def get_menu_choice():
    choice = int(input('Enter your choice: '))
    # validate the input.
    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print(f'Valid choices are {MIN_CHOICE} through {MAX_CHOICE}. Please rerun and try again.')
    return choice

def read():
    name = input('Enter a full name to search for: ')
    num_found = display_item(name)
    print(f'{num_found} row(s) found.')

def update():
    read()
    # get id of selected item
    selected_id = int(input('Type the Entry ID: '))
    # get new values
    name = input('Enter the new name: ')
    phone_number = input('Enter the new phone number: ')
    # update the row
    num_updated = update_row(selected_id, name, phone_number)
    print(f'{num_updated} row(s) updated.')

def delete():
    read()
    answer = input('Are you sure you want to delete this item? (y/n)')
    num = int(input('Type the Entry ID to confirm:'))
    if answer == 'y':
        num_deleted = delete_row(num)
        print(f'{num_deleted} row(s) deleted.')

def display_item(name):
    results = []
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('''SELECT * FROM Entries
                       WHERE lower(Name) == ?''',
                    (name.lower(),))
    results = cur.fetchall()

    for row in results:
        print(f'EntryID: {row[0]:<3} Name: {row[1]:<15} '
                  f'PhoneNumber: {row[2]:<6}')
    conn.close()
    return len(results)


def update_row(entry_id, name, phone_number):
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('''UPDATE Entries
                       SET Name = ?, PhoneNumber = ?
                       WHERE EntryID == ?''',
                    (name, phone_number, entry_id))
    conn.commit()
    num_updated = cur.rowcount
    conn.close()
    return num_updated

def delete_row(entry_id):
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    cur.execute('''DELETE FROM Entries
                       WHERE EntryID == ?''',
                    (entry_id,))
    conn.commit()
    num_deleted = cur.rowcount
    conn.close()
    return num_deleted


# Execute the main function.
if __name__ == '__main__':
    main()