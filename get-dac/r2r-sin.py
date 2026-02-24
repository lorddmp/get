import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000
gpio_bits = [16, 20, 21, 25, 26, 17, 27, 22]

if __name__ == "__main__":
    try:
        dac = r2r.R2R_DAC(gpio_bits, dynamic_range = 3.3, verbose = True)

        while True:
            voltage = sg.get_sin_wave(signal_frequency, time.time())
            dac.set_voltage(voltage*amplitude)
            sg.wait_for_sampling_period(sampling_frequency)


    finally:
        dac.deinit()