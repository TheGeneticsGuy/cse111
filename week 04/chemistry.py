# Author:           Aaron Topping
# Class:            CSE 111
# Date:             10/12/2024
# Description:      Prove - Week 4
# Exceeding Req:    * get_formula_name function was added, including a dictionary of known compounds.
#                   * Expanded list of known compounds to much larger, more complex list
#                   * Pediodic Table/Compound List now has the atomic number included as index 2 (position 3) of the list of atomic details
#                   * Created fix_molecular_formula function to reformat the input and remove case consderations
#                       -- I am little OCD, so formatting with improper formula case drives me nuts. This rebuilds the string properly.

from formula import parse_formula
import re       # Regular Expression parser of the formula

def make_periodic_table():
    '''
    Create and return a compound list that contains data for all 94 naturally occurring elements of the periodic table
    Parameters: None
    Return: Compound list for the periodic table of elements
    '''
    periodic_table_list = {
    "Ac": ["Actinium", 227, 89],
    "Ag": ["Silver", 107.8682, 47],
    "Al": ["Aluminum", 26.9815386, 13],
    "Ar": ["Argon", 39.948, 18],
    "As": ["Arsenic", 74.9216, 33],
    "At": ["Astatine", 210, 85],
    "Au": ["Gold", 196.966569, 79],
    "B": ["Boron", 10.811, 5],
    "Ba": ["Barium", 137.327, 56],
    "Be": ["Beryllium", 9.012182, 4],
    "Bi": ["Bismuth", 208.9804, 83],
    "Br": ["Bromine", 79.904, 35],
    "C": ["Carbon", 12.0107, 6],
    "Ca": ["Calcium", 40.078, 20],
    "Cd": ["Cadmium", 112.411, 48],
    "Ce": ["Cerium", 140.116, 58],
    "Cl": ["Chlorine", 35.453, 17],
    "Co": ["Cobalt", 58.933195, 27],
    "Cr": ["Chromium", 51.9961, 24],
    "Cs": ["Cesium", 132.9054519, 55],
    "Cu": ["Copper", 63.546, 29],
    "Dy": ["Dysprosium", 162.5, 66],
    "Er": ["Erbium", 167.259, 68],
    "Eu": ["Europium", 151.964, 63],
    "F": ["Fluorine", 18.9984032, 9],
    "Fe": ["Iron", 55.845, 26],
    "Fr": ["Francium", 223, 87],
    "Ga": ["Gallium", 69.723, 31],
    "Gd": ["Gadolinium", 157.25, 64],
    "Ge": ["Germanium", 72.64, 32],
    "H": ["Hydrogen", 1.00794, 1],
    "He": ["Helium", 4.002602, 2],
    "Hf": ["Hafnium", 178.49, 72],
    "Hg": ["Mercury", 200.59, 80],
    "Ho": ["Holmium", 164.93032, 67],
    "I": ["Iodine", 126.90447, 53],
    "In": ["Indium", 114.818, 49],
    "Ir": ["Iridium", 192.217, 77],
    "K": ["Potassium", 39.0983, 19],
    "Kr": ["Krypton", 83.798, 36],
    "La": ["Lanthanum", 138.90547, 57],
    "Li": ["Lithium", 6.941, 3],
    "Lu": ["Lutetium", 174.9668, 71],
    "Mg": ["Magnesium", 24.305, 12],
    "Mn": ["Manganese", 54.938045, 25],
    "Mo": ["Molybdenum", 95.96, 42],
    "N": ["Nitrogen", 14.0067, 7],
    "Na": ["Sodium", 22.98976928, 11],
    "Nb": ["Niobium", 92.90638, 41],
    "Nd": ["Neodymium", 144.242, 60],
    "Ne": ["Neon", 20.1797, 10],
    "Ni": ["Nickel", 58.6934, 28],
    "Np": ["Neptunium", 237, 93],
    "O": ["Oxygen", 15.9994, 8],
    "Os": ["Osmium", 190.23, 76],
    "P": ["Phosphorus", 30.973762, 15],
    "Pa": ["Protactinium", 231.03588, 91],
    "Pb": ["Lead", 207.2, 82],
    "Pd": ["Palladium", 106.42, 46],
    "Pm": ["Promethium", 145, 61],
    "Po": ["Polonium", 209, 84],
    "Pr": ["Praseodymium", 140.90765, 59],
    "Pt": ["Platinum", 195.084, 78],
    "Pu": ["Plutonium", 244, 94],
    "Ra": ["Radium", 226, 88],
    "Rb": ["Rubidium", 85.4678, 37],
    "Re": ["Rhenium", 186.207, 75],
    "Rh": ["Rhodium", 102.9055, 45],
    "Rn": ["Radon", 222, 86],
    "Ru": ["Ruthenium", 101.07, 44],
    "S": ["Sulfur", 32.065, 16],
    "Sb": ["Antimony", 121.76, 51],
    "Sc": ["Scandium", 44.955912, 21],
    "Se": ["Selenium", 78.96, 34],
    "Si": ["Silicon", 28.0855, 14],
    "Sm": ["Samarium", 150.36, 62],
    "Sn": ["Tin", 118.71, 50],
    "Sr": ["Strontium", 87.62, 38],
    "Ta": ["Tantalum", 180.94788, 73],
    "Tb": ["Terbium", 158.92535, 65],
    "Tc": ["Technetium", 98, 43],
    "Te": ["Tellurium", 127.6, 52],
    "Th": ["Thorium", 232.03806, 90],
    "Ti": ["Titanium", 47.867, 22],
    "Tl": ["Thallium", 204.3833, 81],
    "Tm": ["Thulium", 168.93421, 69],
    "U": ["Uranium", 238.02891, 92],
    "V": ["Vanadium", 50.9415, 23],
    "W": ["Tungsten", 183.84, 74],
    "Xe": ["Xenon", 131.293, 54],
    "Y": ["Yttrium", 88.90585, 39],
    "Yb": ["Ytterbium", 173.054, 70],
    "Zn": ["Zinc", 65.38, 30],
    "Zr": ["Zirconium", 91.224, 40]
    }

    return periodic_table_list

