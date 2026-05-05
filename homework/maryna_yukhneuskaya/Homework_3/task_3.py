#Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел

a = int(input("Enter a: "))
b = int(input("Enter b: "))

arithmetic_mean = (a + b) / 2
geometric_mean = (a * b) ** 0.5

print("Arithmetic mean:", arithmetic_mean)
print("Geometric mean:", geometric_mean)

