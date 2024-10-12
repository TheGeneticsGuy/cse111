# Author:           Aaron Topping
# Class:            CSE 111
# Date:             10/12/2024
# Description:      Prove - Week 4
# Additional Notes: I was not satisfied with the idea of only taking input for limited chemical formulas, but I wanted to be able to
#                   handle complex formulas as well, notably formulas with nested compounds, like Ca(NO3)2. Since these are extremely common
#                   the goal was to challenge my ability to use RegEx for pattern recognition.  So, a non-complex pattern was created, as well as a
#                   complex. The strategy was to first go over all the elements outside of the parentheses, and then go back do the same for all within
#                   Due to the Complexity, an additional function 'parse_formula' was added to handle this logic.


import re       # Regular Expression parser of the formula

# This took a LOT of tinkering to get right!
FORMULA_PATTERN = r'([A-Z][a-z]*)(\d+)*'                        # Simple chemical formulas with no parenthese ( H2O2 or C6H12O6 )
FORMULA_PATTERN_COMPLEX = r'([A-Z][a-z]*)(\d+)?(?![^\(]*\))'    # For complex formulas that include parentheses ( Ca(NO3)2 or C6H12(CO2)6 )

def make_periodic_table():
    '''
    Create and return a compound list that contains data for all 94 naturally occurring elements of the periodic table
    Parameters: None
    Return: Compound list for the periodic table of elements
    '''
    periodic_table_list = [
        ["Ac", "Actinium", 227],
        ["Ag", "Silver", 107.8682],
        ["Al", "Aluminum", 26.9815386],
        ["Ar", "Argon", 39.948],
        ["As", "Arsenic", 74.9216],
        ["At", "Astatine", 210],
        ["Au", "Gold", 196.966569],
        ["B", "Boron", 10.811],
        ["Ba", "Barium", 137.327],
        ["Be", "Beryllium", 9.012182],
        ["Bi", "Bismuth", 208.9804],
        ["Br", "Bromine", 79.904],
        ["C", "Carbon", 12.0107],
        ["Ca", "Calcium", 40.078],
        ["Cd", "Cadmium", 112.411],
        ["Ce", "Cerium", 140.116],
        ["Cl", "Chlorine", 35.453],
        ["Co", "Cobalt", 58.933195],
        ["Cr", "Chromium", 51.9961],
        ["Cs", "Cesium", 132.9054519],
        ["Cu", "Copper", 63.546],
        ["Dy", "Dysprosium", 162.5],
        ["Er", "Erbium", 167.259],
        ["Eu", "Europium", 151.964],
        ["F", "Fluorine", 18.9984032],
        ["Fe", "Iron", 55.845],
        ["Fr", "Francium", 223],
        ["Ga", "Gallium", 69.723],
        ["Gd", "Gadolinium", 157.25],
        ["Ge", "Germanium", 72.64],
        ["H", "Hydrogen", 1.00794],
        ["He", "Helium", 4.002602],
        ["Hf", "Hafnium", 178.49],
        ["Hg", "Mercury", 200.59],
        ["Ho", "Holmium", 164.93032],
        ["I", "Iodine", 126.90447],
        ["In", "Indium", 114.818],
        ["Ir", "Iridium", 192.217],
        ["K", "Potassium", 39.0983],
        ["Kr", "Krypton", 83.798],
        ["La", "Lanthanum", 138.90547],
        ["Li", "Lithium", 6.941],
        ["Lu", "Lutetium", 174.9668],
        ["Mg", "Magnesium", 24.305],
        ["Mn", "Manganese", 54.938045],
        ["Mo", "Molybdenum", 95.96],
        ["N", "Nitrogen", 14.0067],
        ["Na", "Sodium", 22.98976928],
        ["Nb", "Niobium", 92.90638],
        ["Nd", "Neodymium", 144.242],
        ["Ne", "Neon", 20.1797],
        ["Ni", "Nickel", 58.6934],
        ["Np", "Neptunium", 237],
        ["O", "Oxygen", 15.9994],
        ["Os", "Osmium", 190.23],
        ["P", "Phosphorus", 30.973762],
        ["Pa", "Protactinium", 231.03588],
        ["Pb", "Lead", 207.2],
        ["Pd", "Palladium", 106.42],
        ["Pm", "Promethium", 145],
        ["Po", "Polonium", 209],
        ["Pr", "Praseodymium", 140.90765],
        ["Pt", "Platinum", 195.084],
        ["Pu", "Plutonium", 244],
        ["Ra", "Radium", 226],
        ["Rb", "Rubidium", 85.4678],
        ["Re", "Rhenium", 186.207],
        ["Rh", "Rhodium", 102.9055],
        ["Rn", "Radon", 222],
        ["Ru", "Ruthenium", 101.07],
        ["S", "Sulfur", 32.065],
        ["Sb", "Antimony", 121.76],
        ["Sc", "Scandium", 44.955912],
        ["Se", "Selenium", 78.96],
        ["Si", "Silicon", 28.0855],
        ["Sm", "Samarium", 150.36],
        ["Sn", "Tin", 118.71],
        ["Sr", "Strontium", 87.62],
        ["Ta", "Tantalum", 180.94788],
        ["Tb", "Terbium", 158.92535],
        ["Tc", "Technetium", 98],
        ["Te", "Tellurium", 127.6],
        ["Th", "Thorium", 232.03806],
        ["Ti", "Titanium", 47.867],
        ["Tl", "Thallium", 204.3833],
        ["Tm", "Thulium", 168.93421],
        ["U", "Uranium", 238.02891],
        ["V", "Vanadium", 50.9415],
        ["W", "Tungsten", 183.84],
        ["Xe", "Xenon", 131.293],
        ["Y", "Yttrium", 88.90585],
        ["Yb", "Ytterbium", 173.054],
        ["Zn", "Zinc", 65.38],
        ["Zr", "Zirconium", 91.224]
    ]

    return periodic_table_list

