##crear un programa que me pida mis datos para poderlos poner en un resumen de mi cv


nombre = input("Ingresa tu nombre: ")
edad = input("Cual es tu edad: ")
carrera = input("Ingresa tu carrera: ")
especialidad = input("Ingresa cual es tu especialidad: ")
skiil1 = input("Ingresa tu skill numero 1: ")
skill2 = input("Ingresa tu skill numero 2: ")
skill3 = input("Ingresa tu skill numero 3: ")
salarioMenor = input("Ingresa tu salario menor: ")
salarioMaximo = input("Ingresa tu salario Maximo: ")

print(f"Mi nombre es {nombre}, Tengo {edad} tengo una carrera en {carrera}.\n\nMis especialidades son:\n -{skiil1}\n -{skill2}\n -{skill3}\n\nBusco un salario como minimo de {salarioMenor} y como maximo de {salarioMaximo}")