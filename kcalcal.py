# Calculadora TMB - GET - Superavit/Deficit - Macronutrientes diarios.
#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------

def tmb(x, y, z, s):
    if s == "H" or s == "h":
        Harris1918 = 66.5 + (13.8 * x) + (5 * y) - (6.8 * z)
        Harris1984 = 88.3620 + (13.3970 * x) + (4.7990 * y) - (5.6770 * z)
        Harris1990 = (10 * x) + (6.25 * y) - (5 * z) + 5
        Eric = x * 22
    elif s == "M" or s == "m":
        Harris1918 = 665 + (9.6 * x) + (1.85 * y) - (4.7 * z)
        Harris1984 = 447.5930 + (9.2470 * x) + (3.0980 * y) - (4.33 * z)
        Harris1990 = (10 * x) + (6.25 * y) - (5 * z) - 161
        Eric = x * 22
    tasaMetabolicaBasal = (Eric + Harris1918 + Harris1984 + Harris1990) / 4
    return tasaMetabolicaBasal

def ejercioFisico(x, y):
    if x == 1:
        get = y * 1.45 * 1.1 #1.1 Refiere a Termogenesis
    if x == 2:
        get = y * 1.65 * 1.1
    elif x == 3:
        get = y * 1.85 * 1.1
    elif x == 4:
        get = y * 2.05 * 1.1
    return get

def macronutrientes(x, y, z):
    if x == 1: #Perder
        proteina = y * 2.75
        grasa = y * 0.8
        carbos = ((z - 350) - (proteina * 4 + grasa * 9)) / 4
    if x == 2: #Ganar
        proteina = y * 2.05
        grasa = y * 1.20
        carbos = ((z + 550) - (proteina * 4 + grasa * 9)) / 4
    return proteina, grasa, carbos

# Bloque de menú
#----------------------------------------------------------------------------------------------

while True:
    objetivo = int(input("¿Cuál es su objetivo?\nIngrese [1] - Perder Peso. \nIngrese [2] - Ganar Peso.\nRespuesta: "))
    if objetivo == 1 or objetivo == 2:
        break
    else:
        print("ERR0R ---> Ingreso un número invalido. Intentelo de nuevo.\n")
        
peso = float(input("Ingrese su peso actual: "))
altura = float(input("Ingrese su altura actual: "))
edad = int(input("Ingrese su edad: "))
while True:
    sexo = str(input("Ingrese [H] para Hombre o [M] para Mujer: "))
    if sexo == "m" or sexo == "M" or sexo == "H" or sexo == "h":
        break
    else:
        print("ERR0R ---> Ingreso un caracter invalido. Intentelo de nuevo\n")
tasaMetabolica = tmb(peso, altura, edad, sexo)

print("\n\nEn este programa se considera que usted ya realiza entrenamientos de fuerza entre 3 a 6 días semanales.")
while True:
    actividadFisica = int(input("¿Cuál es su nivel de actividades cardiovasculares?\n[1] - Sedentario\n[2] - Ligeramente activo\n[3] - Activo\n[4] - Muy activo\nRespuesta: "))
    if actividadFisica in [1, 2, 3, 4]:
        break
    else:
        print("ERR0R ---> Ingreso un número invalido. Intentelo de nuevo\n")
gastoEnergeticoTotal = ejercioFisico(actividadFisica, tasaMetabolica)
gastoEnergeticoTotalInt = int(gastoEnergeticoTotal)
tasaMetabolicaInt = int(tasaMetabolica)
print(f"\nSu TMB es de {tasaMetabolicaInt} Kcal.\nSu GET es de {gastoEnergeticoTotalInt} Kcal.")

prote, gra, carbo = macronutrientes(objetivo, peso, gastoEnergeticoTotal)
proteina = int(prote)
grasa = int(gra)
carbos = int(carbo)
print(f"Sus macronutrientes diarios son de aproximadamente:\n{proteina}gr de Proteinas  {grasa}gr de Grasa  {carbos}gr de Carbohidratos")

if objetivo == 1:
    deficit = gastoEnergeticoTotalInt - 350
    print(f"Un total de {deficit} calorias.")
else:
    superavit = gastoEnergeticoTotalInt + 550
    print(f"Un total de {superavit} calorias.")