def parse_formula( formula ):
    '''
    Parse elements into a dictionary with the number of each element
    Parameters: Chemical formula (H20)
    Returns:    Dictionary of values of parsed formula
    '''
    result = {}             # Initializing the empty dictionary to return at end
    pattern_outside = ''
    pattern_inside = ''

    # Convert the parse data from regEx to a dictionary for easier counting
    def buildDictionaryCounts (elements , multiplyer=1 ):

        '''
        Converts the regex list of parsed elements with number of element into the dictionary
        Uses the global (within parent function) dictionary 'result'
        parameters: elements(list),multiplyer(int)
        returns: nothing
        '''
         # Now, we build the dictionary.
        for element , count in elements:
            count = int(count) if count else 1  # Since formulas without numbers following will be 1, default value needs to be one
            if element in result:
                result[element] += ( count * multiplyer )        # Since formulas can have multiple of same element, just add here
            else:
                result[element] = ( count * multiplyer )

    # Setup the patterns for RegEx matching
    # Only need to do more complex pattern matching IF formula has a parentheses
    if '(' in formula:
        pattern_outside = FORMULA_PATTERN_COMPLEX
        pattern_inside = r'\(([A-Za-z0-9]+)\)(\d+)*'            # Will provide the complex pattern match what formulas inside parenthesesC

    else:
        pattern_outside = FORMULA_PATTERN

    # Start with the outside
    parsed_elements = re.findall( pattern_outside, formula )  # Adds to the list all pattern matches, the *indicates it as an optional value, so \d+ for any size number (no + means 1 digit only), and * in case no number

    # First, let's count all the outside stuff
    if parsed_elements:
        buildDictionaryCounts(parsed_elements)
    else:
        print("ERROR1")
        return result       # Did not successfully parse any elements Formula didn't match pattern

    if pattern_inside != '':
        parsed_parentheses_group = re.findall( pattern_inside, formula )

        print(parsed_parentheses_group)
        for elementGroup , count in parsed_parentheses_group:
            print("Group: " + elementGroup)
            if count == '':     # Edge case in case the formula is placed into parentheses incorrectly with no power. It will still work
                count = "1"
            parsed_elements = re.findall( pattern_outside, elementGroup )
            if parsed_elements:
                buildDictionaryCounts(parsed_elements , int(count))

    return result

def compute_molar_mass( formula ):

    '''
    Calculates molar mass by parsing the text input formula of the user
    '''

# For error checking the inputs
def is_valid_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

def main():
    periodic_table = make_periodic_table()
    formula = ''
    mass = 0
    errorMsg = 'Error - Input is not valid. Please re-enter!'

    print()

    # Obtain a valid chemical formula
    while True:
        formula = input("Please provide a chemical formula (Example: H2O, C6H12O6, etc.): ").upper()
        if re.findall ( FORMULA_PATTERN , formula ) or re.findall ( FORMULA_PATTERN_COMPLEX , formula ):
            print(f"{formula} is Valid")
            break
        else:
            print(errorMsg)

    # Obtain a valid mass weight in grams
    while True:
        mass = input(f"Please provide the mass of the \'{formula}\' chemical sample (grams): ")
        if is_valid_number ( mass ):
            print(f"{mass}(g) is Valid")
            break
        else:
            print(errorMsg)
    print()
    print('TABLE OF ELEMENTS')

    for i in range ( 0 , len(periodic_table) - 1 ):
        print(f'{periodic_table[i][1]} {periodic_table[i][2]}')


# Bypass main if imported
if __name__ == "__main__":
    main()