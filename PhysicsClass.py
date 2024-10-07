train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below:

def f_to_c(f_temp):
    c_temp_result =  (float(f_temp)-32)*5/9

    return c_temp_result

def c_to_f(c_temp):
    f_temp_result = c_temp*(9/5)+32

    return f_temp_result

def get_force(mass, acceleration):
    return mass * acceleration

def get_energy(mass, c = 3*10**8):
    return mass * (c**3)

def get_work(mass, acceleration, distance):
    return get_force(mass, acceleration) * distance

f100_in_celsius = f_to_c(100)
c0_in_fahrenheit = c_to_f(0)
train_force = get_force(train_mass, train_acceleration)
bomb_energy = get_energy(bomb_mass)

print(f'The GE train supplies {train_force} Newtons of force.')
print(f'A 1kg bomb supplies {bomb_energy} Joules')
print(f'Work is: {get_work(5,100,100)}')