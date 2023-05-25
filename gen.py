import csv
import random
import string

# Define the number of rows required to reach approximately 1GB
target_file_size = 1 * 1024 * 1024 * 1024  # 1GB in bytes
row_size = 4 * (4 + 32 + 32) + 3  # 4 columns: id, integer1, string1, string2. Plus separators and newline characters.
num_rows = target_file_size // row_size

# Define the column names
columns = ['id', 'integer1', 'string1', 'string2']

# Create and open the CSV file
with open('source.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')

    # Write the header row
    writer.writerow(columns)

    # Write the data rows
    for i in range(1, num_rows + 1):
        integer1 = random.randint(1, 10)
        string1 = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 32)))
        string2 = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 32)))
        writer.writerow([i, integer1, string1, string2])
