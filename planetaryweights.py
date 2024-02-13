"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""

#constants for required weight multipliers depending on the planet
mercury_mult = 0.376
venus_mult = 0.89
mars_mult = 0.378
jupiter_mult = 2.360
saturn_mult = 1.081
uranus_mult = 0.82
neptune_mult = 1.140

def main():
    # First, we store the input weight in a variable 'x'
    x = float(input("Enter a weight on Earth: "))
    # Then, we record the planet name with a variable 'p'
    p = input("Enter a planet: ")
    # Now we check the planet name in 'p' with valid planet names
    # If we get a match, we assign a variable 'm' to the planet's weight multiplier
    if p=="Mercury":
        m = float(mercury_mult)
    elif p=="Venus":
        m = float(venus_mult)
    elif p=="Mars":
        m = float(mars_mult)
    elif p=="Jupiter":
        m = float(jupiter_mult)
    elif p=="Saturn":
        m = float(saturn_mult)
    elif p=="Uranus":
        m = float(uranus_mult)
    elif p=="Neptune":
        m = float(neptune_mult)
    # If there is no match, we get an error statement
    else: 
        print("That is not a valid planet.")
    # Now we calculate the value of equivalent weight and round it to 2 decimals
    a = x * m
    rounded_a = round(a,2)
    # Finally, we print out the answer
    print("The equivalent weight on ", p, ": ", rounded_a)

if __name__ == "__main__":
    main()