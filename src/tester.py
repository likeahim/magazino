import csv

print(csv.list_dialects())
# with open('names.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'first_name': 'John', 'last_name': 'Doe'})
#     writer.writerow({'first_name': 'Steve', 'last_name': 'Boa'})
#     writer.writerow({'first_name': 'Mary', 'last_name': 'Black'})
with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['last_name'], row['first_name'])