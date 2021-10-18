
# cs6375-project
A project for CS 6375, Introduction to Machine Learning

## Installation
Running this program requires some dependencies such as Pandas and Numpy. I've provided a requirements.txt to be able to quickly get it running on your machine. To install the dependencies:
		
	pip3 install -r requirements.txt

## Running the Program
In order to run the program, type in:

	python3 project1.py --dataset test.csv
			    --input <input>.txt
			    --output <output>.txt
			    
## The Output
The program will output to the console to better allow you to understand the decision making process. Here is some sample output

	Y A1 1.0 1.0 [[4, 5, 6, 7]]
	Y  A2 1.0 1.0 [[4, 5, 6, 7]]
	Y  A3 1.0 1.0 [[4, 5, 6, 7]]
	X2 A1 0.9182958340544896 0.9182958340544896 [[1, 2, 3]]
	X2  A2 0.9182958340544896 0.9182958340544896 [[1, 2, 3]]
	X2  A3 0.9182958340544896 0.6666666666666666 [[1, 2], [3]]
	Partition X2 was replaced with partition X21,X22 using Feature  A3
	
1. Column 1 is the subgroup
2. Column 2 is the attribute
3. Column 3 is the previous entropy for the subgroup
4. Column 4 is the calculated entropy for the subgroup being split by the attribute
5. Column 5 is the split of the subgroup into further subgroups by the attribute

The last line of the output will tell which subgroup was split based on which attributes.
