import random
cara1=0
cara2=0
cara3=0
cara4=0
cara5=0
cara6=0
n=int(input("Digita la cantidad de dados que deseas lanzar: "))

for i in range(1,n+1):
    b=random.randint(1,6)
    if b==1:
        cara1=cara1+1
    if b==2:
        cara2=cara2+1
    if b==3:
        cara3=cara3+1
    if b==4:
        cara4=cara4+1
    if b==5:
        cara5=cara5+1
    if b==6:
        cara6=cara6+1

print("EL numero 1 cayo: " + str(cara1) + " veces" )
print("EL numero 2 cayo: " + str(cara2) + " veces" )
print("EL numero 3 cayo: " + str(cara3) + " veces" )
print("EL numero 4 cayo: " + str(cara4) + " veces" )
print("EL numero 5 cayo: " + str(cara5) + " veces" )
print("EL numero 6 cayo: " + str(cara6) + " veces" )

