#Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь

leg1 = float(input('Enter leg 1: '))
leg2 = float(input('Enter leg 2: '))

hypotenuse = (leg1 ** 2 + leg2 ** 2) ** 0.5
area = (leg1 * leg2) / 2

print("Hypotenuse =", hypotenuse)
print("Area =", area)