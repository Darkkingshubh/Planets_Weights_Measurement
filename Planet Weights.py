##Planet Weights

# Write code below 💖
# Create a weight conversion program
earth_weight = float(input("What is Earth weight is : "))
planet_num = int(input("What planet number are you on: "))

#destination_weight = earth_weight * 0.38
m = earth_weight * 0.38
v = earth_weight * 0.91
ms = earth_weight * 0.38
j = earth_weight * 2.53
s = earth_weight * 1.07
u = earth_weight * 0.89
n = earth_weight * 1.14
#use an if/elif/else statement to calculate the user's weight on the destination planet.
if planet_num == 1:
  print(f"Mercury destination weight = {m}")
elif planet_num == 2:
  print(f"Venus destination weight = {v}")
elif planet_num == 3:
  print(f"Mars destination_weight = {ms}")
elif planet_num == 4:
  print(f"Jupiter destination_weight = {j}")
elif planet_num == 5:
  print(f"Saturn destination_weight = {s}")
elif planet_num == 6:
  print(f"Uranus destination_weight = {u}")
elif planet_num == 7:
  print(f"Neptune destination_weight = {n}")
else:
  print('Invalid planet number')