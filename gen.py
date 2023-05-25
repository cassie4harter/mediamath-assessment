import random
import csv

# Create a list of random integers
integers = [random.randint(1, 10) for _ in range(10000000)]

# Create a list of random strings
strings = [random.choice("abcdefghijklmnopqrstuvwxyz0123456789") for _ in range(10000000)]

# Create a list of tuples
tuples = [(i, s1, s2) for i, s1, s2 in zip(integers, strings, strings)]

# Write the tuples to a CSV file
with open("source.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "integer1", "string1", "string2"])
    writer.writerows(tuples)
