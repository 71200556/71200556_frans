celcius_to_fahrenheit = lambda C: int((9/5) * C + 32)
celcius_to_reamur = lambda C: int(0.8 * C)

# Tes
print("Input C = 100, Output F =", celcius_to_fahrenheit(100))
print("Input C = 80, Output R =", celcius_to_reamur(80))
print("Input C = 0, Output F =", celcius_to_fahrenheit(0))