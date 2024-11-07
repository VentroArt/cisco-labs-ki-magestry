import numpy as np
import matplotlib.pyplot as plt

gamma = 0.5  # demping

def amplitude_with_damping(A0, t, gamma):
    return A0 * np.exp(-gamma * t)
amplitude_E1 =  0.0034 # meters

wave_speed_e1 = 393.78  # wave speed for E1
scale_length = 0.597  
time_points = np.linspace(0, 10, 100)


dt = 0.000001 # time change
dx = 0.0005  
x = np.arange(0, scale_length, dx) 


plt.figure(figsize=(10, 6))

wave_number = 2 * np.pi / scale_length  # wavenumber
omega = 2 * np.pi * wave_speed_e1 / scale_length  # corner frequency

for t in time_points:
    y = amplitude_with_damping(amplitude_E1, t , gamma) * np.sin(wave_number * x - omega * t)  # function of waving E1 string
    plt.plot(x, y, label=f'Time {t:.2f} s')

plt.xlabel('Position along string (meters)')
plt.ylabel('Displacement (meters)')
plt.title('Waveform of String E1 Over Time')
plt.legend(loc='upper right')
plt.show()
