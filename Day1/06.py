# find the area of rectangle circle and square
a = int(input("Enter Number a: "))
b = int(input("Enter Number b: "))

area_rectangle = a * b
area_square = a * a
area_circle = 3.14 * a * a

perimeter_rectangle = 2 * (a + b)
perimeter_square = 4 * a
perimeter_circle = 2 * (3.14 * a)

print("Area of Rectangle:", area_rectangle)
print("Area of Square:", area_square)
print("Area of circle:", area_circle)

print("Peremeter of circle:", perimeter_circle)
print("Peremeter of square:", perimeter_square)
print("Peremeter of rectangle:", perimeter_rectangle)