def make_known_molecules_dict():
    '''
    Create and return a compound list that contains data for many known compounds to compare a formula to
    Parameters: None
    Return: known compound list in dictionary form
    '''

    known_molecules_dict = {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CH3(CH2)6CH3": "octane",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water",
        "CO2": "carbon dioxide",
        "O2": "oxygen",
        "N2": "nitrogen",
        "H2SO4": "sulfuric acid",
        "HNO3": "nitric acid",
        "NaCl": "sodium chloride",
        "NaHCO3": "sodium bicarbonate",
        "CaCO3": "calcium carbonate",
        "H2O2": "hydrogen peroxide",
        "NH3": "ammonia",
        "CH4": "methane",
        "C2H2": "acetylene",
        "C2H4": "ethylene",
        "C5H12": "pentane",
        "C7H16": "heptane",
        "C9H20": "nonane",
        "C10H22": "decane",
        "C12H22O11": "sucrose",
        "C6H12O6": "glucose",
        "HCl": "hydrochloric acid",
        "NaOH": "sodium hydroxide",
        "KOH": "potassium hydroxide",
        "MgSO4": "magnesium sulfate",
        "CaCl2": "calcium chloride",
        "CCl4": "carbon tetrachloride",
        "Na2CO3": "sodium carbonate",
        "H3PO4": "phosphoric acid",
        "C6H5OH": "phenol",
        "C4H6": "butadiene",
        "C6H5CH3": "toluene",
        "CH3COOH": "acetic acid",
        "C9H8O4": "aspirin",
        "C8H10N4O2": "caffeine",
        "C27H46O": "cholesterol",
        "CH3CH2CH2OH": "propanol",
        "CH3(CH2)2CH3": "butane",
        "CH3CH2CH2CH2CH3": "pentane",
        "CH3(CH2)4CH3": "hexane",
        "CH3(CH2)5CH3": "heptane",
        "CH3(CH2)16COOH": "stearic acid",
        "CH3(CH2)7COOH": "octanoic acid",
        "CH3COOCH3": "methyl acetate",
        "CH3CH2OCH2CH3": "diethyl ether"
    }

    return known_molecules_dict

def get_formula_name(formula, known_molecules_dict):
    """Try to find formula in the known_molecules_dict.
    If formula is in the known_molecules_dict, return
    the name of the chemical formula; otherwise return
    "unknown compound".
    Parameters
        formula is a string that contains a chemical formula
        known_molecules_dict is a dictionary that contains
            known chemical formulas and their names
    Return: the name of a chemical formula
    """

    if formula in known_molecules_dict:
        return known_molecules_dict[formula]

    return ''

