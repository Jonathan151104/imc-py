#Le pedimos al usuario que ingrese su nombre(s) y se almacena en "n".
n = input("Ingrese su nombre(s) por favor: ")

#Le pedimos el apellido paterno o primer apellido y se almacena en "ap".
ap = input("Ingresa su apellido paterno por favor: ")

#Ahora el apellido materno o segundo apellido y se alamcena en "am".
am = input("Ingresa su apellido materno por favor: ")

#Mismo procedimiento para la edad, cabe decir que debe ser de tipo entero osea int() y se almacena en "e"
e = int (input("Ingresa tu edad en años por favor: "))

#Le pedimos el peso en kilogramos, puede tener decimales debe ser de tipo flotante float() y se aguarda en "p"
p = float(input("Ingresa tu peso o masa en kilogramos por favor: "))

#Le pedimos la altura, pero en metros y no centimetros hay que ponerle decimaal y debe ser flotante float()
est = float(input("Ingresa tu estatura en metros por favor: "))

"""Hacemos el calculo del IMC peso (Kg), entre estatura (m), multiplicadoce así misma."""
IMC= p / (est * est)

#En esta condición estamos diciendo que las variables (n, ap, am,) a la cual son de tipo string, de qeu el usuario no debe dejar espacios en blanco, es igual a error.
#Al igual para las variables (p, e, est), a las cuales son de tpo float() e int(), el usuario no debe de poner menos o igual a 0, es igual a error.
if n == "" or ap == "" or am == "" or p <= 0 or e <= 0 or est <= 0 :
  print("Error reinicie el programa.")

#De lo contrario imprime los valores capturados, de las variables (nombre, apellidos paterno y materno, edad, estatura y peso).
else:
  print("Su nombre completo: " +str(n) + " " +str(ap) + " " +str(am)) 
  print("Conforme a tu edad: " + str(e) + " años")
  print("Conforme a tu peso de: " +str(p)+ " kg y tu estatura " + str(est) + " m")
#Se imprime el resultado del calculo IMC
  print("IMC: " +str(IMC))

#Se hace las posibles variables de lo que arroja el calculo de IMC, e imprime unmensaje de acorde a lo dicho.
  if IMC >= 0 and IMC <= 15.99 :
    print("Delgadez Severa")
  elif IMC >= 16.00 and IMC <= 16.99 :
    print("Delgadez Moderada")
  elif IMC >= 18.50 and IMC <= 24.99 :
    print("Normal")
  elif IMC >= 25.00 and IMC <= 29.99 :
    print(" Sobrepeso")
  elif IMC >= 30.00 and IMC <= 34.99 :
    print("Obesidad leve")
  elif IMC >= 35.00 and IMC <= 39.00 :
    print("Obesidad Media")
  elif IMC >= 40.00:
    print("Obesidad Morbida")

  


