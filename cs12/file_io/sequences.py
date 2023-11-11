# Arithmetic sequence counter
# Mr. Kuepfer
# 9/18/2023

# Reads a file containing a grid of numbers, and prints
# out the total number of rows and columns which form
# arithmetic sequences.

filename = 'sample_numbers.txt'

with open(filename, 'r') as file:
    data = file.readlines()

# Turn data into list of lists of numbers
num_grid = []
for line in data:
    row = []
    listline = line.split(' ')
    for num in listline:
        if num != '':
            row.append(int(num))
    num_grid.append(row)

# Accumulator to count arithmetic sequences found
total_sequences = 0

# Count rows that form arithmetic sequences
for row in num_grid:
    matches = 0
    first_diff = row[1] - row[0]
    # Difference between first two numbers must be the same as
    # the difference between all other pairs of numbers.
    if first_diff == 0:
        continue
    for i in range(len(row)-1):
        if row[i + 1] - row[i] == first_diff:
            matches += 1
    if matches == 3:
        total_sequences += 1

# Count columns that form arithmetic sequences
for i in range(len(num_grid[0])):
    matches = 0
    first_diff = num_grid[1][i] - num_grid[0][i]
    if first_diff == 0:
        continue
    for j in range(len(num_grid)-1):
        if num_grid[j+1][i] - num_grid[j][i] == first_diff:
            matches += 1
    if matches == 3:
        total_sequences += 1

print("Total sequences: " + str(total_sequences))