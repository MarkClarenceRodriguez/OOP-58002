class TempConversion:
    def __init__(self, temp):
        self.__temp = temp

    def __Fahrenheit_to_Celsius(self):
        return (self.__temp - 32) * 5 / 9

    def __Kelvin_to_Celsius(self):
        return self.__temp - 273.15

    def __Celsius_to_Fahrenheit(self):
        return (self.__temp * 9 / 5) + 32

    def __Kelvin_to_Fahrenheit(self):
        return (self.__temp * 1.8) - 459.67

    def __Celsius_to_Kelvin(self):
        return self.__temp + 273.15

    def __Fahrenheit_to_Kelvin(self):
        return (self.__temp + 459.67) / 1.8

    def convert_temperatures(self):
        fahrenheit_to_celsius = self.__fahrenheit_to_celsius()
        kelvin_to_celsius = self.__kelvin_to_celsius()
        celsius_to_fahrenheit = self.__celsius_to_fahrenheit()
        kelvin_to_fahrenheit = self.__kelvin_to_fahrenheit()
        celsius_to_kelvin = self.__celsius_to_kelvin()
        fahrenheit_to_kelvin = self.__fahrenheit_to_kelvin()

        return f"Fahrenheit to Celsius: {fahrenheit_to_celsius}\nKelvin to Celsius: {kelvin_to_celsius}\nCelsius to Fahrenheit: {celsius_to_fahrenheit}\nKelvin to Fahrenheit: {kelvin_to_fahrenheit}\nCelsius to Kelvin: {celsius_to_kelvin}\nFahrenheit to Kelvin: {fahrenheit_to_kelvin}"
