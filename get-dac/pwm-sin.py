import pwm_dac as pd
import signal_generator as sg
import time

amplitude = 3.2
signsl_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        dac = pd.PWM_DAC(12, 500, 3.3, True)

        while True:
            voltage = sg.get_sin_wave(signsl_frequency, time.time())*amplitude
            dac.set_voltage(voltage)
            sg.wait_for_sampling_period(sampling_frequency)
    finally:
        dac.deinit()