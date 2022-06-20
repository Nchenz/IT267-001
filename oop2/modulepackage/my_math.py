PI = 3.1416
def sqrt(number):
    #return (number * number)
    return (number**2)

def circle_area(radius):
    area = PI * radius
    return area

if __name__ == '__main__':
    print(sqrt(5))
    print(circle_area(1))
    print(PI)