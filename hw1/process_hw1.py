'''
process_hw1.py : a short script to write homework 1

Draine problems can be found at https://www.astro.princeton.edu/~draine/book/problems.
pdf.
1. Draine Problem 1.1 part (a), and the following: [10 pts]
2. Draine Problem 1.2 [5 pts]
3. Energy and momentum input from a massive star: [10 pts]

Requirements:
----
python 3+
no library installation requirements, it a pure python script

<Run>
----
>> python process_hw1.py

<Output>
----
Prob 1.1 (a): number density of H is -> 8.98 1/cm^3
Prob 1.1 (b): ρb / <ρb> = Nb / <Nb> = 1.62e+06
Lower. If there's a higher concentration in the galaxy, then the structure of the galaxy will be changed by the
structure of the dark matter, which is not the case. Baryons have more structures in the galaxtic plane than dark matter halos,
so the concentration for baryons should be higher.
Prob 1.2 : mean free path  = 
	= 1 / cross-section (pi * radius^2) / number density
	= 4.72e+13 cm
Prob 3: 3 sources contribute to momentum and energy to ISM: 1) radiation; 2) stellar wind; 3) ejecta
1) radiation energy = 2.84e+53 erg; radiation momentum = 9.46e+42 g cm /s
2) stellar wind energy = 7.5e+51 erg; stellar wind momentum = 3e+43 g cm /s
3) ejecta energy = 1.25e+51 erg; ejecta momentum = 5e+42 g cm / s
'''

class PhysVal:
    '''
    Args: 
        value(float)
        unit(str)
    '''
    def __init__(self, value, unit):
        self.value = value
        self.unit  = unit 

    def __repr__(self):
        return "{} {}".format(self.value, self.unit)

    def __mul__(self, other):
        if not isinstance(other, PhysVal):
            other_value = other
            other_unit  = '1'
        else:
            other_value = other.value
            other_unit  = other.unit

        return PhysVal(*
            (self.value * other_value,
            "{} * {}".format( self.unit, other_unit )) 
        )

    def __rmul__(self, other):
        if not isinstance(other, PhysVal):
            other_value = other
            other_unit  = '1'
        else:
            other_value = other.value
            other_unit  = other.unit

        return PhysVal(*
            (self.value * other_value,
            "{} * {}".format( self.unit, other_unit )) 
        )

    def __add__(self, other):
        # assert self.unit == other.unit
        return PhysVal(*
            (self.value + other.value, 
            "{}".format(self.unit))
        )

    def __truediv__(self, other):
        if not isinstance(other, PhysVal):
            other_value = other
            other_unit  = '1'
        else:
            other_value = other.value
            other_unit  = other.unit
            
        return PhysVal(*
            (self.value / other_value,
            "{} / ({})".format(self.unit, other_unit))
        )

    def __rtruediv__(self, other):
        if not isinstance(other, PhysVal):
            other_value = other
            other_unit  = '1'
        else:
            other_value = other.value
            other_unit  = other.unit
            
        return PhysVal(*
            (other_value / self.value,
            "{} / ({})".format(other_unit, self.unit))
        )


# Prob 1.1 : Calculate the number density in the disk with mixture of He/H = 0.1
# defines physical values of the problem
M_gal  = PhysVal( 4 * 10**9, 'M_sun' )
Radius = PhysVal( 15       , 'kpc'   )
Height = PhysVal( 20,        'pc'   )

# constants
pi     = PhysVal( 3.1415926, '1' )
He_H   = PhysVal( 0.1, '1' )
NA     = PhysVal( 6 * 10**23, '1')

m_H    = PhysVal( 1 / NA.value, 'g' )
m_He   = PhysVal( 4 / NA.value, 'g' )

# volume = M_gal / ( pi * Radius**2 *  Height)
volume  = pi * Radius * Radius * Height

# number particles * m_particle    = M_gal 
# ( N_H * m_H + N_He * m_He )      = M_gal 
# ( N_H * m_H + N_H / 10 * m_He )  = M_gal
# N_H = M_gal / ( m_H + m_He / 10 )
N_H = M_gal / ( m_H + m_He / 10 ) # 1.714+33 M_sun / g

# calc average number density
num_density = N_H / volume        # 1.212+29 M_sun / g / 1 * kpc * kpc * pc

