# File: circular_motion_dynamics.py

import numpy as np

g = 9.80665 

def centripetal_acceleration(speed, rope_length):
    '''
    Given the speed of the ball at the top and the length of the rope,
    Calculates the centripetal acceleration at that point.
    centripetal_acceleration = v^2/r, m/s^2
    
    Inputs: speed in m/s (float), length of the rope in m (float)
    Output: centripetal acceleration in m/s^2 (float)
    '''
    result = speed
    result **= 2
    acceleration = np.divide(result, rope_length)
    
    return acceleration

def find_tension(centripetal_acceleration, mass):
    '''
    Given centripetal acceleration and mass, finds the tension in the rope
    at the top of the path.
    Fnet = ma
    T + mg = Fnet
    T + mg = ma
    T = m(a - g)
    
    Inputs: centripetal acceleration (float), mass (float)
    Output: tension (float)
    '''
    result = centripetal_acceleration
    result -= g
    tension = result * mass

    return round(tension, 4)

def will_complete_a_rotation(speed_and_mass_array, rope_length):
    '''
    Given an array of speeds and masses, along with the length of a rope,
    finds whether each ball will complete a rotation when spun vertically around.
    Inputs: arrays of speed and mass, length of rope
    Outputs: array
    '''

    result = []
    
    for i in range(len(speed_and_mass_array)):
        acceleration = centripetal_acceleration(speed_and_mass_array[i, 1], rope_length)
        tension = find_tension(acceleration, speed_and_mass_array[i, 0])
        if(tension < 0):
            result.append(f"The speed is not enough for a ball that weighs {speed_and_mass_array[i, 0]} kg to complete a rotation.")
        elif tension == 0:
            result.append(f"The speed is just barely enough for a ball that weighs {speed_and_mass_array[i, 0]} kg to complete a rotation.")
        else:
            result.append(f"The speed of a ball that weighs {speed_and_mass_array[i, 0]} kg will be more than enough to complete a rotation.")
    return result
        