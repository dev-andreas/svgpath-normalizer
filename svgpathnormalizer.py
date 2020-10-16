
def normalize(svgpath, factor):
    tokens = svgpath.split()
    points = init_points(tokens)
    del(tokens)
    largest_number = get_largest_number(points)

    for point in points:
        if point[0].lower() == 'l':
            point = l_normalizer(point, largest_number, factor)
        elif point[0].lower() == 'q':
            point = l_normalizer(point, largest_number, factor)
        elif point[0].lower() == 'c':
            point = l_normalizer(point, largest_number, factor)
        elif point[0].lower() == 'a':
            point = l_normalizer(point, largest_number, factor)
    del(largest_number)

    svgpath = ''
    
    for point in points:
        for token in point:
            svgpath += token + ' '
    return svgpath

def l_normalizer(point, largest_number, factor):
    x = float(point[1])
    y = float(point[2])

    x /= (largest_number / factor)
    y /= (largest_number / factor)

    point[1] = str(x)
    point[2] = str(y)
    
    return point

def q_normalizer(point, largest_number, factor):
    point = l_normalizer(point, largest_number, factor)

    c_x = float(point[3])
    c_y = float(point[4])

    c_x /= (largest_number / factor)
    c_y /= (largest_number / factor)

    point[3] = str(c_x)
    point[4] = str(c_y)
    return point

def c_normalizer(point, largest_number, factor):
    point = q_normalizer(point, largest_number, factor)
    c_x = float(point[5])
    c_y = float(point[6])

    c_x /= (largest_number / factor)
    c_y /= (largest_number / factor)

    point[5] = str(c_x)
    point[6] = str(c_y)
    return point

def a_normalizer(point, largest_number, factor):
    point = q_normalizer(point, largest_number, factor)
    return point

def init_points(tokens):
    points = []
    point = []

    current_type = tokens[0]
    point.append(tokens[0])

    for token in tokens[1:]:
        if is_number(token):
            point.append(token)
        else:
            points.append(point)
            point = []
            point.append(token)
    return points

def get_largest_number(points):
    largest_number = 0
    for point in points:
        number1 = float(point[1])
        number2 = float(point[2])
        if number1 > largest_number:
            largest_number = number1
        if number2 > largest_number:
            largest_number = number2
    return largest_number

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

print(normalize('M 400 300 A 50 125 0 1 1 475 300 L 450 375 L 225 325 Q 350 250 200 200 L 275 50 C 300 175 650 125 575 175 A 50 50 0 1 1 550 450 ', 1))