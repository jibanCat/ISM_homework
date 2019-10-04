# ISM Homework 1

Draine problems can be found at https://www.astro.princeton.edu/~draine/book/problems.
pdf.

1. Draine Problem 1.1 part (a), and the following: [10 pts]
2. Draine Problem 1.2 [5 pts]
3. Energy and momentum input from a massive star: [10 pts]

## Prob 1.1 : Calculate the number density in the disk with mixture of He/H = 0.1

- The idea is to calculate the number of H particles and divide by volume.

```
volume = M_gal / ( pi * Radius**2 *  Height)
```

- Define physical values of the problem

```python
M_gal  = 4 * 10**9 'M_sun'
Radius = 15        'kpc'
Height = 20        'pc'
```

- constants

```python
He_H   = 0.1        # the ration between He/H
NA     = 6 * 10**23 # avogadro's number

m_H    = 1 / NA  'g' # atomic mass
m_He   = 4 / NA  'g' # atomic mass
```

```python
number particles * m_particle        = M_gal
=>  ( N_H * m_H + N_He * m_He )      = M_gal  # N_H : number of H; N_He: number of He
=>  ( N_H * m_H + N_H / 10 * m_He )  = M_gal  # m_H : mass of a H particle; m_He : mass of a He particle
=>  N_H = M_gal / ( m_H + m_He / 10 )

N_H = M_gal / ( m_H + m_He / 10 )    # 1.714+33 M_sun / g
```

- calculate average number density

```python
num_density = N_H / volume        # 1.212+29 M_sun / g / 1 * kpc * kpc * pc
```

- Convert to unit of 1 / cm^3

```python
pc  = 3 * 10**18     # cm
kpc = 1000 * pc      # cm
g   = 1              # g
M_sun = 2 * 10**33   # g
```

ANS : `number density of H is = 8.98 1/cm^3`

## Prob 1.1(b) :

Assume the ratio of mass density to average is the same us number density if we only consider a fixed value of atomic mass.

```
ρb / <ρb> = Nb / <Nb>
```

Using the relation of baryon abundance

```
<Nb> = photon number density  * baryon abundance
     = (4.11*10**8 m^-3)      * (2.75 * 10^-8 h^2)
     = 2.75 * 10**(-8) * 4.11 * 10**8 / (10**2)**3 * (0.7)**2
     = mean_number_density
```

So that

```
ρb / <ρb> = Nb / <Nb> = 1.62e+06
```

Lower. If there's a higher concentration in the galaxy, then the structure of the galaxy will be changed by the
structure of the dark matter, which is not the case. Baryons have more structures in the galactic plane than dark matter halos,
so the concentration for baryons should be higher.

## Prob 1.2

- The definition of mean free path:

```
mean free path = 1 / cross-section (pi * radius^2) / number density
               = 1 / (pi * atom_radius * atom_radius * n_H)
```

- Unit conversions

```python
atom_radius = 1.5     'Å'
n_H         = 30      'cm**(-3)'
Å           = 10**-8  'cm'
```

So that

```python
mean free path  =
	= 1 / cross-section (pi * radius^2) / number density
	= 4.72e+13 cm
```

# Prob 3:

- There are three kinds of contribution sources: 1) radiation; 2) stellar wind; 3) ejecta.

- The physical parameters defined in the question are

```python
life_time       = 3 * 10**6   'yr'
luminosity      = 3 * 10**39  'erg / s'
velocity_wind   = 5000        'km / s'
mass_loss_rate  = 10**-5      'M_sun / yr'
ejecta_mass     = 5           'M_sun'
ejecta_velocity = 5000        'km / s'
speed_of_light  = 3 * 10**5   'km / s'
```

The conversion of units to cgs is

```python
cm  = 1                      # cm
g   = 1                      # g
s   = 1                      # s
erg = cm**2 * g / s**2       # cm^2 g / s^2
km  = 10**5                  # cm
yr  = 365 * 24 * 60 * 60     # s
```

- First, consider radiation

Radiation energy and momentum defined as,
```
 energy = luminosity * lifetime
 momentum = energy / speed of light
```

If the star steadily emit light for his/her whole life time, then

```
radiation_energy   = luminosity * life_time
radiation_momentum = radiation_energy / speed_of_light
```

The results are

```python
radiation energy   = 2.84e+53  'erg'
radiation momentum = 9.46e+42  'g cm /s'
```

- Secondly, consider stellar wind

If we consider the stellar wind steadily emitting mass with the same velocity,

```
energy   = 1 / 2 m v^2 = 1/2 mass_loss_rate * life_time * velocity_wind^2
momentum = mass_loss_rate * life_time * velocity_wind
```

So that

```
wind_energy = 0.5 * mass_loss_rate * life_time * velocity_wind * velocity_wind
wind_momentum = mass_loss_rate * life_time * velocity_wind
```

```python
stellar wind energy   = 7.5e+51 'erg'
stellar wind momentum = 3e+43   'g cm /s'
```

- Thirdly, ejecta

```
energy   = 1 / 2 ejecta_mass * ejecta_velocity**2
momentum = ejecta_mass * ejecta_velocity
```

So that

```
ejecta_energy  = 0.5 * ejecta_mass * ejecta_velocity * ejecta_velocity
ejecta_momentum = ejecta_mass * ejecta_velocity
```

The results are,

```python
ejecta energy = 1.25e+51 'erg'
ejecta momentum = 5e+42  'g cm / s'
```

## Running the Script

- Requirements:
  - python 3+
  - no library installation requirements, it a pure python script

```bash
>> python process_hw1.py
```

```python
'''
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
```
