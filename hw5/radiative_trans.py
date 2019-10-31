'''
radiative_trans.py : calc for hw5
'''
import math

# in cgs
h = 6.626 * 10**(-34) * 10**7 #erg/s
c = 3 * 10**10                #cm/s
k = 1.38 * 10**(-16)

# 2(a)
calc_Tb = lambda nu, Inu : h * nu / k / math.log(1 + (2 * h * nu**3 / c**2 / Inu) )
calc_Inu = lambda A, nu, phi, N : 3 / 16 / math.pi * A * h * nu * phi * N
calc_Ilte = lambda nu, T : 2 * h * nu**3 / c**2 / (math.exp(h * nu / k / T) - 1)

lambda_21cm = 21.106
nu          = c / lambda_21cm
A_21cm      = 2.8843 * 10**(-15)
sigma_nu    = 10**5
N_ell       = 10**20 

phi_line_center = 1 / math.sqrt(2 * math.pi) * c / nu / sigma_nu

I_21cm = calc_Inu(A_21cm, nu, phi_line_center, N_ell)

# calc I for CMB
nu_cmb = 160.23 * 10**9
T_cmb  = 2.7255
I_cmb  = calc_Ilte(nu_cmb, T_cmb)

print("total intensity: {}".format(I_21cm + I_cmb))

Tb = calc_Tb(nu, I_21cm + I_cmb)

#2(b)
# To Jy Sr-1
print("in Jysr-1",
 (I_21cm + I_cmb) * 10**(-7) / 10**(-4) * 10**(26) / (4 * math.pi) )

#3(a)
calc_optical_depth = lambda g, lrest : g * lrest**3

print("optical depth ratio : ", 
    calc_optical_depth(4, 1548.2) / calc_optical_depth(2, 1550.8))