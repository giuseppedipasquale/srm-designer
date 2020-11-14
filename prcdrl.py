import numpy as np
import matplotlib.pyplot as plt
        
R = 198 #J/(kg K)
k = 1.139

Dc = 75                                             # [mm]
Lc = 470                                            # [mm]

d0 = 20                                             # [mm]
D0 = 69                                             # [mm]
l0 = 115                                            # [mm]
MEOP = 6                                          # [MPa]

N = 4
inib_internal = 1
inib_external = 0
inib_lat = 1

rho_g = 1.795                                       # [g/cm^3]
T0 = 1634                                           # [K]
# _____________________________________________________________________
# DATA AND KN TAB

"""
    This section determines the throat diameter and area.
"""

Vc = np.pi/4*Lc*Dc**2
print(Vc)
lg0 = N*l0

interval = np.arange(0,50+1,1)

xinc = 0.49                                         # [mm] 
xfinal = (D0-d0)/2                                  # [mm] 

x = np.arange(0,xfinal+xinc,xinc)                   # [mm]   
d = d0 + 2*x*inib_internal                          # [mm]
D = D0 - 2*x*inib_external                          # [mm]
L = lg0 - (2*N*x)*inib_lat                          # [mm]
t_web = (D-d)/2                                     # [mm]

A_be = inib_lat*(2*N*np.pi/4)*(D**2-d**2)           # [mm^2]
A_bc = inib_internal*np.pi*d*L                      # [mm^2]  
A_bs = inib_external*np.pi*D*L                      # [mm^2]
A_b = A_be+A_bc+A_bs                                # [mm^2]

a = 32.954
b = 44.108
c = -1.1025
KN_max = a + b*MEOP + c*MEOP**2

A_t0 = max(A_b)/KN_max                              # [mm^2]
d_t0 = np.sqrt(4*A_t0/np.pi)                        # [mm]
print(d_t0/10,"cm")
print(KN_max)
print(xfinal)
A_t = np.pi/4*(d_t0)**2                             # [mm^2]
KN = A_b/A_t
# _____________________________________________________________________
# PRESSURE

"""
    This section calculates the chamber pressure over time.
"""
xincp = 0.02#0.0293764988009578
xp = np.arange(0,xfinal,xincp)

dp = np.zeros(len(xp))
Dp= np.zeros(len(xp))
Lp= np.zeros(len(xp))
t = np.zeros(len(xp))
r = np.zeros(len(xp))
p = np.zeros(len(xp))
m_gen = np.zeros(len(xp))
m_noz = np.zeros(len(xp))
m_sto = np.zeros(len(xp))
mass_sto = np.zeros(len(xp))
rho_prod = np.zeros(len(xp))

dp[0] = d[0]
Dp[0] = D[0]
Lp[0] = L[0]
for i in range(1,len(xp)):
    xp[i] = round(xp[i],4)
    dp[i] = round(dp[i-1] + 2*xincp*inib_internal,2)  
    Dp[i] = Dp[i-1] - 2*xincp*inib_external
    Lp[i] = Lp[i-1] - 2*xincp*N*inib_lat
t_webp = (Dp-dp)/2

A_tp = np.pi/4*(d_t0)**2*np.ones(len(xp))           # [mm^2]
A_star = A_tp/(1000**2)                             # [m^2]

A_duct = np.pi/4*Dc**2 - np.pi/4*(Dp**2-dp**2)
A_duct_t = A_duct/A_tp


a_p = 8.26                                          # [mm/s]
n_p = 0.319                                         # 

V_grain = np.pi/4*(Dp**2-dp**2)*Lp                  # [mm^3]
V_g_m = V_grain/1000**3                             # [m^3]

V_free = (Vc/1000**3-V_g_m)                         # [m^3]

m_grain = rho_g*V_grain/1000**2                     # [kg]


p[0] = 0.101                                        # [MPa]
r[0] = a_p*p[0]**n_p

for i in range(1,len(xp)):
    r[i] = a_p*p[i-1]**n_p
    t[i] = t[i-1] + xincp/r[i]
    m_gen[i] = (m_grain[i-1]-m_grain[i])/(t[i]-t[i-1])
    m_noz[i] = ((p[i-1]-0.101)*1000000*A_star[i]/np.sqrt(R*T0))*np.sqrt(k)*(2/(k+1))**((k+1)/(2*(k-1)))    
    m_sto[i] = m_gen[i]-m_noz[i]
    if m_sto[i]*(t[i]-t[i-1])+mass_sto[i-1] < 0:
        mass_sto[i] = 0
    else:
        mass_sto[i] = mass_sto[i-1]+m_sto[i]*(t[i]-t[i-1])
    rho_prod[i] = mass_sto[i]/V_free[i]
    p[i] = (rho_prod[i]*R*T0+1e6*0.101)/1e6

tbinc = 0.00153
t_tailoff = np.arange(t[-1],t[-1]+0.25,tbinc)
cstar = 894
p_tailoff = np.zeros(len(t_tailoff))
for i in range(0,len(t_tailoff)):
    p_tailoff[i] = p[-1]*np.exp(-R*T0*A_star[-1]*(t_tailoff[i]-t[-1])/Vc*1000000000/cstar)

print_to_file = 0

if print_to_file == 1:
    f = open("out.txt","w")
    f.write("i,   x,       tweb,   d,     D,     L,     At,    A*,       Aduct,p0,    r,      t,      Vgr,     Vgr,      Vfree, mgrain, mgen, mnoz,\n")
    for i in range(0,len(xp)):
       f.write("%03d, %07.4f, %06.3f, %05.2f, %05.2f, %05.1f, %05.1f, %08.6f, %04d, %05.3f, %06.3f, %06.4f, %07d, %08.6f, %07.5f, %06.4f, %06.4f, %06.4f\n" %(i,xp[i],
                                           t_webp[i],dp[i],Dp[i],Lp[i],A_tp[i],A_star[i],A_duct[i], p[i],
                                           r[i], t[i],V_grain[i], V_g_m[i], V_free[i], m_grain[i], m_gen[i], m_noz[i]))
    f.close()

plt.figure()
plt.plot(t,m_gen,'r',label="MFR generated")
plt.plot(t,m_noz,'b',label="MFR nozzle")
plt.plot(t,m_sto,'g',label="MFR stored")
plt.legend()
plt.grid()

plt.figure()
plt.plot(t,mass_sto)
plt.grid()

T = np.concatenate([t, t_tailoff])
P = np.concatenate([p, p_tailoff])

F = P*1e6*A_star[1]*1.3

plt.figure()
plt.xlabel("t [s]")
plt.ylabel("p [MPa]")
plt.plot(T,P)
plt.grid()

plt.figure()
plt.xlabel("t [s]")
plt.ylabel("F [N]")
plt.plot(T,F)
plt.grid()

plt.show()
