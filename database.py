# This module handles everything related to the bot's MySQL database
import mysql.connector

db=mysql.connector.connect(host="localhost",
                           user="Kalle",
                           passwd="kalle",
                           database="meetings",
                           auth_plugin='mysql_native_password')
datacursor=db.cursor()

# Checks if a query using the given name returns anything
def row_exists(name):
    query = "SELECT name FROM Meetings WHERE name = " + "'" + name + "'"
    datacursor.execute(query)
    return datacursor.fetchall() != []

# Inserts a new person into the leaderboard data table or increments their "total" value by 1.
def add_data(name):
    if row_exists(name):
        query = "UPDATE Meetings SET total = total + 1 WHERE name = %s"
        datacursor.execute(query, (name,))
    else:
        query = "INSERT INTO Meetings VALUES (%s, %s)"
        datacursor.execute(query, (name, 1))
    db.commit()

# Prints the 10 people with the most meetings chaired.
def print_top10():
    message = ""
    datacursor.execute("SELECT * FROM Meetings ORDER BY total ASC")
    number = 1
    for i in datacursor:
        # i[0] = name and i[1] = total (amount of meetings chaired)
        new_row = str(number) + ". " + i[0] + ": " + str(i[1]) + "\n"
        message = message + new_row
        number = number + 1
        if number > 10:
            break
    return message






