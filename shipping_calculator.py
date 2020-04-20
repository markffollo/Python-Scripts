## This script determines the cheapest shipping costs for various shipping
## options
def ground_shipping_cost(weight):
  flat_charge = 20
  if weight <= 2:
    weight_cost = 1.50 * weight
    total_cost = weight_cost + flat_charge
    return total_cost
  elif weight <= 6:
    weight_cost = 3.00 * weight
    total_cost = weight_cost + flat_charge
    return total_cost
  elif weight <= 10:
    weight_cost = 4.00 * weight
    total_cost = weight_cost + flat_charge
    return total_cost
  else:
    weight_cost = 4.75 * weight
    total_cost = weight_cost + flat_charge
    return total_cost

def drone_shipping_cost(weight):
  flat_charge = 0
  if weight <= 2:
    weight_cost = 4.50 * weight
    total_cost = weight_cost + flat_charge
    return total_cost
  elif weight <= 6:
    weight_cost = 9.00 * weight
    total_cost = weight_cost + flat_charge
    return total_cost
  elif weight <= 10:
    weight_cost = 12.00 * weight
    total_cost = weight_cost + flat_charge
    return total_cost
  else:
    weight_cost = 14.25 * weight
    total_cost = weight_cost + flat_charge
    return total_cost

def cost_calculator(weight):
  ground_shipping = ground_shipping_cost(weight)
  print("Ground shipping will cost " + str(ground_shipping) + "$")
  drone_shipping = drone_shipping_cost(weight)
  print("Drone shipping will cost " + str(drone_shipping) + "$")
  premium_ground_shipping = 125 
  print("Premium Ground shipping will cost 125$")
  if (ground_shipping < drone_shipping) and (ground_shipping < premium_ground_shipping):
    return "You should use Ground Shipping!"
  elif (drone_shipping < ground_shipping) and (ground_shipping < premium_ground_shipping):
    return "You should use Drone Shipping!"
  else:
    return "You should use Premium Ground Shipping!"

print(cost_calculator(4.8))
print(cost_calculator(41.5))
print(cost_calculator(15))




