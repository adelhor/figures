# Figures calculation tool

## Overview
This project is a Python-based solution designed to calculate area and circuit of figure (square, triangle, circle and trapezoid) chosen by user. This project includes essential components to manipulate data, execute core algorithms, and interact with a database.

## Installation
To set up this project locally, clone the repository and install the required dependencies:

```bash
git clone https:/https://github.com/adelhor/figures.git
cd figures
pip install -r requirements.txt
```

## Usage
Launch the application by executing the main.py script. Follow the interactive prompts to choose figures and calculate their properties:

```bash
python main.py
```

## Key Components
algorithm.py: Houses the core logic for calculating properties of geometric figures. It includes methods for area, perimeter, and possibly volume computations, depending on the figure types handled.

main.py: The entry point of the application, main.py manages user input and coordinates the calculation processes by leveraging the algorithm.py functionalities.

tabeles_creation.py: Script that contains connection to database and creation of tables - results and parameteres.

