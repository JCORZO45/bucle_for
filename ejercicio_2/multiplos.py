from re import A


m9=0 
m7=0

for i in range(1000,5001):
    if i%7==0:
        m7=m7+1
    if i%9==0:
        m9=m9+1
    
print("la cantidad de numeros multiplos de 7 son: " +str(m7))
print("la cantidad de numeros multiplos de 9 son: " +str(m9))