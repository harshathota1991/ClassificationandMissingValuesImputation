
Steps to Run the 1st Program(Missing values)
============================================

Source File : \Missing Values\Machine_Gene\src\Project_Gene_1.java

Step 1: Change the below values in the initial lines. 

        int NUM_OF_COLUMNS =14;  //this is for the first data set
	int NUM_OF_ROWS = 242;   

Step 2: Change the input file name in the read() method.

        XSSFWorkbook worksheet2 = new XSSFWorkbook(new FileInputStream( new File("GeneS1.xlsx")));//For first dataset

Step 3: Run the program and we get the output in the console.

Step 4: we need to paste the output onto an excel file.


Source File : \Machine_Gene\src\Project_Gene_1.java

Step 1: Change the below values in the initial lines. 

        int NUM_OF_COLUMNS = 50;  //this is for the first data set
	int NUM_OF_ROWS = 758;   

Step 2: Change the input file name in the read() method.

        XSSFWorkbook worksheet2 = new XSSFWorkbook(new FileInputStream( new File("GeneS2.xlsx")));//For Second dataset

Step 3: Run the program and we get the output in the console.

Step 4: we need to paste the output onto an excel file.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Steps to Run the 2nd Program (Classification)
=============================================

Source File: \Classification\Classification\src\classification.py

Software Requirements:

Please install Python 2.7 Software
Installation instructions

Instilling dependencies

The code depends on two main packages 
1 .scikit - http://scikit-learn.org/stable/install.html
2. numpy - http://docs.scipy.org/doc/numpy/user/install.html 

The internal dependencies are clearly mentioned in the documentation of the above packages:

Directory structure

src - code directory
    classification.py - main program which performs knn classification and predicts the values

data - input info directory
    test1 - testset 1
        TrainData.txt
        TrainLabel.txt
        TestData.txt
    test2 - testset 2
        TrainData.txt
        TrainLabel.txt
        TestData.txt
    test3 - testset 3
        TrainData.txt
        TrainLabel.txt
        TestData.txt
    test4 - testset 4
        TrainData.txt
        TrainLabel.txt
        TestData.txt

Execution Process

$ python classification.py <test1|test2|test3|test4>


