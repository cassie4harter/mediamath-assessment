import random
import csv

# Create a file object for the output file
with open("source.csv", "w", newline="") as f:

    # Write the header row
    writer = csv.writer(f)
    writer.writerow(["id", "integer1", "string1", "string2"])

    # Generate 1GB of data
    for i in range(10000000):

        # Generate a random id
        id = i + 1

        # Generate a random integer
        integer1 = random.randint(1, 10)

        # Generate a random string
        string1 = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(1, 33))

        # Generate another random string
        string2 = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(1, 33))

        # Write the row to the file
        writer.writerow([id, integer1, string1, string2])

# Download the file to local storage
import requests

# Get the file URL
url = "https://raw.githubusercontent.com/bard/gen.py/main/source.csv"

# Download the file
response = requests.get(url)

# Save the file to local storage
with open("source.csv", "wb") as f:
    f.write(response.content)
