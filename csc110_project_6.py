
# this code gets information about co2 readings then calculates the minimum, maximum, and average readings entered

def main():
    enter_co2_reading_batch()


def get_nonempty_string():
    # this function gets the reader's name and the location he or she took the reading from
    # while block used in order to prompt user to enter a non-empty string
    while True:
        user_name = input("Please enter your name: ")
        if user_name != "":
            print(f"Name: {user_name}")
            break
        else:
            print("Please enter a valid name.")

    while True:
        reading_location = input("Please enter the reading location: ")
        if reading_location != "":
            print(f"Reading Location: {reading_location}")
            break
        else:
            print("Please enter a valid location.")

    return user_name, reading_location


def get_in_range_integer():
    # this function gets the proper ranges for the day, month, year, and reading
    # I added in the "exit" because I believed it was more intuitive for the user
    while True:
        reading_day = input('Please enter a reading day or type "exit" to exit: ')
        if reading_day.lower() == "exit":
            return None

        day = int(reading_day)
        if 0 < day <= 31:
            print(f"Reading Day: {day}")
            break
        else:
            print("Please enter a valid day.")

    while True:
        reading_month = input('Please enter a reading month: ')
        month = int(reading_month)
        if 0 < month <= 12:
            print(f"Reading Month: {month}")
            break
        else:
            print("Please enter a valid month.")
    # the reading year range is set to 1900 to 2023 because I felt it was more fitting than 2022 to 2099
    while True:
        reading_year = input('Please enter a reading year: ')
        year = int(reading_year)
        if 1900 < year <= 2023:
            print(f"Reading Year: {year}")
            break
        else:
            print("Please enter a valid year.")

    while True:
        co2_reading = input('Please enter a CO2 reading: ')
        reading = int(co2_reading)
        if 1 < reading <= 10000:
            print(f"CO2 Reading: {reading}")
            break
        else:
            print("Please enter a valid CO2 reading.")

    return day, month, year, reading


def enter_co2_reading_batch():
    # defining a tuple named "strings" to the return values of the non-empty strings function
    strings = get_nonempty_string()
    user_name, reading_location = strings

    # initializing variable names for subsequent use in while loop to calculate average
    total = 0
    average = 0
    co2_list = []

    # defining the tuple named "values" to the return values of get in range integer function and calculate average
    while True:
        values = get_in_range_integer()
        if values is None:
            break

        day, month, year, reading = values
        co2_list.append(reading)

        total += reading
        average = total / len(co2_list)

    print("--------------------------------------------------")
    print(f"Recorder Name: {user_name}")
    print(f"Reading Location: {reading_location}\n")
    print(f"Number of readings: {len(co2_list)}")
    print(f"Maximum CO2 level: {max(co2_list)}")
    print(f"Minimum CO2 level: {min(co2_list)}")
    print(f"Average CO2 level: {round(average)}")
    print("--------------------------------------------------")


main()

'''
TEST OUTPUTS: 
1. 
--------------------------------------------------
Recorder Name: John Doe
Reading Location: Seattle Bus Stop 12

Number of readings: 3
Maximum CO2 level: 912
Minimum CO2 level: 188
Average CO2 level: 429
--------------------------------------------------

2. 
--------------------------------------------------
Recorder Name: John Doe
Reading Location: Pike Place Market

Number of readings: 8
Maximum CO2 level: 973
Minimum CO2 level: 6
Average CO2 level: 683
--------------------------------------------------

3. 
--------------------------------------------------
Recorder Name: Jane Doe
Reading Location: Discovery Park

Number of readings: 3
Maximum CO2 level: 872
Minimum CO2 level: 177
Average CO2 level: 535
-------------------------------------------------

'''
