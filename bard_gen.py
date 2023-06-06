import random
import csv

def generate_file(file_name):
  """Generates a 1GB file with the specified file name.

  Args:
    file_name: The path to the output file.
  """

  with open(file_name, 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['id', 'integer1', 'string1', 'string2'])

    for i in range(1, 10**9):
      id = i
      integer1 = random.randint(1, 10)
      string1 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(1, 32)))
      string2 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(1, 32)))

      writer.writerow([id, integer1, string1, string2])

if __name__ == '__main__':
  file_name = 'source.csv'
  generate_file(file_name)
