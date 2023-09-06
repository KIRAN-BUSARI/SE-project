import csv

# Open the CSV file in read mode
with open('data.csv', 'w') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)

    # Read the CSV file line by line
    lines = []
    for line in csv_reader:
        lines.append(line)

    # Write the list to a Python file
    with open('data.py', 'w') as py_file:
        py_file.write(str(lines))
