from algorithm import *


while True:
    user_option_text = input(
        "Make your choice: "
        "\n Making calculation - press 1, "
        "\n Deleting the chosen figure - press 2, "
        "\n Checking the table with figures that calculated - press 3,"
        "\n Leaving the program - press 4. \n"
    )
    user_option = int(user_option_text)
    user_figure: Square | Triangle | Circle | Trapezoid | None = None
    if user_option == 1:
        shape = input(
            "What is the shape of your figure? Square, circle, triangle or trapezoid? \n"
        )
        parameters = []
        if shape == "square":
            side_length = float(input("Size of the sides: \n"))
            parameters.append(side_length)
            user_figure = Square(shape, parameters)

        elif shape == "triangle":
            triangle_base = float(input("Size of the base: \n"))
            parameters.append(triangle_base)
            first_leg = float(input("Size of the first leg: \n"))
            parameters.append(first_leg)
            second_leg = float(input("Size of the second leg: \n"))
            parameters.append(second_leg)
            height = float(input("Size of the height: \n"))
            parameters.append(height)
            user_figure = Triangle(shape, parameters)

        elif shape == "circle":
            radius = float(input("Size of the radius: \n"))
            parameters.append(radius)
            user_figure = Circle(shape, parameters)

        elif shape == "trapezoid":
            first_base = float(input("Size of the first base: \n"))
            parameters.append(first_base)
            second_base = float(input("Size of the second base: \n"))
            parameters.append(second_base)
            first_leg = float(input("Size of the first leg: \n"))
            parameters.append(first_leg)
            second_leg = float(input("Size of the second leg: \n"))
            parameters.append(second_leg)
            height = float(input("Size of the height: \n"))
            parameters.append(height)
            user_figure = Trapezoid(shape, parameters)
        else:
            print("Wrong type of the figure, I can not calculate it.")

    elif user_option == 2:
        figure_id = int(input("Which figure do want to delete. Input the ID \n"))
        chosen_figure = DbManipulation(figure_id)
        DbManipulation.removing_figure(chosen_figure)

    elif user_option == 3:
        table_with_results = DbManipulation.showing_figures()
        print(table_with_results)

    elif user_option == 4:
        print("See you again!")
        break

    else:
        print("Wrong input")
