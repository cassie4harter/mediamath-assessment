!pip install boto3

import random
import csv
import boto3

def generate_data():
  """Generates a 1GB file with random data."""

  # Create a file object for the output file.
  with open("source.csv", "w", newline="") as f:

    # Write the header row to the file.
    writer = csv.writer(f)
    writer.writerow(["id", "integer1", "string1", "string2"])

    # Generate 1GB of random data.
    for i in range(1024 * 1024 * 1024):

      # Generate a random id.
      id = i + 1

      # Generate a random integer.
      integer1 = random.randint(1, 10)

      # Generate a random string.
      string1 = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(1, 33))

      # Generate another random string.
      string2 = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(1, 33))

      # Write the data to the file.
      writer.writerow([id, integer1, string1, string2])

if __name__ == "__main__":
  # Create a boto3 client for S3.
  s3 = boto3.client("s3")

  # Generate the data.
  generate_data()

  # Upload the file to the S3 bucket.
  s3.upload_file("source.csv", "random-data-cassie", "source.csv")
