from sys import argv, exit
from cs50 import SQL

# Check for correct usage
if len(argv) == 1:
    print('roster.py missing command-line argument\nUsage: python roster.py example-house')
    exit(1)
elif len(argv) > 2:
    print('roster.py only accepts one command-line argument\nUsage: python roster.py example-house')
    exit(2)

# Assign house argument to a variable
house = argv[1].capitalize()

# Connect to the database
db = SQL('sqlite:///students.db')

# Return a list of students in the specified house from the roster
results = db.execute('SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first', house)

# Iterate through the results and print each row in a format
for row in results:
    # Check for middle names
    if row['middle']:
        print(f"{row['first']} {row['middle']} {row['last']}, born {row['birth']}")
    else:
        print(f"{row['first']} {row['last']}, born {row['birth']}")

exit(0)