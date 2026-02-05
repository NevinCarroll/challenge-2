"""
This file runs the main code for the Montana County Lookup. It allows the user to type a license plate
prefix and see which county it comes from and its seat city.
"""
import csv

counties = {} # Dictionary that stores up county data for lookup
city_to_county = {} # Dictionary that store city as key and county number as value

def import_counties():
    """
    Import county data from csv file and put it in counties dictionary.
    :return:
    """
    with open('MontanaCounties.csv', newline='') as file:
        reader = csv.reader(file)
        next(reader) # Skip first line, since it is column names

        for row in reader:
            if len(row) == 3:  # Fill counties dictionary with counties names and seat cities
                county_name, seat_city, prefix = row
                counties[int(prefix)] = [county_name.strip(), seat_city.strip()]
                city_to_county[seat_city.strip()] = int(prefix)
            elif len(row) == 2: # Regular cities only have city name and license plate prefix
                city, prefix = row
                city_to_county[city.strip()] = int(prefix)

def add_city(city, license_plat_prefix):
    """
    Saves city to csv file, and add it to the city_to_county dictionary.
    """
    city_to_county[city] = license_plat_prefix
    county_data = [city, license_plat_prefix]

    # Write city data to csv file
    with open("MontanaCounties.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow(county_data)

def license_plate_lookup():
    """
    Lookup county and county seat city by license plate prefix (1-56)
    """
    processing_choice = True
    user_choice = 0

    while processing_choice:
        # Let user decide which information they want to lookup
        print("If you want county name, type (n), if you want seat city, type (c), if you want both, type (nc)")
        output_type = input("")

        # Check if valid output type
        if output_type.lower() not in ["n", "c", "nc"]:
            print("Please enter either (n), (c), or (nc)")
            continue

        looking = True
        while looking:
            # Ask user for license plate prefix
            print("Enter the license plate prefix (1-56) of the Montana county you want to look up.")
            user_choice = input("")

            # Check if choice is actually an integer
            try:
                user_choice = int(user_choice)
            except ValueError:
                print("Please enter a number between 1-56.")
                continue

            # Check if choice is valid, displaying choice if valid
            if user_choice < 1 or user_choice > 56:
                print("Please enter a number between 1-56.")
                continue
            else:
                processing_choice = False

            looking = False
            # Output the information the user wanted
            if output_type.lower() == "n":
                print(f"County Name: {counties[user_choice][0]}")
            elif output_type.lower() == "c":
                print(f"County Seat City: {counties[user_choice][1]}")
            else:
                print(f"County Name: {counties[user_choice][0]}\nSeat City: {counties[user_choice][1]}")

def city_lookup():
    """
    Lookup county and county seat city by city, if city is not in database, add it to the csv file
    and in memory storage
    """
    processing_choice = True
    user_choice = 0

    while processing_choice:
        # Let user decide which information they want to lookup
        print("If you want county name, type (n), if you want seat city, type (c), if you want both, type (nc)")
        output_type = input("")

        # Check if valid output type
        if output_type.lower() not in ["n", "c", "nc"]:
            print("Please enter either (n), (c), or (nc)")
            continue

        # Ask user for license plate prefix
        print("Enter the Montana city that you want to look up the county of.")
        user_choice = input("")

        city = user_choice.strip().lower().title() # Format city name

        # Check if city exists in database, if not allow user to add it to csv file
        if city not in city_to_county.keys():
            adding_city = True
            license_plate_prefix = ""
            while adding_city:
                print("Enter the license plate prefix (1-56) of the Montana county this city belongs to.")
                license_plate_prefix = input("")

                # Check if choice is actually an integer
                try:
                    license_plate_prefix = int(license_plate_prefix)
                except ValueError:
                    print("Please enter a number between 1-56.")
                    continue

                # Check if choice is valid, displaying choice if valid
                if license_plate_prefix < 1 or license_plate_prefix > 56:
                    print("Please enter a number between 1-56.")
                    continue
                else:
                    adding_city = False

            add_city(city, license_plate_prefix)
            print("Added city to csv file.")

        county_number = city_to_county[city]

        # Output the information the user wanted
        if output_type.lower() == "n":
            print(f"County Name: {counties[county_number][0]}")
        elif output_type.lower() == "c":
            print(f"County Seat City: {counties[county_number][1]}")
        else:
            print(f"County Name: {counties[county_number][0]}\nSeat City: {counties[county_number][1]}")

        processing_choice = False

if __name__ == '__main__':
    import_counties() # Populate counties dictionary

    # Run as long as the user wants to lookup counties
    running = True
    while running:
        # Rest choice every time
        user_choice = 0

        choosing_lookup = True

        while choosing_lookup:
            print("Do you want to search montana counties using a city (type 'c') or license prefix (type 'l')? If you want to quit type ('q')")
            user_choice = input("")

            # Quit program
            if user_choice == 'q':
                running = False
                break

            if user_choice.lower() not in ['c', 'l']:
                print("Invalid choice, please chose 'c', 'l' or 'q'.")
            else:
                choosing_lookup = False

        # Go to appropriate method to search up city
        if user_choice.lower() == "c":
            city_lookup()
        elif user_choice.lower() == "l":
            license_plate_lookup()