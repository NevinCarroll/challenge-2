"""
This file runs the main code for the Montana County Lookup. It allows the user to type a license plate
prefix and see which county it comes from and its seat city.
"""

counties = {} # Dictionary that stores up county data for lookup

def import_counties():
    """
    Import county data from csv file and put it in counties dictionary.
    :return:
    """
    global counties
    file = open('MontanaCounties.csv', 'r')

    next(file) # Skip first line
    # Read each line, using license plate prefix for key, and store county name and seat city as an array
    # as the value
    for line in file:
        split = line.split(',')
        county = [split[0], split[1]]
        counties[int(split[2])] = county

if __name__ == '__main__':
    import_counties() # Populate counties dictionary

    print("Welcome to the Montana County Lookup!")

    # Run as long as the user wants to lookup counties
    running = True
    while running:
        # Rest choice every time
        processing_choice = True
        user_choice = 0
        while processing_choice:
            # Let user decide which information they want to lookup
            print("If you want county name, type (n), if you want seat city, type (c), if you want both, type (nc)")
            output_type = input("")

            # Check if valid output type
            if output_type.lower() not in ["n", "c", "nc"]:
                print("Please enter either (n), (c), or (nc)")
                break

            # Ask user for license plate prefix
            print("Enter the license plate prefix (1-56) of the Montana county you want to look up. Or type (0) to quit.")
            user_choice = input("")

            # Check if choice is actually an integer
            try:
                user_choice = int(user_choice)
            except ValueError:
                print("Please enter a number between 1-56.")
                continue

            # Check if choice is valid, either quitting program or displaying choice if valid
            if user_choice == 0:
                running = False
                break
            elif user_choice < 1 or user_choice > 56:
                print("Please enter a number between 1-56.")
                break
            else:
                processing_choice = False

            # Output the information the user wanted
            if output_type.lower() == "n":
                print(f"County Name: {counties[user_choice][0]}")
            elif output_type.lower() == "c":
                print(f"County Seat City: {counties[user_choice][1]}")
            else:
                print(f"County Name: {counties[user_choice][0]}\nSeat City: {counties[user_choice][1]}")

