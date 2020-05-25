from sys import argv, exit
from cs50 import SQL
from csv import DictReader

# Check for correct usage
if len(argv) == 1:
    print('import.py missing command-line argument\nUsage: python import.py example.csv')
    exit(1)
elif len(argv) > 2:
    print('import.py only accepts one command-line argument\nUsage: python import.py example.csv')
    exit(2)

# Assign file to variable
csv_file = argv[1]

# Connect to the database
db = SQL('sqlite:///students.db')

# Open the csv file
with open(f'{csv_file}', 'r') as students:
    # Create reader (returns rows of dicts)
    reader = DictReader(students)

    # Iterate over csv file
    for row in reader:
        # Analyze the name and return list
        name = row['name'].split(' ')
        # If the list is length 3, assign first, middle, last, otherwise, first, null, last
        if len(name) == 3:
            first = name[0]
            middle = name[1]
            last = name[2]
        else:
            first = name[0]
            middle = None
            last = name[1]
        # Execute query to insert data into the database
        db.execute('INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)', first, middle, last, row['house'], row['birth'])

    # Print on success
    print('Success. Information is loaded into students.db.')

exit(0)
