import time

# Function to raise the mooring
def raise_mooring(depth, target_depth):
    while depth < target_depth:
        print(f"Raising mooring: Depth = {depth} meters")
        depth += 1
        time.sleep(1)  # Simulate the time it takes to raise by 1 meter

# Function to lower the mooring
def lower_mooring(depth, target_depth):
    while depth > target_depth:
        print(f"Lowering mooring: Depth = {depth} meters")
        depth -= 1
        time.sleep(1)  # Simulate the time it takes to lower by 1 meter

# Main function
def main():
    current_depth = 10  # Initial depth of the mooring in meters
    target_depth = 5  # Target depth in meters

    if current_depth > target_depth:
        lower_mooring(current_depth, target_depth)
    elif current_depth < target_depth:
        raise_mooring(current_depth, target_depth)
    else:
        print("Mooring is already at the target depth.")

if __name__ == "__main__":
    main()
