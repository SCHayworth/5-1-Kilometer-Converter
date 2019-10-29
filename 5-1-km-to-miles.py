# 5-1 Kilometer Converter
# Shaun Hayworth
# CIS 2
# 10-28-2019
# Original source code and revision history available at https://github.com/SCHayworth/5-1-Kilometer-Converter

# Converts distance in kilometers into miles using the show_miles function.

# Define the main function
# Mainline logic of the program
def main():

    # Prompt user for a distance in km
    km = int(input('Enter the distance in km: '))

    # Calls the show_miles function
    show_miles(km)

# Define the show_miles function
# Converts kilometers into miles and displays the result.
def show_miles(km):

    # Multiply km by 0.6214 to convert distance to miles
    miles = km * 0.6214

    # Display the result
    print(f'The conversion of {km:.2f} kilometers to miles is {miles:.2f} miles.')

# Call the main function to execute the program
main()
