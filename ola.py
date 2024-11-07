#Calcular el promedio de 3 edades
#Calcular el promedio de 3 notas
#Calcular el promedio de 3 mesadas
def promedio (a,b,c):
   return (a+b+c)/3

def especialidad():
   validas_especialidad= {"programacion", "administracion", "contabilidad"}
   while True:
      especialidad = input ("Introduce tu especialidad (programacion, administracion, contabilidad)")

      if especialidad in validas_especialidad:
         print(f"Especialidad {especialidad} ingresada correctamente")
         return especialidad
      else:
         print("La opcion no existe")

def nota():
    nota=0
    while ((nota<1)or(nota>7)):
      nota=float(input("Nota valida: "))
      if nota<0:
         print("No")
      if nota>7:
         print("No existe esa nota")
    return nota

def mesada():
    mesada=0

    while mesada>0:
      mesada=int(input("Mesada valida plox: "))
      if mesada<0:
         print("no")
      if mesada>20000:
         print("No")
    return mesada

def edad():
    edad=0
    while ((edad<10)or(edad>20)):
      edad=int(input("Edad valida plox: "))
      if edad<10:
         print("Edad muy baja")
      if edad>20:
         print("Sal del sueño de ser joven")
    return edad
    
nombre = (0,0,0)
edad = (0,0,0)
nota = (0,0,0)
especialidad= (0,0,0)



print("")

print("Bienvenido")

for i in range(0,3,1):
   print("Datos alumno",i+1, [i])
   print("Ingrese edad",i+1, edad[i])
   print("Ingrese nota",i+1, nota[i])
   print("Ingrese mesada",i+1, mesada[i])
   print("Ingrese especialidad",i+1, especialidad[i])

prom_e = promedio (edad[0],edad[1],edad[2])
prom_n = promedio (nota[0],nota[1],nota[2])
prom_m = promedio (mesada[0],mesada[1],mesada[2])

print(f"El promedio de los edades de los 3 alumnos es: {prom_e}")
print(f"El promedio de los nota de los 3 alumnos es: {prom_n}")
print(f"El promedio de los mesada de los 3 alumnos es: {prom_m}")