import math

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion (a,b):
    return a * b

def division (a,b):
    if b != 0:
        return a / b
    else:
        print ("No es posible dividir por 0")

def potencia (a, b):  
    return a**b

def raiz (a): 
    if a >= 0: 
        return math.sqrt(a) 
    else:
        print ("No es posible calcular una raiz negativa")

def seno(a):
    return math.sin(a)

def coseno(a):
    return math.cos(a)

def tangente(a):
    return math.tan(a)

def cuadratica(a, b, c):
    return (-b+raiz(b**2-4*a*c))/(2*a), (-b-raiz(b**2-4*a*c))/(2*a)

def integralSimple():
    pass

def calculadora ():
    print("""

    ////////////////////////////////////////////////
    //  Suma                  Seno                //
    //  Resta                 Coseno              //
    //  Multiplicacion        Tangente            //
    //  División                                  //
    //  Cuadratica                                //        
    //  Salir                                     //
     //////////////////////////////////////////////""")
    
    # while True:
    #     resultado = 0
    #     op_1 = input("Ingrese la operacion que desee hacer (escribir salir para salir): ")
    #     if op_1.lower() == "salir":  
    #         print ("Bye bye")
    #         break
    #     if op_1 not in ["suma","resta","multiplicacion","division","Potencia","raiz","sen","cos","tan"]:
    #         print ("Opcion no reconocida")
    #         continue

    #     try: 
    #         if op_1 in ["suma","resta","multiplicacion","division","Potencia","raiz","sen","cos","tan"]:  
    #             num_1 = float(input("Ingrese su primer valor: "))  
    #             num_2 = float(input("Ingrese su segundo valor: ")) 
    #             num_1 = float(input("Ingrese su valor para raiz cuadrada o angulo en radianes para funciones trignonometricas "))   
    #     except ValueError: 
    #         print ("Error, ingrese numeros validos")
    #         continue
    #     if op_1 == "Suma":
    #         resultado = suma(num_1,num_2)  
    #     elif op_1 == "Resta":                   
    #         resultado = resta(num_1,num_2)     
    #     elif op_1 == "Multiplicacion":
    #         resultado = multiplicacion(num_1,num_2)    
    #     elif op_1 == "Division":
    #         resultado = division(num_1,num_2)    
    #     elif op_1 == "Potencia":        
    #         resultado = potencia(num_1,num_2)   
    #     elif op_1 == "Raiz":
    #         resultado = raiz(num_1)
    #     elif op_1 == "Sen":
    #         resultado = seno(num_1)
    #     elif op_1 == "Cos":
    #         resultado = coseno(num_1)
    #     elif op_1 == "Tan":
    #         resultado = tangente(num_1)
        
    #     print (f"Su resultado es {resultado}")


if __name__ == "__main__":
    calculadora()