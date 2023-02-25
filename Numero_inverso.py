# Programa entregar un número de 3 digitos inverso

print("----------------------------------")
print("------------NÚMERO INVERSO--------")
print("----------------------------------")

#input
n= int(input("Digite el valor de n= "))

#procesing
mod= n%10
de= n//10%10
m= n//100
ni= mod*100 + de*10 + m


#ouput
print("------------------------------")
print("------------RESULTADOS--------")
print("------------------------------")
print("Modulo: " + str(mod))
print("División parte entera: " + str(de))
print("División parte entera del ultimo digito: " + str(m))
print("Resultado " + str(ni))