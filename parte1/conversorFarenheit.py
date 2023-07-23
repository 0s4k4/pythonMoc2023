temperature = float(input("Please type in a temperature (F): "))
celsius = (temperature - 32) * 5/9

if celsius < 0:
    print(f"{temperature} degrees Fahrenheit equals {celsius} degrees Celsius")
    print("Brr! It's cold in here!")
    
elif celsius >= 0:
    print(f"{temperature} degrees Fahrenheit equals {celsius} degrees Celsius")