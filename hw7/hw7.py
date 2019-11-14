'''
Calculations for hw7
'''

import math as m 

# Stromgren radius
sradius = lambda Q0, nh, aB : ( 3 * Q0 / (4 * m.pi * nh**2 * aB) )**(1/3) 
alpha_B = lambda T4 : 2.56 * 10**(-13) * T4**(-0.83)

# given parameters
Q0 = 10**(48.44) # from table
nh = 0.2         # given in question
T4 = 1           # given in question
aB = alpha_B(T4)

radius = sradius(Q0, nh, aB)

print("1 (a): Stromgren radius = {:.4g}".format(radius))

# 1(b): comparing timescales
v_star   = 100 * 10**3 # cm/s
t_travel = radius / v_star
t_rec    = 1 / aB / nh 

ratio = t_travel / t_rec

print("ratio = t_travel / t_rec = {:.4g}".format(ratio))

# 2(b)
slength_disk = lambda q0, nh, aB : q0 / aB /  nh**2

h   = 6.626 * 10**(-34) * 10**7 # cgs 
q_0 = 0.66 * 10**(-21) / h      # cm^-2 sr-1
nh  = 0.1
T4  = 1
aB  = alpha_B(T4)

length = slength_disk(q_0, nh, aB)

print("2(b): disk Stromgren length = {:.4g}".format(length))