# Indexes for inner lists in the periodic table
ATOMIC_NUMBER_INDEX = 2
ATOMIC_MASS_INDEX = 1
# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1
def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.
    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.
    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    # Do the following for each inner list in the
    # compound symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        # Get the atomic mass for the symbol from the dictionary.
        # Multiply the atomic mass by the quantity.
        # Add the product into the total molar mass.
    # Return the total molar mass.

    molar_mass = 0
    for element in symbol_quantity_list:
        if element[SYMBOL_INDEX] in periodic_table_dict:
            molar_mass += ( element[QUANTITY_INDEX] * periodic_table_dict[element[SYMBOL_INDEX]][ATOMIC_MASS_INDEX] )

    return molar_mass


def sum_protons(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total number of protons in
    all the elements listed in symbol_quantity_list.
    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total number of protons of all
        the elements in symbol_quantity_list.
    """

    proton_count = 0
    for element in symbol_quantity_list:
        if element[SYMBOL_INDEX] in periodic_table_dict:
            proton_count += element[QUANTITY_INDEX] * periodic_table_dict[element[SYMBOL_INDEX]][ATOMIC_NUMBER_INDEX]

    return proton_count


# For error checking the inputs
def is_valid_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

def fix_molecular_formula( formula , periodic_table ):
    """Parse the molecular formula and ensure it is properly formatted in the correct case
    Parameters: formula (molecular formula as string), periodic_table (as dict)
    Return: The properly formatted molecular input
    """

    fixed_string = ''
    for i in range( len(formula) ):
        if not formula[i].isnumeric() and formula[i] != '(' and formula[i] != ')':
            if i == 0 or formula[i-1].isnumeric():
                fixed_string += formula[i].upper()              # First letter is always capitalized in the string, or the one right after a number
            elif not formula[i-1].isnumeric():                  # The previous letter is either a parentheses or a letter
                if formula[i-1] == '(' or formula[i-1] == ')':
                    fixed_string += formula[i].upper()
                else:
                    temp_element = f'{fixed_string[i-1]}{formula[i].lower()}'
                    if temp_element in periodic_table:
                        fixed_string += formula[i].lower()
                    else:
                        fixed_string += formula[i].upper()  # Could be CO2
        else:
            fixed_string += formula[i]
    return fixed_string

def main():
    periodic_table = make_periodic_table()
    known_compounds = make_known_molecules_dict()
    formula = ''
    mass = 0
    errorMsg = 'Error - Input is not valid. Please re-enter!'

    # This took a LOT of tinkering to get right!
    formula_pattern = r'([A-Z][a-z]*)(\d+)*'                        # Simple chemical formulas with no parenthese ( Ex: H2O2 or C6H12O6 )
    formula_pattern_complex = r'([A-Z][a-z]*)(\d+)?(?![^\(]*\))'    # For complex formulas that include parentheses ( Ex: Ca(NO3)2 or C6H12(CO2)6 )

    print() # Aesthetic Spacing

    # Obtain a valid chemical formula
    while True:
        formula = input("Please provide a chemical formula (Example: H2O, C6H12O6, etc.): ")
        formula = fix_molecular_formula(formula , periodic_table)
        if re.findall ( formula_pattern , formula ) or re.findall ( formula_pattern_complex , formula ):
            print(f"{formula} is Valid")
            break
        else:
            print(errorMsg)

    # Obtain a valid mass weight in grams
    while True:
        mass = input(f"Please provide the mass of the \'{formula}\' chemical sample (grams): ")
        if is_valid_number ( mass ):
            print(f"{mass}(g) is Valid")
            mass = float(mass)
            break
        else:
            print(errorMsg)

    parsed_elements = parse_formula ( formula , periodic_table )
    molar_mass = compute_molar_mass( parsed_elements , periodic_table )
    formula_name = get_formula_name( formula , known_compounds )
    moles = (mass / molar_mass)
    proton_count = sum_protons ( parsed_elements , periodic_table )

    if formula_name != '':
        formula_name = f' ({formula_name})'  # Add Parentheses and spacing, otherwise it stays empty string

    print()
    print(f'Sample Details: {formula}{formula_name} - {mass}(g)')        # Adds the FORMULA NAME (Stretch)
    print(f'{molar_mass:.5f} games/mole')
    print(f'{moles:.5f} moles')
    print(f'{proton_count} total protons')

    # print('TABLE OF ELEMENTS')

    # for i in range ( 0 , len(periodic_table) - 1 ):
    #     print(f'{periodic_table[i][1]} {periodic_table[i][2]}')

    print() # Aesthetic spacing


# Bypass main if imported
if __name__ == "__main__":
    main()