# convert to unit of 1 / cm^3
pc  = 3 * 10**18     # cm
kpc = 1000 * pc      # cm
g   = 1              # g
M_sun = 2 * 10**33   # g

# just eval the unit of PhysVal attr
# ANS : Prob 1.1: number density of H is -> 8.98 1/cm^3
print("Prob 1.1 (a): number density of H is -> {:.3g} 1/cm^3".format(
    num_density.value  *  eval(num_density.unit)
))

# Prob 1.1(b) : 
# ρb / <ρb> = Nb / <Nb>
# <Nb> = photon number density (4.11*10**8 m^-3) * baryon abundance (2.75 * 10^-8 h^2) 
mean_number_density = 2.75 * 10**(-8) * 4.11 * 10**8 / (10**2)**3 * (0.7)**2
print("Prob 1.1 (b): ρb / <ρb> = Nb / <Nb> = {:.3g}".format(
    num_density.value  *  eval(num_density.unit) / mean_number_density 
))
print('''Lower. If there's a higher concentration in the galaxy, then the structure of the galaxy will be changed by the
structure of the dark matter, which is not the case. Baryons have more structures in the galaxtic plane than dark matter halos,
so the concentration for baryons should be higher.''')

# Prob 1.2
# mean free path = 1 / cross-section (pi * radius^2) / number density
atom_radius = PhysVal( 1.5, 'A' )
n_H         = PhysVal( 30, 'cm**(-3)' )

mean_free_path = 1 / (pi * atom_radius * atom_radius * n_H)

# unit converter
cm = 1       # cm
A  = 10**-8  # cm

print('''Prob 1.2 : mean free path  = 
\t= 1 / cross-section (pi * radius^2) / number density
\t= {:.3g} cm'''.format( mean_free_path.value * eval(mean_free_path.unit) ))

# Prob 3:
# Contribution sources:
# 1) radiation; 2) stellar wind; 3) ejecta.
print("Prob 3: 3 sources contribute to momentum and energy to ISM: 1) radiation; 2) stellar wind; 3) ejecta") 
life_time       = PhysVal(3 * 10**6, 'yr')
luminosity      = PhysVal(3 * 10**39, 'erg / s')
velocity_wind   = PhysVal(5000, 'km / s')
mass_loss_rate  = PhysVal(10**-5, 'M_sun / yr')
ejecta_mass     = PhysVal(5, 'M_sun')
ejecta_velocity = PhysVal(5000, 'km / s')

# constants
speed_of_light = PhysVal(3 * 10**5, 'km / s')

# unit converter
cm  = 1                      # cm
g   = 1                      # g
s   = 1                      # s
erg = cm**2 * g / s**2       # cm^2 g / s^2
km  = 10**5                  # cm
yr  = 365 * 24 * 60 * 60     # s

# 1) radiation
# energy = luminosity * lifetime
# momentum = energy / speed of light
radiation_energy   = luminosity * life_time
radiation_momentum = radiation_energy / speed_of_light

print("1) radiation energy = {:.3g} erg; radiation momentum = {:.3g} g cm /s".format(
    radiation_energy.value * eval(radiation_energy.unit),
    radiation_momentum.value * eval(radiation_momentum.unit)
))

# 2) stellar wind
# energy   = 1 / 2 m v^2 = 1/2 mass_loss_rate * life_time * velocity_wind^2
# momentum = mass_loss_rate * life_time * velocity_wind
wind_energy = 0.5 * mass_loss_rate * life_time * velocity_wind * velocity_wind
wind_momentum = mass_loss_rate * life_time * velocity_wind

print("2) stellar wind energy = {:.3g} erg; stellar wind momentum = {:.3g} g cm /s".format(
    wind_energy.value * eval(wind_energy.unit),
    wind_momentum.value * eval(wind_momentum.unit)
))

# 3) ejecta
# energy   = 1 / 2 ejecta_mass * ejecta_velocity**2
# momentum = ejecta_mass * ejecta_velocity
ejecta_energy  = 0.5 * ejecta_mass * ejecta_velocity * ejecta_velocity
ejecta_momentum = ejecta_mass * ejecta_velocity

print("3) ejecta energy = {:.3g} erg; ejecta momentum = {:.3g} g cm / s".format(
    ejecta_energy.value * eval(ejecta_energy.unit),
    ejecta_momentum.value * eval(ejecta_momentum.unit)
))
