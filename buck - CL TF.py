# -*- coding: utf-8 -*-
from math import pi, log10, sqrt
from control import tf, bode_plot
L= 10e-6; rL=0.05; C=33e-6;rC=0.1; R=1; Vi= 10; D=0.53;
# PWM modulator gain
kd=1
# PI compensator
R1=1.81e3; R2=1.81e3; C2=10e-9
wz=1/(R2*C2)
# Transfer functions
s = tf('s')
# Control-to-output
Gd = Vi*(1+rC*C*s)/\
    (L*C*(1+rC/R)*s**2 + (L/R+rC*C+rL*C+rL*rC*C/R)*s + 1 + rL/R)
Cp=(1+s/wz)/(s/wz) # Compensator
H=1 # Sensor
# Loop gain
T=Cp*kd*Gd*H
# Closed-loop response
Gcl= Cp*kd*Gd/(1+T)
# Plot Plant's Bode
# Note that once Hz is true, omega_limits are in Hz

mag, phase, omega = bode_plot(Gd, dB=True, Hz=True, omega_limits=(10,1000e3),\
                              omega_num=100, color="red" )
mag, phase, omega = bode_plot(Gcl, dB=True, Hz=True, omega_limits=(10,1000e3),\
                              omega_num=100, color="blue" )
        
    
# Print a few points
print("F(Hz)               Magnitude(dB)       Phase(deg)")
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


# mag1, phase1, omega1 = bode_plot(Zo, dB=True, Hz=True, omega_limits=(10,1000e3),\
#                               omega_num=100 )

