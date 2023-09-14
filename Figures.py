import math
from abc import ABC, abstractclassmethod, abstractmethod
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Y1012Jqkhkp',
    database = 'adelh'
)
mycursor=mydb.cursor()
class Figures(ABC):

    @property #getter creation
    def area(self):
        return self._area
    @area.setter #setter creation, value rounded
    def area(self,value):
        self._area = round(value,2)
    
    @property
    def circuit(self):
        return self._circuit
    @circuit.setter
    def circuit(self,value):
        self._circuit = round(value,2)
    
    def __init__(self,figure_name):
       self.figure_name = figure_name
    
    #@abstractmethod
    def write(self,area, circuit):
        #print(f"The area for {self.figure_name} equals: {self.area}")
        sql = "INSERT INTO properties(shape, area, circuit) values(%s, %s, %s)"
        val = (self.figure_name,self.area, self.circuit)
        mycursor.execute(sql, val)
        mydb.commit()
        #pass
    #@abstractmethod
    #def write_circuit(self,circuit):
        #print(f"The area for {self.figure_name} equals: {self.circuit}")

class Square(Figures):
    def __init__(self,a):
        super().__init__('square')
        self.a = a
        self.calculate()
        self.write_parameters()
        #self.calculate_circuit()
    def calculate(self):
        self.area = self.a*self.a
        self.circuit = 4 * self.a
        super().write(self.area, self.circuit)
    #def calculate_circuit(self):
        #super().write(self.circuit)
    def write_parameters(self):
        sql = "INSERT INTO figures(shape,first_parameter) values(%s, %s)"
        val = (self.figure_name, self.a)
        mycursor.execute(sql, val)
        mydb.commit() #MUST BE to make changes in table
        print('The record has been added')

class Triangle(Figures):
    def __init__(self,a,b,c,h):
        super().__init__('triangle')
        self.a = a
        self.b = b
        self.c = c
        self.h = h
        self.calculate()
        self.write_parameters()
        #self.calculate_circuit()
    def calculate(self):
        self.area = self.a * self.h * (1/2)
        self.circuit = self.a + self.b + self.c
        super().write(self.area, self.circuit)
    #def calculate_circuit(self):
        #super().write_circuit(self.circuit)
    def write_parameters(self):
        sql = "INSERT INTO figures(shape, first_parameter, second_parameter, third_parameter, height) values(%s, %s, %s, %s, %s)"
        val = (self.figure_name, self.a, self.b, self.c, self.h)
        mycursor.execute(sql, val)
        mydb.commit() #MUST BE to make changes in table
        print('The record has been added')

class Circle(Figures):
    def __init__(self, radius):
        super().__init__('circle')
        self.radius = radius
        self.calculate()
        self.write_parameters()
        #self.calculate_circuit()
    def calculate(self):
        self.area = math.pi * self.radius * self.radius
        self.circuit = 2*math.pi * self.radius
        super().write(self.area, self.circuit)
    #def calculate_circuit(self):
        #super().write_circuit(self.circuit)
    def write_parameters(self):
        sql = "INSERT INTO figures(shape,first_parameter) values(%s, %s)"
        val = (self.figure_name, self.radius)
        mycursor.execute(sql, val)
        mydb.commit() #MUST BE to make changes in table
        print('The record has been added')

class Trapezoid(Figures):
    def __init__(self, base, base2, leg, leg2, h):
        super().__init__('trapezoid')
        self.base = base
        self.base2 = base2
        self.leg = leg
        self.leg2 = leg2
        self.h = h
        self.calculate()
        self.write_parameters()
        #self.calculate_circuit()
    def calculate(self):
        self.area = ((self.base + self.base2) * (1/2)) / self.h
        self.circuit = self.base + self.base2 + self.leg + self.leg2
        super().write(self.area, self.circuit)
   # def calculate_circuit(self):
        #super().write_circuit(self.circuit)
    def write_parameters(self):
        sql = "INSERT INTO figures(shape,first_parameter, second_parameter, third_parameter, fourth_parameter, height) values(%s, %s, %s, %s, %s, %s)"
        val = (self.figure_name, self.base, self.base2, self.leg, self.leg2, self.h)
        mycursor.execute(sql, val)
        mydb.commit() #MUST BE to make changes in table
        print('The record has been added')





