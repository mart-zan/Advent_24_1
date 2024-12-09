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

# def remove_comprehensions(list_1, list_2, item):
#     # using list comprehension to perform the task
#     list_1 = [i for i in list_1 if i != item]
#     list_2 = [i for i in list_2 if i != item]
#     return list_1, list_2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Read and close file
    locations = read_input("input.txt")

    # ---------- TASK 1 ---------
    # Get columns separately, copy so it tays in "locations"
    locations_1 = locations[0].copy()
    locations_2 = locations[1].copy()
    # Initialize dist
    dist_out = 0
    # Run until the list is not empty
    while len(locations_1) > 0:
        locations_1, locations_2, dd = find_and_remove_min(locations_1, locations_2)
        # Compute the distance
        dist_out = dist_out + dd

    print("The final distance between the historically significant locations onj the lists in the Chief's office is " + str(dist_out) + ".")

    # ---------- TASK 2 ----------
    # Get columns separately
    locations_1 = locations[0]
    locations_2 = locations[1]
    # Initialize similarity score
    sim_score = 0
    # Get number from right list
    for i, item in enumerate(locations_1):
        sim_item = item*locations_2.count(item)
        # Count similarity score from assign
        sim_score = sim_score + sim_item

    print("The final similarity score between historically significant locations on the lists in the Chief's office is " + str(sim_score) + ".")
