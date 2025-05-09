a = 0
b = 0 
for item in range(1,6):
    a += item
c = a
print (c)


contador = 0
for i in range(5):
    for j in range (3):
        if (i+j)%2 == 0:
            contador += 1
print (contador)


x=0
for i in range (1,6):
    x += 1
    if x>10:
        break
print (x)

for i in range (1,10,2):
    print (i)

for i in range(0,10,2):
    if i % 3 == 0: 
        print (i)

nums = [1,2,3,4,5]
result = 1
for num in nums:
    result *= num
    if result > 10:
        break
print (result)


numero = 5
iteracion = 0
suma = 0

for i in range(numero):
    iteracion += 1
    suma += 1
print(f"En la iteracion número {iteracion} la suma vale {suma}.")

