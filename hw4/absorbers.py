'''
absorbers.py: compute for hw4
'''
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

# get gradient from cmap colors
cmap = cm.get_cmap("viridis")

# redshift 
z = 2

save_figure = lambda filename : plt.savefig(filename, dpi=300, format="pdf")

class Ion:

    # cgs units
    c = 3 * 10**10


    def __init__(self, lrest, f, gamma, Wlrest):
        self.lrest = lrest
        self.f     = f
        self.gamma = gamma
        self.Wlrest    = Wlrest

        self.W = self.Wl2W(Wlrest, lrest)

    @staticmethod
    def Wl2W(Wl, l):
        return Wl / l

    @staticmethod
    def tau_0(f, l, b, N):
        '''
        in cgs
        '''
        return 1.497e-2 * f * l / b * N

    def approx_W_small(self, b, tau_0):
        '''
        Approximated W if tau_0 < 1.25393
        '''
        W = np.sqrt(np.pi) * b / self.c * tau_0 / (1 + tau_0 / (2 * np.sqrt(2)))
        return W

    def approx_W_large(self, b, tau_0):
        '''
        Approximated W if tau_0 > 1.25393
        '''
        term_ln_tau = (2 * b / self.c)**2 * np.log(tau_0 / np.log(2))
        term_gamma  = b / self.c * self.gamma * self.lrest / self.c * (tau_0 - 1.25393) / np.sqrt(2)

        return np.sqrt( term_ln_tau + term_gamma )

    def calc_W(self, N, b):
        '''
        calc W based on given N and b.

        N (array)
        b (float)
        '''
        tau_0 = self.tau_0(
            self.f, self.lrest, b, N
        )

        ind = tau_0 >= 1.25393

        W = np.empty(ind.shape)

        W_small = self.approx_W_small(b, tau_0)
        W_large = self.approx_W_large(b, tau_0)

        W[ ind] = W_large[ind]
        W[~ind] = W_small[~ind]

        return W

def do_loglog_plot(ion, N, all_b):
    '''
    Plotting for C.O.G in 1(a)
    '''
    # plot for different bs
    for i,b in enumerate(all_b):
        W = ion.calc_W(N, b)

        plt.loglog(N, W, label="b = {} km/s".format(b / 10**5), color=cmap(i / len(all_b)))
        plt.xlabel(r"$N_{\ell}$")
        plt.ylabel(r"$W$")
    plt.legend()    

def do_loglog_plot_Wlambda(ion, N, all_b):
    '''
    Plotting for C.O.G in 1(a)
    '''
    # plot for different bs
    for i,b in enumerate(all_b):
        W = ion.calc_W(N, b)

        Wl = W * ion.lrest * 10**8 # A

        plt.loglog(N, Wl, label="b = {} km/s".format(b / 10**5), color=cmap(i / len(all_b)))
        plt.xlabel(r"$N_{\ell}$")
        plt.ylabel(r"$W^{\mathrm{rest}}_\lambda$ $\AA$")
    plt.legend()


# provided by the question
all_b = np.array([1, 2, 3, 5, 10]) * 10**5 # cm/s

log_NFe = np.linspace(12, 16, 100)
log_NC  = np.linspace(13, 17, 100)

# unit convert
NFe = 10**( log_NFe ) # cm^-2
NC  = 10**( log_NC  ) # cm^-2

ion_fe_1 = Ion(2382.7642 * 10**-8, 0.32, 3.13e8, 0.051)
ion_fe_2 = Ion(2249.8768 * 10**-8, 0.00182, 3.31e8, 0.0047)
ion_c    = Ion(1334.5323 * 10**-8, 0.12780, 2.880e8, 0.060)

# 1(a) do plots
do_loglog_plot(ion_fe_1, NFe, all_b); save_figure("images/W_N_Fe_II_1.pdf"); plt.clf()
do_loglog_plot(ion_fe_2, NFe, all_b); save_figure("images/W_N_Fe_II_2.pdf"); plt.clf()
do_loglog_plot(ion_c, NC, all_b); save_figure( "images/W_N_C_II.pdf"); plt.clf()

do_loglog_plot_Wlambda(ion_fe_1, NFe, all_b)
plt.hlines(ion_fe_1.Wlrest, min(NFe), max(NFe))
save_figure("images/Wl_N_Fe_II_1.pdf"); plt.clf()

do_loglog_plot_Wlambda(ion_fe_2, NFe, all_b)
plt.hlines(ion_fe_2.Wlrest, min(NFe), max(NFe))
save_figure("images/Wl_N_Fe_II_2.pdf"); plt.clf()

do_loglog_plot_Wlambda(ion_c, NC, all_b)
plt.hlines(ion_c.Wlrest, min(NC), max(NC))
save_figure("images/Wl_N_C_II.pdf"); plt.clf()

# 1(b)
dv_Fe_1 = 2 * np.sqrt(np.log(2)) * 1.5
print("(dv)FeII_1 = {};".format(dv_Fe_1))
print("(dv)FeII_obs_1 = {};".format(dv_Fe_1 * (1 + z)))

# 1(d) thermal broadening
calc_T = lambda M_mH, dv : 1/2.15**2 * M_mH * dv**2 * 100
T_Fe_1 = calc_T(56, 2.5)
print("At least T for Fe II {}.".format(
    T_Fe_1
))

# 1(e)
Mfe = 56
MC  = 12
b_fe = 2.5
b_C = np.sqrt(Mfe / MC) * b_fe
print("b for CII by thermal: {}".format(b_C))

do_loglog_plot_Wlambda(ion_fe_1, NFe, all_b)
plt.hlines(ion_fe_1.Wlrest, min(NFe), max(NFe))
save_figure("images/Wl_N_Fe_II_1_more_b.pdf"); plt.clf()
