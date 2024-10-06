# Week 3 -      Prove Assignment
# Author:       Aaron Topping
# CSE 111  -    October 5, 2024
# NOTES:        Exceeding functions added: convert_kPa_to_psi, test_convert_kPa_to_psi ( to test_water_flow file)
#               Running THIS file will now also print out the result in PSI following the kPa printout
#               Coloring added to end of string indicating exceeding requirements goal when printing out psi

def water_column_height(tower_height, tank_height):
    '''
        Calculate the water column height
        t = h * (3w / 4)
        Parameters: Tower_height , tank_height
        Returns the water column height as a float
    '''

    result = ( 3 * tank_height ) / 4
    return ( result + tower_height )

def pressure_gain_from_water_height (height):
    '''
    Calculate the pressure gain due to water height
    P = pgh / 1000

    P is the pressure in kilopascals
    p is the density of water 998.2 ( kilogram / meter3) *Just use # in your calculations
    g is the acceleration from Earths gravity 9.80665 (meter / second2) *Just use # in your calculations
    h is the height of the water column in meters
    Parameters: height of water column in meters
    Returns: Pressure gain due to water height

    '''

    result = 998.2 * 9.80665 * height
    return ( result / 1000 )

def pressure_loss_from_pipe (pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):

    '''
    Calculate the pressure loss from a pipe
    P = -fLpv^2 / 2000d

    P is the lost pressure in kilopascals
    f is the pipe's friction factor
    L is the length of the pipe in meters
    p is the density of water 998.2 (kilogram / meter3) *Just use # in your calculations
    v is the velocity of the water flowing through the pipe in meters / second
    d is the diameter of the pipe in meters

    Parameters: pipe diameter, length, friction_factor, fluid velocity
    Returns: Pressure loss

    '''

    result = fluid_velocity**2 * -1 * friction_factor * pipe_length * 998.2
    return ( result / ( 2000 * pipe_diameter ) )

def pressure_loss_from_fittings(
        fluid_velocity, quantity_fittings):

    '''
    Calculate the pressure loss from pipe fittings
    P = -0.04pv^2n / 2000


    P is the lost pressure in kilopascals
    p is the density of water (998.2 kilogram / meter3)
    v is the velocity of the water flowing through the pipe in meters / second
    n is the quantity of fittings

    Parameters: fluid_velocity, quantity_fittings
    Returns: Pressure loss from the fittings

    '''

    result = fluid_velocity**2 * -0.04 * 998.2 * quantity_fittings
    return ( result / 2000 )

def reynolds_number(hydraulic_diameter, fluid_velocity):

    '''
    Calculate the "Reynolds number"
    R = pdv / μ

    R is the Reynolds number
    p is the density of water (998.2 kilogram / meter3)
    d is the hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe's inner diameter.
    v is the velocity of the water flowing through the pipe in meters / second
    μ is the dynamic viscosity of water (0.0010016 Pascal seconds)

    Parameters: hydraulic_diameter, fluid_velocity
    Returns: Reynolds number

    '''

    result = 998.2 * hydraulic_diameter * fluid_velocity
    return ( result / 0.0010016 )

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):

    '''
    Calculate the Pressure loss from pipe reduction (More complicated formula)
    k = ( 0.1 + 50/R ) * ((D/d)^4 - 1)
    P = -kpv^2 / 2000

    k is a constant computed by the first formula and used in the second formula
    R is the Reynolds number that corresponds to the pipe with the larger diameter
    D is the diameter of the larger pipe in meters
    d is the diameter of the smaller pipe in meters
    P is the lost pressure kilopascals
    p is the density of water (998.2 kilogram / meter3)
    v is the velocity of the water flowing through the larger diameter pipe in meters / second

    Parameters: larger_diameter, fluid_velocity, reynolds_number, smaller_diameter
    Returns: Pressure loss due to pipe reduction

    '''
    # Let's calculate the constant first
    constant = 0.1 + ( 50 / reynolds_number )                       # Step 1 ( breaking it up to make it more readable)
    constant *= ( (larger_diameter / smaller_diameter )**4 - 1)     # Step 2

    pressure = fluid_velocity**2 * -1 * constant * 998.2            # Step 3 - using constant in pressure calculation
    return ( pressure / 2000 )                                      # Step 4  - Returning final Pressure

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

# STRETCH ACTIONS ADDED
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500
WATER_DENSITY = 998.2000000
WATER_DYNAMIC_VISCOSITY = 0.0010016

def convert_kPa_to_psi( kPa ):
    '''
        Calculates the conversion of kPa to psi, which is standard US use
        psi = kPa / 6.89475729

        Parameters: kPa
        Returns: psi
    '''
    return ( kPa / 6.89475729 )

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print((f"Pressure at house: {convert_kPa_to_psi(pressure):.1f} psi \033[36m(EXCEEDING REQ)\033[0m"))

if __name__ == "__main__":
    main()