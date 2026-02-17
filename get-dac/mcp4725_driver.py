import smbus

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = False):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00

        self.verbose = verbose
        self.dynamic_range = dynamic_range

    def deinit(self):
        self.bus.close()

    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП должны подаваться только целые числа")

        if not (0 <= number <= 4095):
            print("Число выходит за разрядность MCP4752 (12 бит)")

        first_byte = self.wm | self.pds | number >> 8
        second_byte = number & 0xFF
        self.bus.write_byte_data(0x61, first_byte, second_byte)

        if self.verbose:
            print(f"число: {number}, отправленные по I2C данные [0x{(self.address << 1):02X}, 0x{first_byte:2X}, 0x{second_byte:2X}]\n")

    def set_voltage(self, voltage):
        if (0 > voltage or voltage > 4095):
            print()
        self.set_number(int((voltage/self.dynamic_range) * 4095))
       
if __name__ == "__main__":
    try:
        dac = MCP4725(5.21, 0x61, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()