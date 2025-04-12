import csv

# Step 1: Open the CSV file
with open('people.csv', 'r') as file:
    reader = csv.DictReader(file) 

    print("CSV Data:")
    for row in reader:
        print(row)

# Step 2: Re-open to filter (or store in list and filter)
with open('people.csv', 'r') as file:
    reader = csv.DictReader(file)

    print("\nFiltered (Age > 25):")
    for row in reader:
        if int(row['age']) > 25:
            print(row)
