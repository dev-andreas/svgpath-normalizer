'''Module for scaling and svgpaths'''
class SVGNormalizer(object):

    def __init__(self):
        self.__prev_scaled_path = None
    
    def scale(self, svgpath, scalar: float=1) -> str:
        tokens = svgpath.split()
        points = self.__init_points(tokens)
        del(tokens)
        largest_number = self.__get_largest_number(points)

        for point in points:
            if point[0].lower() == 'm':
                point = self.__l_normalizer(point, largest_number, scalar)
            if point[0].lower() == 'l':
                point = self.__l_normalizer(point, largest_number, scalar)
            elif point[0].lower() == 'q':
                point = self.__q_normalizer(point, largest_number, scalar)
            elif point[0].lower() == 'c':
                point = self.__c_normalizer(point, largest_number, scalar)
            elif point[0].lower() == 'a':
                point = self.__a_normalizer(point, largest_number, scalar)

        svgpath = ''
        
        for point in points:
            for token in point:
                svgpath += token + ' '
        self.__prev_scaled_path = svgpath
        return svgpath

    def __l_normalizer(self, point: list, largest_number: float, scalar: float) -> list:
        x = float(point[1])
        y = float(point[2])

        x /= (largest_number / scalar)
        y /= (largest_number / scalar)

        point[1] = str(x)
        point[2] = str(y)
        return point

    def __q_normalizer(self, point: list, largest_number: float, scalar: float) -> list:
        point = self.__l_normalizer(point, largest_number, scalar)

        c_x = float(point[3])
        c_y = float(point[4])

        c_x /= (largest_number / scalar)
        c_y /= (largest_number / scalar)

        point[3] = str(c_x)
        point[4] = str(c_y)
        return point

    def __c_normalizer(self, point: list, largest_number: float, scalar: float) -> list:
        point = self.__q_normalizer(point, largest_number, scalar)
        c_x = float(point[5])
        c_y = float(point[6])

        c_x /= (largest_number / scalar)
        c_y /= (largest_number / scalar)

        point[5] = str(c_x)
        point[6] = str(c_y)
        return point

    def __a_normalizer(self, point: list, largest_number: float, scalar: float) -> list:
        point = self.__l_normalizer(point, largest_number, scalar)

        p_x = float(point[6])
        p_y = float(point[7])

        p_x /= (largest_number / scalar)
        p_y /= (largest_number / scalar)

        point[6] = str(p_x)
        point[7] = str(p_y)
        return point

    def __init_points(self, tokens: list) -> list:
        points = []
        point = []

        current_type = tokens[0]
        point.append(tokens[0])

        for token in tokens[1:]:
            if self.__is_number(token):
                point.append(token)
            else:
                points.append(point)
                point = []
                point.append(token)
        points.append(point)
        return points

    def __get_largest_number(self, points: list) -> float:
        largest_number = 0
        for point in points:
            number1, number2 = 0, 0
            
            if point[0].lower() == 'z':
                continue
            elif point[0].lower() ==  'a':
                number1 = float(point[6])
                number2 = float(point[7])
            else:
                number1 = float(point[1])
                number2 = float(point[2])
            
            if number1 > largest_number:
                largest_number = number1
            if number2 > largest_number:
                largest_number = number2
        return largest_number

    def __is_number(self, s: str) -> bool:
        try:
            float(s)
            return True
        except ValueError:
            return False

    # GETTERS AND SETTERS

    def __get_prev_scaled_path(self) -> str:
        return self.__prev_scaled_path

    # PROPERTIES

    prev_scaled_path: str = property(__get_prev_scaled_path, None)
        
