# Creating a dictionary in Python
engl_span_dictionaries = {
    "Spring": "Primavera",
    "Summer": "Verano",
    "Fall": "Otoño",
    "Winter": "Invierno"
}

# Function to get description based on user input
def get_season_description():
    season = input("Enter a season (Spring, Summer, Fall, Winter): ").capitalize()  # Capitalize to match dictionary keys
    if season in engl_span_dictionaries:
        print(f"The Spanish word for {season} is: {engl_span_dictionaries[season]}")
    else:
        print("Invalid input. Please enter one of the following: Spring, Summer, Fall, Winter.")

# Call the function
get_season_description()
