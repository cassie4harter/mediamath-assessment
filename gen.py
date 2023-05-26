import random
import string
import csv
import boto3

# AWS S3 configuration
bucket_name = 'random-data-cassie'
output_file = 'source.csv'

# Generate a random string of given length
def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Generate CSV data
def generate_csv_data(num_rows):
    data = []
    for i in range(1, num_rows+1):
        row = [
            i,                             # id (auto-incrementing)
            random.randint(1, 10),         # integer1 (random number 1-10)
            generate_random_string(32),    # string1 (random characters of length 1-32)
            generate_random_string(32)     # string2 (random characters of length 1-32)
        ]
        data.append(row)
    return data

# Write CSV data to a file
def write_to_csv(data):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['id', 'integer1', 'string1', 'string2'])  # Header row
        writer.writerows(data)

# Upload file to S3 bucket
def upload_to_s3(filename):
    s3 = boto3.client('s3')
    s3.upload_file(filename, bucket_name, filename)

if __name__ == '__main__':
    desired_file_size = 1024 * 1024 * 1024  # 1GB
    row_size = 1 + 4 + 32 + 32  # Size of one row (in bytes)

    num_rows = desired_file_size // row_size

    data = generate_csv_data(num_rows)
    write_to_csv(data)
    upload_to_s3(output_file)

    print(f'{output_file} created and uploaded to {bucket_name} bucket.')
