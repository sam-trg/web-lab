# WAP to solve quadratic equations

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))
D = pow(b, 2) - 4 * a * c
if D < 0:
    print("Roots are imaginary")
else:
    x1 = (-b + D ** (1 / 2)) / (2 * a)
    x2 = (-b - D ** (1 / 2)) / (2 * a)
    print("Roots of the quadratic equation are", round(x1, 2), "and", round(x2, 2))
