import csv
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def generate_file(file_path, size_gb):
    row_count = int(size_gb * 1024 * 1024 * 1024 / 64)  # Assuming each row is approximately 64 bytes
    header = ['id', 'integer1', 'string1', 'string2']

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(header)

        for i in range(1, row_count + 1):
            integer1 = random.randint(1, 10)
            string1 = generate_random_string(random.randint(1, 32))
            string2 = generate_random_string(random.randint(1, 32))
            writer.writerow([i, integer1, string1, string2])

    print(f"Generated file '{file_path}' with approximately {size_gb}GB.")

# Example usage: generate_file('source.csv', 1)  # Generates a 1GB file

