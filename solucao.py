#Solucao para o Problema
a = int(input("Digite o valor de a "))
b = int(input("Digite o valor de b "))
c = int(input("Digite o valor de c "))

print(a, "x² +", b, "x +", c, "= 0")

delta = b ** 2 - 4 * a * c

print("Delta é igual a:", delta)

x1 = ((-1 * b) + (delta ** 0.5)) / (2 * a)
x2 = ((-1 * b) - (delta ** 0.5)) / (2 * a)

print("x1 =", x1)
print("x2 =", x2)