pagoPorHora = float(input("Hourly wage: "))
HorasTrabajadas = float(input("Hours worked: "))
DiaTrabajado = input("Day of the week: ")

if DiaTrabajado == 'Sunday':
    
    salarioEspecial = pagoPorHora *2
    salarioTotal = salarioEspecial * HorasTrabajadas
    
    print(f"Daily wages: {salarioTotal} euros")
    
elif DiaTrabajado != "Sunday":
    
    salarioTotal = pagoPorHora * HorasTrabajadas
    
    print(f"Daily wages: {salarioTotal} euros")


