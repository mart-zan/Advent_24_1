import numpy as np

# Advent of Code 2024
# --- Day 1: Historian Hysteria ---

def find_and_remove_min(list_1, list_2):
    # Find minimum number
    min_column_1 = np.min(list_1)
    min_column_2 = np.min(list_2)
    # Remove minimum number
    list_1.remove(min_column_1)
    list_2.remove(min_column_2)
    # Compute distance
    dist = np.abs(min_column_1 - min_column_2)
    # Returns
    return list_1, list_2, dist

def read_input(filename: str):
    my_file = open(filename, "r")
    data = my_file.read()
    rows = data.strip().split('\n') # Split text into each row
    # Initialize
    column_1 = []
    column_2 = []
    # Find each two columns in each row
    for row in rows:
        values = row.split()  # Split each row by whitespace
        if len(values) == 2:
            column_1.append(int(values[0]))  # Add to column 1
            column_2.append(int(values[1]))  # Add to column 2
    my_file.close()
    # Returns
    return column_1, column_2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Read and close file
    locations = read_input("input.txt")
    locations_1 = locations[0]
    locations_2 = locations[1]
    # Initialize dist
    dist_out = 0
    # print(len(column_1)>0)
    # Run until the list is not empty
    while len(locations_1) > 0:
        result = find_and_remove_min(locations_1, locations_2)
        # print("d: " + str(dist_out))
        # print(result)
        # Compute the distance
        dist_out = dist_out + result[2]
        # Get new values without min
        locations_1 = result[0]
        locations_2 = result[1]

print("The final distance between the historically significant locations in the Chief's office is " + str(dist_out) + ".")
