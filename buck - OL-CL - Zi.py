# -*- coding: utf-8 -*-
from math import pi, log10, sqrt
from control import tf, bode_plot

L= 10e-6; rL=0.05; C=33e-6;rC=0.1; R=1; 
Vi= 10; D=0.53;
# Output voltage and current
Vo=D*Vi/(1 + rL/R)
IL=Vo/R
# PI compensator
R1=1.81e3; R2=1.81e3; C2=10e-9
wz=1/(R2*C2)
s = tf('s')
Zi_ol= (R/D**2)*( L*C*(1+rC/R)*s**2 + (L/R+rC*C+rL*C+rL*rC*C/R)*s + 1+rL/R )/ \
    (1 + (R+rC)*C*s)
Zi_cl= (1/D)*( (1+(R+rC)*C*s)*(rL+L*s) + (Vi*(1+s/wz)/(s/wz)+1)*R*(1+rC*C*s)  )/\
    (  D*(1 + (R+rC)*C*s) -IL*(1+s/wz)/(s/wz)*R*(1+rC*C*s) )
# Plot Plant's Bode
# Note that once Hz is true, omega_limits are in Hz

mag, phase, omega = bode_plot(Zi_ol, dB=True, Hz=True, omega_limits=(10,1000e3),\
                              omega_num=100, color="red" )

mag, phase, omega = bode_plot(Zi_cl, dB=True, Hz=True, omega_limits=(10,1000e3),\
                              omega_num=100, color="blue" )


    
    
   
    # Print a few points
print("F(Hz)               Magnitude(dBOhm)       Phase(deg)")
print("----------------------------------------------------------")
i=20
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=40
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=60
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=70
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)
i=80
print(omega[i]/2/pi, 20*log10(mag[i]), phase[i]*180/pi)


