ax = float(input('Введите координату x для точки A:'))
ay = float(input('Введите координату y для точки A:'))
bx = float(input('Введите координату x для точки B:'))
by = float(input('Введите координату y для точки B:'))
points_lenght = float((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5
print(f'Расстояние между точками A и B равно {round(points_lenght, 3)}')