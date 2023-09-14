from Figures import *
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Y1012Jqkhkp',
    database = 'adelh'
)

mycursor=mydb.cursor()


#figures = "CREATE TABLE figures (ID int AUTO_INCREMENT, SHAPE char(255), FIRST_PARAMETER FLOAT(10,2), SECOND_PARAMETER FLOAT(10,2), THIRD_PARAMETER FLOAT(10,2), FOURTH_PARAMETER FLOAT(10,2), HEIGHT FLOAT(10,2), PRIMARY KEY (ID));"
#mycursor.execute(figures)

#mycursor.execute("DROP TABLE IF EXISTS figures")

#properties = "CREATE TABLE properties (ID int AUTO_INCREMENT, SHAPE char(255), AREA FLOAT(10,2), CIRCUIT FLOAT(10,2), PRIMARY KEY (ID));"
#mycursor.execute(properties)

while True:
    mycursor.execute("ALTER TABLE figures AUTO_INCREMENT = 1")
    mycursor.execute("ALTER TABLE properties AUTO_INCREMENT = 1")

    user_option = input('What would you like to perform? \n If add press 1, \n if delete press 2, \n if show table with figures press 3, \n if show table with properties press 4, \n if exit press 5. \n')
    user_option = int(user_option)
    if user_option == 1:
        shape = input("What is the shape? Square, circle, triangle or trapezoid? \n")
        if shape == 'square':
            a = input('Size of the sides: \n')
            a = float(a)
            '''
            sql = "INSERT INTO figures(shape,first_parameter) values(%s, %s)"
            val = (shape, a)
            mycursor.execute(sql, val)
            mydb.commit() #MUST BE to make changes in table
            print('The record has been added')
            '''
            figure = Square(a)
            
            '''
            area = figure.area
            circuit = figure.circuit
            sql2 = "INSERT INTO properties(shape,area, circuit) values(%s, %s, %s)"
            val2 = (shape, area, circuit)
            mycursor.execute(sql2, val2)
            mydb.commit() #MUST BE to make changes in table
            '''

        elif shape == 'triangle':
            a = input('Size of the base: \n')
            a = float(a)
            b = input('Size of the first leg: \n')
            b = float(b)
            c = input('Size of the second leg: \n')
            c = float(c)
            h = input('Size of the height: \n')
            h = float(h)
            
            figure = Triangle(a,b,c,h)

        elif shape == 'circle':
            radius = input('Size of the radius: \n')
            radius = float(radius)

            figure = Circle(radius)

        elif shape == 'trapezoid':
            base = input('Size of the first base: \n')
            base = float(base)
            base2 = input('Size of the second base: \n')
            base2 = float(base2)
            leg = input('Size of the first leg: \n')
            leg = float(leg)
            leg2 = input('Size of the second leg: \n')
            leg2 = float(leg2)
            h = input('Size of the height: \n')
            h = float(h)

            figure = Trapezoid(base, base2, leg, leg2, h)
        
        '''
        first = float(input("What is the first parameter:\n"))
        second = float(input("What is the second parameter:\n"))
        third = float(input("What is the third parameter:\n"))
        fourth = float(input("What is the fourth parameter:\n"))
        h = float(input("What is the height:\n"))
        sql = "INSERT INTO figures(shape,first_parameter) values(%s, %s, %s, %s, %s, %s)"
        val = (shape, first, second, third, fourth, h)
        mycursor.execute(sql, val)
        mydb.commit() #MUST BE to make changes in table
        print('The record has been added')
        '''

    elif user_option == 2:
        figure_id = int(input('Which figure do want to delete. Input the ID \n'))
        sql = "DELETE FROM figures WHERE ID = %s"
        sql2 = "DELETE FROM properties WHERE ID = %s"
        val = (figure_id,)
        mycursor.execute(sql, val)
        mycursor.execute(sql2, val)
        mydb.commit()
        print(mycursor.rowcount, "record deleted")

    elif user_option == 3:
        mycursor.execute("SELECT * FROM figures")
        result = mycursor.fetchall()
        print(result)

    elif user_option == 4:
        mycursor.execute("SELECT * FROM properties")
        result = mycursor.fetchall()
        print(result)

    elif user_option == 5:
        break

    else:
        print('Wrong input')


'''
i=0
my_list=[]
while i<3:
    which_figure = input('Which figure do you want to analyze: square, triangle, circle or trapezoid? \nIf none write exit \n')
    if which_figure == 'square':
        a = input('Size of the sides: \n')
        a = float(a)
        figure = Square(a)
        my_list.append(figure)
        #print(f"The area for this figure equals: {figure.area}")
        #print (f"The circuit for this figure equals: {figure.circuit}")

    elif which_figure == 'triangle':
        a = input('Size of the base: \n')
        a = float(a)
        b = input('Size of the first leg: \n')
        b = float(b)
        c = input('Size of the second leg: \n')
        c = float(c)
        h = input('Size of the height: \n')
        h = float(h)
        figure = Triangle(a,b,c,h)
        my_list.append(figure)
        #print(f"The area for this figure equals: {figure.area}")
        #print (f"The circuit for this figure equals: {figure.circuit}")

    elif which_figure == 'circle':
        radius = input('Size of the radius: \n')
        radius = float(radius)
        figure = Circle(radius)
        my_list.append(figure)
        #print(f"The area for this figure equals: {figure.area}")
        #print (f"The circuit for this figure equals: {figure.circuit}")

    elif which_figure == 'trapezoid':
        base = input('Size of the first base: \n')
        base = float(base)
        base2 = input('Size of the second base: \n')
        base2 = float(base2)
        leg = input('Size of the first leg: \n')
        leg = float(leg)
        leg2 = input('Size of the second leg: \n')
        leg2 = float(leg2)
        h = input('Size of the height: \n')
        h = float(h)
        figure = Trapezoid(base, base2, leg, leg2, h)
        my_list.append(figure)
        #print(f"The area for this figure equals: {figure.area}")
        #print (f"The circuit for this figure equals: {figure.circuit}")
    
    elif which_figure == 'exit':
        break

    else:
        print('Wrong shape. Try again')
        i=i-1
    i+=1

if i==3:
   with open ('C:/Users/adelh/OneDrive/Pulpit/figures.txt', 'w') as f:
        for figure in my_list:
            f.write(f'For {figure.figure_name} the area equals: {figure.area} and the circuit equals: {figure.circuit} \n')
'''
