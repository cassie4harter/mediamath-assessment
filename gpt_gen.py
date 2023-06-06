import csv
import random
import string

# Size of the file in bytes (1GB)
file_size = 1024 * 1024 * 1024

# Number of rows required to achieve the file size
row_size = 42  # Approximate row size in bytes (including newline character)
num_rows = file_size // row_size

# Open the output file
with open('source.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(['id', 'integer1', 'string1', 'string2'])
    
    # Generate and write the data rows
    for i in range(1, num_rows + 1):
        integer1 = random.randint(1, 10)
        string1 = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1, 32)))
        string2 = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1, 32)))
        writer.writerow([i, integer1, string1, string2])
