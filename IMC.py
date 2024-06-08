n = input("Ingrese su nombre por favor: ")
ap = input("Ingresa su apellido paterno por favor: ")
am = input("Ingresa su apellido materno por favor: ")
e = int (input("Ingresa tu edad en años por favor: "))
p = float(input("Ingresa tu peso o masa en kilogramos por favor:"))
est = float(input("Ingresa tu estatura en metros por favor: "))
IMC= p / (est*est)
print("Su nombre completo: " +str(n) +str(ap) +str(am)) 
print("Conforme a tu edad:" +str(e))
print("Conforme a tu peso de:" +str(p)" y tu estatura " +str(est))
print("IMC: " +str(IMC))
if (n==" "):
  print("Ingresa tu nombre por favor y reinicie el programa.")
elif (ap==" "):
  print("Ingresa el apellido paterno por favor y reinicie el programa.")
elif (am==" "):
  print("Ingresa el apellido materno por favor y reinicie el programa.")
elif (e==" "):
  print("Ingresa tu edad nuevamente en años por favor y reinicie el programa")
elif (p==" "):
  print("Ingresa tu peso nuevamente en kilogramos por favor y reinicie el programa")
elif (est==" "):
  print("Ingresa tu estatura en metros nuevamente por favor y reinice el programa")
elif IMC >= 0 and IMC <= 15.99 :
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

