import calcu_2 as operaciones

operacionesBasicas = {
   "suma" : operaciones.suma,
   "resta" : operaciones.resta,
   "multiplicacion" : operaciones.multiplicacion,
   "division" : operaciones.division,
   "potencia" : operaciones.potencia,
   "raiz": operaciones.raiz,
   "cuadratica":operaciones.cuadratica
}
operacionesTrigonometricas = {
   "seno" : operaciones.seno, #Radianes 
   "coseno" : operaciones.coseno, #Radianes
   "tangente" : operaciones.tangente #Radianes
}

def calculadora():
   while True:
      resultado = 0
      opcion = input("Ingrese la operacion que desee hacer (escribir salir para salir): ").lower()
      if opcion == "salir":
         print("Bye Bye")
         break
      if opcion not in operacionesTrigonometricas and opcion not in operacionesBasicas:
         print ("Opcion no reconocida")
         continue
      try:
         if opcion in operacionesBasicas:
            numero1 = float(input("Ingrese su primer valor: "))
            if opcion == "raiz":
               resultado = operacionesBasicas["raiz"](numero1)
            else:    
               numero2 = float(input("Ingrese su primer valor: "))
               resultado = operacionesBasicas[opcion](numero1, numero2)
         if opcion in operacionesTrigonometricas:
            numero1 = float(input("Ingrese el numero en Radianes: "))
            resultado = operacionesTrigonometricas[opcion](numero1)
      except ValueError: 
            print ("Error, ingrese numeros validos")
            continue
      print (f"Su resultado es {resultado}")
1.5708

# calculadora()
print(operaciones.cuadratica(-1,1/2,5))