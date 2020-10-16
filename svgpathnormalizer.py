
testing_path = 'M 100 300 Q 150 50 200 300 Q 250 550 300 300 Q 350 50 400 300 C 450 550 450 50 500 300 C 550 50 550 550 600 300 A 50 50 0 1 1 700 300 '

def normalize(svgpath, scalar):
    tokens = svgpath.split()
    points = init_points(tokens)
    del(tokens)
    largest_number = get_largest_number(points)

    for point in points:
        if point[0].lower() == 'm':
            point = l_normalizer(point, largest_number, scalar)
        if point[0].lower() == 'l':
            point = l_normalizer(point, largest_number, scalar)
        elif point[0].lower() == 'q':
            point = l_normalizer(point, largest_number, scalar)
        elif point[0].lower() == 'c':
            point = l_normalizer(point, largest_number, scalar)
        elif point[0].lower() == 'a':
            point = l_normalizer(point, largest_number, scalar)
    del(largest_number)

    svgpath = ''
    
    for point in points:
        for token in point:
            svgpath += token + ' '
    return svgpath

def l_normalizer(point, largest_number, scalar):
    x = float(point[1])
    y = float(point[2])

    x /= (largest_number / scalar)
    y /= (largest_number / scalar)

    point[1] = str(x)
    point[2] = str(y)
    
    return point

def q_normalizer(point, largest_number, scalar):
    point = l_normalizer(point, largest_number, scalar)

    c_x = float(point[3])
    c_y = float(point[4])

    c_x /= (largest_number / scalar)
    c_y /= (largest_number / scalar)

    point[3] = str(c_x)
    point[4] = str(c_y)
    return point

def c_normalizer(point, largest_number, factor):
    point = q_normalizer(point, largest_number, scalar)
    c_x = float(point[5])
    c_y = float(point[6])

    c_x /= (largest_number / scalar)
    c_y /= (largest_number / scalar)

    point[5] = str(c_x)
    point[6] = str(c_y)
    return point

def a_normalizer(point, largest_number, scalar):
    point = q_normalizer(point, largest_number, scalar)
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
    
