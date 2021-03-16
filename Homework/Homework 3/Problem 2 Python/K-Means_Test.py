x = [-0.82, -1.33, -3.63, -1.62, -2.95, 0.95, 0.53, 1.79, 0.95, 2.28]
pi_1 = [1, 0, 0, 0, 1, 1, 0, 1, 0, 1]
chi_1=[]
chi_2=[]

print("x = ", x)
print("pi_1: ", pi_1)

for index, val in enumerate(x):
   if pi_1[index] == 0:
      chi_1.append(val)
   else:
      chi_2.append(val)
print("\nchi_1: ", chi_1)
print("chi_2: ", chi_2)

mu_1 = sum(chi_1) / len(chi_1)
mu_2 = sum(chi_2) / len(chi_2)
print("\nmu_1: ", mu_1)
print("mu_2: ", mu_2)

pi_2 = []
for val in x:
   dist_from_mu_1 = abs(mu_1 - val)
   dist_from_mu_2 = abs(mu_2 - val)

   pi_2.append(int(dist_from_mu_2 < dist_from_mu_1))

print("\npi_2: ", pi_2)

"""########OUTPUT########
x =  [-0.82, -1.33, -3.63, -1.62, -2.95, 0.95, 0.53, 1.79, 0.95, 2.28]
pi_1:  [1, 0, 0, 0, 1, 1, 0, 1, 0, 1]

chi_1:  [-1.33, -3.63, -1.62, 0.53, 0.95]
chi_2:  [-0.82, -2.95, 0.95, 1.79, 2.28]

mu_1:  -1.02
mu_2:  0.24999999999999992

pi_2:  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
"""

