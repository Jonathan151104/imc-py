Mi nombre es Jonthan Rodriguez Tavares en este código muestro el IMC a la vez pidiendo el nombre del usuario como primera parte
n = input("Ingrese su nombre por favor: ")

Luego pregunto su apellido paterno.
ap = input("Ingresa su apellido paterno por favor: ")

Tambien su apellido materno.
am = input("Ingresa su apellido materno por favor: ")

Le pido su edad.
e = int (input("Ingresa tu edad en años por favor: "))

Cuanto pesa actualmente el usuario ustilizando variable de tipo flotante.
p = float(input("Ingresa tu peso o masa en kilogramos por favor:"))

#Le pido la estatura utilizando flotante.
est = float(input("Ingresa tu estatura en metros por favor: "))

#Se hace el cálculo del Índice de Masa Corporal que es peso sobre estatura al cuadrado.
IMC= p / (est*est)

#Se imprime lo que es su nombre completo utilizando las variables del nombre, apellido paterno y apellido materno.
print("Su nombre completo: " +str(n) +str(ap) +str(am)) 

#Se imprime la edad 
print("Conforme a tu edad:" +str(e))

#Se imprime al usuario su peso y estatura según los datos que nos ingreso.
print("Conforme a tu peso de:" +str(p)" y tu estatura " +str(est))

#En esta parte imprime el resultado del IMC.
print("IMC: " +str(IMC))

La condicional ya sea (if o elif) muestra si en caso que el usurio no ingresa nada en la parte del nombre muestre que lo ingrese y reinicie el programa, a la vez
también en el caso de su apellido materno o paterno, edad, peso y estatura  .
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

En esta parte muestra según IMC ya sea el número que arroje el cálculo, determina si tiene delgadez, delgadez moderada, normal, sobrepeso, obesidad leve, media o morbida, según sea el caso
que se presente.
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

Nota: si en el archivo .py les aparce la (n=) no la pude borar ya no me dejo modificarlo, también como se ejecuta en esta plataforma de github y si les aparece diferentes nombres en las variables, esque el código se modifica solo la verdad se me hace complicado programar en esta parte.

Mi experiencia en lo poco que llevo pues se me complica con las grabación de las clases por que no me avisan ni por correo o mensaje, la verdad se me hace díficil también programar en esta parte devido que no puedo ejecutar el archivo y quiero ver si tiene errores o algo, o si se peude ejecutar por favor digame como para poder hacerlo, la verdad mi experiencia es nula espero me comprendan y me ayudan esta parte se los agradezco, sin nada mas que decir me despido ¡HASTA EL PROXIMO PROGRAMA Y CLASE! Hasta luego

Jonathan Rodríguez Tavares.
