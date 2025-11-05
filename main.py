def calculate_area(shape, size1, size2=None):
    """
    Вычисляет площадь фигуры.
    shape: str - тип фигуры ('square', 'circle', 'triangle', 'rectangle')
    size1: float - сторона/радиус/основание
    size2: float (optional) - высота (для треугольника или прямоугольника)
    """
    shape = shape.lower()
    if shape == "square":
        return size1 * size1
    elif shape == "circle":
        return 3.14 * size1 * size1
    elif shape == "triangle":
        if size2 is None:
            return "Ошибка: нужна высота"
        return 0.5 * size1 * size2
    elif shape == "rectangle":
        if size2 is None:
            return "Ошибка: нужна вторая сторона"
        return size1 * size2
    else:
        return "Неизвестная фигура"


# Пример использования
if __name__ == "__main__":
    shape = input("Введите фигуру: ")
    size1 = float(input("Введите размер 1: "))
    size2 = None
    if shape.lower() in ["triangle", "rectangle"]:
        size2 = float(input("Введите размер 2: "))
    
    area = calculate_area(shape, size1, size2)
    print(f"Площадь фигуры: {area}")
