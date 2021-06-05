# # 6. Write a Python program that reads a CSV file
# #    and remove initial spaces, quotes around each entry and the delimiter.

# import csv
# data_list = [
#     ['department_id', 'department_name', 'manager_id', 'location_id'],
#     [10, 'Administration', 200, 1700],
#     [20, 'Marketing', 201, 1800],
#     [30, 'IT', 202, 1900],
#     [40, 'Sales', 203, 2000],
#     [50, 'Finance', 204, 2100],
#     [60, 'Benefit', 205, 2200],
#     [70, 'Treasury', 206, 2300],
#     [80, 'Deposit', 207, 2400]
# ]

# csv.register_dialect('dialect_one', delimiter="\t",
#                      quoting=csv.QUOTE_ALL, quotechar="*")

# csv.register_dialect('dialect_two', delimiter="\t",
#                      quoting=csv.QUOTE_ALL, skipinitialspace=True)


# with open("csv/destinations4.csv", "w", newline="") as csv_file:

#     writer = csv.writer(csv_file, 'dialect_one')
#     writer.writerows(data_list)

# with open("csv/destinations4.csv", "r", newline="") as csv_file:

#     reader = csv.reader(csv_file, 'dialect_two')
#     for line in reader:
#         print(''.join(line))
