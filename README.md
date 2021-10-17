
# cs6375-project
A project for CS 6375, Introduction to Machine Learning

## Installation
Running this program requires some dependencies such as Pandas and Numpy. I've provided a requirements.txt to be able to quickly get it running on your machine. To install the dependencies:

 1. Install Python3 and Pip3
 2. Using pip3 (the package manager), install 
		 
		 python3 -m pip install --user virtualenv
 3. Then create a virtual environment within the project directory

        cd /<...>/cs6375-project
        python3 -m venv project-venv
	> This venv is to ensure that dependencies for this project don't conflict with python dependencies you may have installed elsewhere
4. Activate your venv by typing

		source project-venv/bin/activate
5. Then install the dependencies with pip
		
		pip3 install -r requirements.txt

## Running the Program
In order to run the program, type in:

		python3 project1.py --dataset test.csv
							--input partition2.txt
							--output partition-3.txt

