import z5mymodule

def main():
    print(z5mymodule.module_description())
    print(z5mymodule.greet("Алиса"))

    square_side = 5
    circle_radius = 3

    square_area = z5mymodule.calculate_square_area(square_side)
    circle_area = z5mymodule.calculate_circle_area(circle_radius)

    print(f"Площадь квадрата с длиной стороны {square_side}: {square_area}")
    print(f"Площадь круга с радиусом {circle_radius}: {circle_area}")

if __name__ == "__main__":
    main()