def area(radius):
    return 3.142*radius*radius


def vol(area, length):
    print(area*length)


radius = int(input('Enter the radius:'))
length = int(input('Enter a length:'))


area_calc = area(radius)
vol(area_calc, length)
