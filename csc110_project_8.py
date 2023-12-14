# import sys
# from contextlib import redirect_stdout, redirect_stderr


def main():
    calc_pollutant()

# Redirect output to a file
# with open("TerminalOutput.txt", "w") as new_file:
# with redirect_stdout(new_file), redirect_stderr(sys.stdin):
# Call functions that print to the terminal and read input



def get_pollutant():
    # FUNCTION TO GET RIVER, MONTH, AND POLLUTANT FROM USER
    while True:
        river = input("Which river? ")
        if river != "":
            print("OK")
            break
        else:
            print("Invalid. Please enter a river name.")
    while True:
        try:
            month = int(input("Which month (e.g., 1 for January)? "))
            if 1 <= month <= 12:
                print("OK")
                break
            else:
                print("Invalid. Please enter a month number.")
        except ValueError:
            print("Invalid. Please enter a month number.")

    print("Available pollutants: "
          "\n 1. Arsenic "
          "\n 2. Lead "
          "\n 3. Fertilizer "
          "\n 4. Pesticides")

    while True:
        try:
            pollutant = int(input("Which pollutant? "))
            if 1 <= pollutant <= 4:
                print("OK")
                break
            else:
                print("Invalid. Please enter a pollutant number.")
        except ValueError:
            print("Invalid. Please enter a pollutant number.")
    print("")
    print(f"Data for river: {river} River")
    print(f"Data for month: {month}")
    if pollutant == 1:
        print(f"Data for pollutant: Arsenic")
    elif pollutant == 2:
        print(f"Data for pollutant: Lead")
    elif pollutant == 3:
        print(f"Data for pollutant: Fertilizer")
    else:
        print(f"Data for pollutant: Pesticides")

    return river, month, pollutant


def calc_pollutant():
    # FUNCTION TO EXTRACT DATA AND PERFORM CALCULATIONS ON TEXT FILE
    values = get_pollutant()
    river, month, pollutant = values
    with open("RiverPollutionData.txt", "r") as file:
        content = file.readlines()
        # header = content[0]
        content = content[1:]
        # ESTABLISH VARIABLE NAMES
        river_count = 0
        max_pollutant_level = None
        min_pollutant_level = None
        total_arsenic_level = 0
        total_lead_level = 0
        total_fertilizer_level = 0
        total_pesticides_level = 0

    for line in content:
        reading = line.split()
    # split data into functions then assign column names
    # split data into functions then assign column names
        river_name = reading[0]
        river_month = int(reading[2])
        arsenic_level = float(reading[4])
        lead_level = float(reading[5])
        fertilizer_level = float(reading[6])
        pesticides_level = float(reading[7])
    # working with the data
    # working with the data
        if river_name == river and river_month == month:
            river_count += 1
            total_arsenic_level += arsenic_level
            total_lead_level += lead_level
            total_fertilizer_level += fertilizer_level
            total_pesticides_level += pesticides_level
            # ARSENIC LEVELS CHECKED FOR MINIMUM AND MAXIMUM
            if pollutant == 1 and (max_pollutant_level is None or arsenic_level > max_pollutant_level):
                max_pollutant_level = arsenic_level
            if pollutant == 1 and (min_pollutant_level is None or arsenic_level < min_pollutant_level):
                min_pollutant_level = arsenic_level
            # LEAD LEVELS CHECKED FOR MINIMUM AND MAXIMUM
            if pollutant == 2 and (max_pollutant_level is None or lead_level > max_pollutant_level):
                max_pollutant_level = lead_level
            if pollutant == 2 and (min_pollutant_level is None or lead_level < min_pollutant_level):
                min_pollutant_level = lead_level
            # FERTILIZER LEVELS CHECKED FOR MINIMUM AND MAXIMUM
            if pollutant == 3 and (max_pollutant_level is None or fertilizer_level > max_pollutant_level):
                max_pollutant_level = fertilizer_level
            if pollutant == 3 and (min_pollutant_level is None or fertilizer_level < min_pollutant_level):
                min_pollutant_level = fertilizer_level
            # PESTICIDE LEVELS CHECKED FOR MINIMUM AND MAXIMUM
            if pollutant == 4 and (max_pollutant_level is None or pesticides_level > max_pollutant_level):
                max_pollutant_level = pesticides_level
            if pollutant == 4 and (min_pollutant_level is None or pesticides_level < min_pollutant_level):
                min_pollutant_level = pesticides_level
    if river_count > 0 and pollutant == 1:
        average_arsenic_level = total_arsenic_level / river_count
        print("Average arsenic level of the month:", round(average_arsenic_level, 3))
    if river_count > 0 and pollutant == 2:
        average_lead_level = total_lead_level / river_count
        print("Average lead level of the month:", round(average_lead_level, 3))
    if river_count > 0 and pollutant == 3:
        average_fertilizer_level = total_fertilizer_level / river_count
        print("Average fertilizer level of the month:", round(average_fertilizer_level, 3))
    if river_count > 0 and pollutant == 4:
        average_pesticides_level = total_pesticides_level / river_count
        print("Average pesticides level of the month:", round(average_pesticides_level, 3))

    print("Total number of readings in the month:", river_count)
    print("Highest reading of the month:", max_pollutant_level)
    print("Lowest reading of the month:", min_pollutant_level)


main()

"""
TESTS:
TEST 1:
Data for river: Blanco River
Data for month: 1
Data for pollutant: Lead
Average lead level of the month: 53.32
Total number of readings in the month: 25
Highest reading of the month: 98.0
Lowest reading of the month: 6.0

TEST 2: 
Data for river: Angelina River
Data for month: 6
Data for pollutant: Fertilizer
Average fertilizer level of the month: 0.24
Total number of readings in the month: 24
Highest reading of the month: 0.372
Lowest reading of the month: 0.1

TEST 3:
Data for river: Lampasas River
Data for month: 12
Data for pollutant: Arsenic
Average arsenic level of the month: 21.259
Total number of readings in the month: 27
Highest reading of the month: 37.0
Lowest reading of the month: 12.0
"""
