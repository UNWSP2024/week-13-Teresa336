# Programmer : Teresa Fischer
# Date : 12/8/24
# Program # 3

import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('phonebook.db')

    # Get a database cursor.
    cur = conn.cursor()

    # Add the Entries table.
    add_entries_table(cur)

    # Add rows to the entries table.
    add_entries(cur)

    # Commit the changes.
    conn.commit()

    # Display the entries.
    display_entries(cur)

    # Close the connection.
    conn.close()

# The add_entries_table adds the Entries table to the database.
def add_entries_table(cur):
    # If the table already exists, drop it.
    cur.execute('DROP TABLE IF EXISTS Entries')

    # Create the table.
    cur.execute('''CREATE TABLE Entries (EntryID INTEGER PRIMARY KEY NOT NULL,
                                        Name TEXT,
                                        PhoneNumber INTEGER)''')


# The add_entries function adds rows to the Entries table.
def add_entries(cur):
    phonebook_list = [(1, 'Teresa Fischer', 5072405348),
                  (2, 'John Smith', 1234567890),
                  (3, 'Lee Johnson', 2223334445),
                  (4, 'Bob Red', 1212121212),
                  (5, 'Joe Right', 9087865643)]

    for row in phonebook_list:
        cur.execute('''INSERT INTO Entries (EntryID, Name, PhoneNumber)
                       VALUES (?, ?, ?)''', (row[0], row[1], row[2]))


# The display_entries function displays the contents of
# the Entries table.
def display_entries(cur):
    print('Contents of phonebook.db/Entries table:')
    cur.execute('SELECT * FROM Entries')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]:.0f}')


# Execute the main function.
if __name__ == '__main__':
    main()