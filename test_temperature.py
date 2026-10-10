from temperature import celsius_to_fahrenheit

assert celsius_to_fahrenheit(0) == 32
assert celsius_to_fahrenheit(100) == 212
assert round(celsius_to_fahrenheit(-40), 5) == -40

print("All temperature tests passed.")
