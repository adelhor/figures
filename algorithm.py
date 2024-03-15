import math
from abc import ABC, abstractmethod
import mysql.connector
import sys
from dotenv import load_dotenv
import os
import json

load_dotenv()


class DatabaseManager:
    def __init__(self):
        """
        making connection to database and checking the connection status
        """
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
        """
        method that allows to close the connection do database
        """
        if self.mydb.is_connected():
            self.mycursor.close()
            self.mydb.close()
            print(" -> Connection to database is closed now.")


class Figure:
    """
    getting calculated area and circuit and setting into rounded value
    """

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = round(value, 2)

    @property
    def circuit(self):
        return self._circuit

    @circuit.setter
    def circuit(self, value):
        self._circuit = round(value, 2)

    def __init__(self, figure_name):
        """
        parent class all the figure types
        Args:
            figure_name (string): type of figure/shape
        """
        self.figure_name = figure_name

    def write_results_to_database(self, area, circuit):
        """
        method that allows to write calculated area and circuit to database
        also, returning the id of the last calculations that have been added to databse

        Args:
            area (float): calculated area of the figure
            circuit (float): calculated circuit of the figure

        Returns:
            int: shape_id - id of the figure that was under analysis
        """
        self.area = area
        self.circuit = circuit
        sql = "INSERT INTO results(shape, area, circuit) values(%s, %s, %s)"
        val = (self.figure_name, self.area, self.circuit)
        db_manager = DatabaseManager()
        db_manager.mycursor.execute(sql, val)
        db_manager.mydb.commit()
        inserted_id = db_manager.mycursor.lastrowid
        print("Results have been added.")
        db_manager.close_connection()
        return inserted_id

    def write_parameters_to_database(self):
        """
        method that allows to add parameters in string format due to different numbers of parameters for each figure
        """
        list_of_parameters_json = json.dumps(self.list_of_parameters)
        try:
            inserted_id = self.write_results_to_database()
            db_manager = DatabaseManager()
            sql = "INSERT INTO parameters(SHAPE_ID, parameters) values(%s,%s)"
            val = (
                inserted_id,
                list_of_parameters_json,
            )
            db_manager = DatabaseManager()
            db_manager.mycursor.execute(sql, val)
            db_manager.mydb.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        print("The record has been added")
        db_manager.close_connection()


class Square(Figure):
    def __init__(self, figure_name, list_of_parameters):
        """
        child class for square shape

        Args:
            figure_name (str): name of the figure, here: square
            list_of_parameters (list): list of parameters
        """
        super().__init__(figure_name)
        self.list_of_parameters = list_of_parameters
        self.write_parameters_to_database()

    def write_results_to_database(self):
        """
        method calculating the area and circuit of square and calling the parent method that adds results to database
        """
        area = pow(self.list_of_parameters[0], 2)
        circuit = 4 * self.list_of_parameters[0]
        super().write_results_to_database(area, circuit)


class Triangle(Figure):
    def __init__(self, figure_name, list_of_parameters):
        """
        child class for triangle shape

        Args:
            figure_name (float): name of the figure, here: triangle
            list_of_parameters (list): list of parameters
        """
        super().__init__(figure_name)
        self.list_of_parameters = list_of_parameters
        self.write_parameters_to_database()

    def write_results_to_database(self):
        """
        method calculating the area and circuit of triangle and calling the parent method that adds results to database
        """
        area = self.list_of_parameters[0] * self.list_of_parameters[3] * (1 / 2)
        circuit = (
            self.list_of_parameters[0]
            + self.list_of_parameters[1]
            + self.list_of_parameters[2]
        )
        super().write_results_to_database(area, circuit)


class Circle(Figure):
    def __init__(self, figure_name, list_of_parameters):
        """
        child class for circle shape

        Args:
            figure_name (float): name of the figure, here: circle
            list_of_parameters (list): list of parameters
        """
        super().__init__(figure_name)
        self.list_of_parameters = list_of_parameters
        self.write_parameters_to_database()

    def write_results_to_database(self):
        """
        method calculating the area and circuit of circle and calling the parent method that adds results to database
        """
        area = math.pi * pow(self.list_of_parameters[0], 2)
        circuit = 2 * math.pi * self.list_of_parameters[0]
        super().write_results_to_database(area, circuit)


class Trapezoid(Figure):
    def __init__(self, figure_name, list_of_parameters):
        """
        child class for trapzoid shape

        Args:
            figure_name (float): name of the figure, here: trapezoid
            list_of_parameters (list): list of parameters
        """
        super().__init__(figure_name)
        self.list_of_parameters = list_of_parameters
        self.write_results_to_database()
        self.write_parameters_to_database()

    def write_results_to_database(self):
        """
        method calculating the area and circuit of trapezoid and calling the parent method that adds results to database
        """
        area = (
            (self.list_of_parameters[0] + self.list_of_parameters[1])
            * self.list_of_parameters[4]
            / 2
        )
        circuit = (
            self.list_of_parameters[0]
            + self.list_of_parameters[1]
            + self.list_of_parameters[2]
            + self.list_of_parameters[3]
        )
        super().write_results_to_database(area, circuit)


class DbManipulation:
    def __init__(self, figure_id):
        """
        class allowing for differnet actions on database

        Args:
            figure_id (int): id of the figure
        """
        self.figure_id = figure_id

    def removing_figure(self):
        """
        method allowing to delete the calculation from database by chosing the id of the figure
        """
        sql = "DELETE FROM results WHERE SHAPE_ID = %s"
        val = (self.figure_id,)
        db_manager = DatabaseManager()
        db_manager.mycursor.execute(sql, val)
        db_manager.mydb.commit()
        db_manager.close_connection()
        print(
            f"Record ID: {self.figure_id} is deleted."
            f"\n {db_manager.mycursor.rowcount} record deleted"
        )

    @staticmethod
    def showing_figures():
        """
        showing the list of calculated figures that are in database

        Returns:
            list: list of all calculated figures that were added to database
        """
        db_manager = DatabaseManager()
        db_manager.mycursor.execute("SELECT * FROM results")
        result = db_manager.mycursor.fetchall()
        return result
