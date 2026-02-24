import numpy as np
import time

def get_sin_wave(freq, time):
    sin1 = np.sin(2*np.pi*freq*time) + 1
    sin = sin1/2
    return sin

def wait_for_sampling_period(sampling_frequency):
    sampling_period = 1.0 / sampling_frequency
    time.sleep(sampling_period)

def get_triang_wave(freq, time):
    T = 1/freq
    x = time % T
    if x <= T/2:
        return (2/T)*x
    return 1-(2/T)*(x-T/2)