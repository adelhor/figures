import math
from abc import ABC, abstractmethod
import mysql.connector
import sys
from dotenv import load_dotenv
import os
import json


class DatabaseManager:
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password=os.getenv("PASSWORD"),
                database="figures",
            )
            self.mycursor = self.mydb.cursor()
        except Exception as e:
            print(e)
            sys.exit()

    def close_connection(self):
        if self.mydb.is_connected():
            self.mycursor.close()
            self.mydb.close()
            print("Connection to database is closed now.")


class Figure(ABC):

    @property  # getter creation
    def area(self):
        return self._area

    @area.setter  # setter creation, value rounded
    def area(self, value):
        self._area = round(value, 2)

    @property
    def circuit(self):
        return self._circuit

    @circuit.setter
    def circuit(self, value):
        self._circuit = round(value, 2)

    def __init__(self, figure_name, list_of_parameters):
        self.figure_name = figure_name
        self.list_of_parameters = list_of_parameters

    def write_results_to_database(self):
        sql = "INSERT INTO results(shape, area, circuit) values(%s, %s, %s)"
        val = (self.figure_name, self.area, self.circuit)
        db_manager = DatabaseManager()
        db_manager.mycursor.execute(sql, val)
        db_manager.mydb.commit()
        db_manager.close_connection()

    @abstractmethod
    def write_parameters_to_database(self):
        list_of_parameters_json = json.dumps(self.list_of_parameters)
        sql = "INSERT INTO figures(parameters) values(%s)"
        val = list_of_parameters_json
        db_manager = DatabaseManager()
        db_manager.mycursor.execute(sql, val)
        db_manager.mydb.commit()
        db_manager.close()
        print("The record has been added")


class Square(Figure):
    def __init__(self, figure_name, list_of_parameters):
        super().__init__("square", list_of_parameters=[])
        # self.write_results_to_database()
        # self.write_parameters_to_database()

    def write_results_to_database(self):
        self.area = pow(self.list_of_parameters[0], 2)
        self.circuit = 4 * self.list_of_parameters[0]
        super().write_results_to_database(self.area, self.circuit)

    def write_parameters_to_database(self):
        return super().write_parameters_to_database()


class Triangle(Figure):
    def __init__(self, figure_name, list_of_parameters):
        super().__init__("triangle", list_of_parameters=[])
        self.write_results_to_database()
        self.write_parameters_to_database()

    def write_results_to_database(self):
        self.area = self.list_of_parameters[0] * self.list_of_parameters[3] * (1 / 2)
        self.circuit = (
            self.list_of_parameters[0]
            + self.list_of_parameters[1]
            + self.list_of_parameters[2]
        )
        super().write_results_to_database(self.area, self.circuit)

    def write_parameters_to_database(self):
        return super().write_parameters_to_database()


class Circle(Figure):
    def __init__(self, figure_name, list_of_parameters):
        super().__init__("circle", list_of_parameters=[])
        self.write_results_to_database()
        self.write_parameters_to_database()

    def write_results_to_database(self):
        self.area = math.pi * pow(self.list_of_parameters[0], 2)
        self.circuit = 2 * math.pi * self.list_of_parameters[0]
        super().write_results_to_database(self.area, self.circuit)

    def write_parameters_to_database(self):
        return super().write_parameters_to_database()


class Trapezoid(Figure):
    def __init__(self, figure_name, list_of_parameters):
        super().__init__("trapezoid", list_of_parameters=[])
        self.write_results_to_database()
        self.write_parameters_to_database()

    def write_results_to_database(self):
        self.area = (
            (self.list_of_parameters[0] + self.list_of_parameters[1])
            * self.list_of_parameters[4]
            / 2
        )
        self.circuit = (
            self.list_of_parameters[0]
            + self.list_of_parameters[1]
            + self.list_of_parameters[2]
            + self.list_of_parameters[3]
        )
        super().write_results_to_database(self.area, self.circuit)

    def write_parameters_to_database(self):
        return super().write_parameters_to_database()


class DbManipulation:
    def __init__(self, figure_id):
        self.figure_id = figure_id

    def removing_figure(self):
        sql = "DELETE FROM figures WHERE ID = %s"
        # sql2 = "DELETE FROM properties WHERE ID = %s"
        val = (self.figure_id,)
        db_manager = DatabaseManager()
        db_manager.mycursor.execute(sql, val)
        # mycursor.execute(sql2, val)
        db_manager.mydb.commit()
        db_manager.close()
        print(
            f"Record ID: {self.figure_id} is deleted."
            f"\n {db_manager.mycursor.rowcount} record deleted"
        )

    @staticmethod
    def showing_figures():
        db_manager = DatabaseManager()
        db_manager.mycursor.execute("SELECT * FROM figures")
        result = db_manager.mycursor.fetchall()
        print(result)
