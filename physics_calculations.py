train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

def f_to_c(f_temp):
  f_temp_mod = f_temp - 32
  c_temp = f_temp_mod*5/9
  return (c_temp)

def c_to_f(c_temp):
  c_temp_mod = c_temp*9/5
  f_temp = c_temp_mod + 32
  return f_temp

#c_temp = f_to_c(100)
#print(str(c_temp))

#f_temp = c_to_f(0)
#print(str(f_temp))

def get_force(mass, acceleration):
  force = mass*acceleration
  return force

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

c = 3*10**8
def get_energy(mass, c):
  energy = mass*c**2
  return energy

bomb_energy = get_energy(bomb_mass, c)
print("A 1kg bomb supplies " + str(bomb_energy) +" Joules.")

def get_work(mass, acceleration, distance):
  work = get_force(mass, acceleration)*distance
  return work

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
