import random
cara1=""
cara2=""
cara3=""
cara4=""
cara5=""
cara6=""
n=int(input("Digita la cantidad de dados que deseas lanzar: "))

for i in range(1,n+1):
    b=random.randint(1,6)
    if b==1:
        cara1=(cara1+"*")
    if b==2:
        cara2=(cara2+"*")
    if b==3:
        cara3=(cara3+"*")
    if b==4:
        cara4=(cara4+"*")
    if b==5:
        cara5=(cara5+"*")
    if b==6:
        cara6=(cara6+"*")

print("Número 1 : " + str(cara1) )
print("Número 2 : " + str(cara2) )
print("Número 3 : " + str(cara3) )
print("Número 4 : " + str(cara4) )
print("Número 5: " + str(cara5) )
print("Número 6: " + str(cara6) )