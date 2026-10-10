def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

value = float(input("Temperature in Celsius: "))
print(f"Fahrenheit: {celsius_to_fahrenheit(value):.2f}")
