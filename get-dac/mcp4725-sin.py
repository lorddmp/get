import mcp4725_driver as dr
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

try:
    mcp = dr.MCP4725(5.0, 0x61, True)

    while True:
        try:
            voltage = sg.get_sin_wave(signal_frequency, time.time())*amplitude
            mcp.set_voltage(voltage)
            sg.wait_for_sampling_period(sampling_frequency)
        
        except ValueError():
            print(("Введено не число"))
finally:
    mcp.deinit()